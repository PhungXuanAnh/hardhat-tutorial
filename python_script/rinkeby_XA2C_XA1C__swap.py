import json
from rinkeby_constant import (
    w3, UNISWAP_ROUTER_V2_ADDRESS, UNISWAP_FACTORY_ADDRESS,
    XA1C_ADDRESS, XA2C_ADDRESS,
    BlockchainDataJsonEncoder,
    DEADLINE, DECIMAL,
    ACCOUNT_2_ADDRESS,
    ACCOUNT_2_PRIVATE_KEY,
    ACCOUNT_3_ADDRESS,
    amount_XA1C_in,
    amount_XA2C_out_min
)

# get router

router_built_file = open('../node_modules/@uniswap/v2-periphery/build/IUniswapV2Router02.json', "r")
router_built_content = json.load(router_built_file)
router_abi = router_built_content["abi"]
router_contract = w3.eth.contract(address=UNISWAP_ROUTER_V2_ADDRESS, abi=router_abi)

# get XA1C_ADDRESS XA2C_ADDRESS instance

ERC20_token_built_file = open('../node_modules/@uniswap/v2-periphery/build/ERC20.json', "r")
ERC20_token_built_content = json.load(ERC20_token_built_file)
ERC20_token_abi = ERC20_token_built_content["abi"]

XA1C = w3.eth.contract(address=XA1C_ADDRESS, abi=ERC20_token_abi)
XA2C = w3.eth.contract(address=XA2C_ADDRESS, abi=ERC20_token_abi)

# check ACCOUNT 2 give allowance router how many XA1C, XA2C

XA1C_allowance = XA1C.functions.allowance(ACCOUNT_2_ADDRESS, UNISWAP_ROUTER_V2_ADDRESS).call()
print("account_2 have gave router {} XA1C ".format(XA1C_allowance / DECIMAL))

# first we need to add account_2 account to default account of web3

account_2 = w3.eth.account.from_key(ACCOUNT_2_PRIVATE_KEY)
w3.eth.default_account = account_2.address

# approve to router spend 1 XA1C

if XA1C_allowance < amount_XA1C_in:
    amount_allowance = amount_XA1C_in - XA1C_allowance
    transaction = XA1C.functions.approve(router_contract.address, amount_allowance).buildTransaction()
    transaction.update({ 'nonce' : w3.eth.get_transaction_count(ACCOUNT_2_ADDRESS) })
    signed_tx = w3.eth.account.sign_transaction(transaction, ACCOUNT_2_PRIVATE_KEY)
    txn_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    txn_receipt = w3.eth.wait_for_transaction_receipt(txn_hash)
    print(json.dumps(txn_receipt, indent=4, sort_keys=True, cls=BlockchainDataJsonEncoder))
    
# check ACCOUNT 2 give allowance router how many XA1C again

XA1C_allowance = XA1C.functions.allowance(ACCOUNT_2_ADDRESS, UNISWAP_ROUTER_V2_ADDRESS).call()
print("account_2 have gave router {} XA1C ".format(XA1C_allowance / DECIMAL))

# get pair of XA1C and XA2C

factory_built_file = open('../node_modules/@uniswap/v2-core/build/UniswapV2Factory.json', "r")
factory_built_content = json.load(factory_built_file)
factory_abi = factory_built_content["abi"]
factory = w3.eth.contract(address=UNISWAP_FACTORY_ADDRESS, abi=factory_abi)
pair_address = factory.functions.getPair(XA1C_ADDRESS, XA2C_ADDRESS).call()
print("pair address: ", pair_address)

# get reverses from pair

pair_built_file = open('../node_modules/@uniswap/v2-core/build/UniswapV2Pair.json', "r")
pair_built_content = json.load(pair_built_file)
pair_abi = pair_built_content["abi"]
pair = w3.eth.contract(address=pair_address, abi=pair_abi)
reverses = pair.functions.getReserves().call()
# print("reverses: ", reverses)

# get amount out of XA2C when swap 1 XA1C

if XA1C_ADDRESS < XA2C_ADDRESS:
    reverse_XA1C = reverses[0]
    reverse_XA2C = reverses[1]
else:
    reverse_XA1C = reverses[1]
    reverse_XA2C = reverses[0]
    
amount_out = router_contract.functions.getAmountOut(1 * DECIMAL, reverse_XA1C, reverse_XA2C).call()
print('reverse XA1C: ', reverse_XA1C / DECIMAL)
print('reverse XA2C: ', reverse_XA2C / DECIMAL)
print("1 XA1C can swap amount XA2C: ", amount_out / DECIMAL)

amounts_out = router_contract.functions.getAmountsOut(1 * DECIMAL, [XA1C_ADDRESS, XA2C_ADDRESS]).call()
print(amounts_out)
# print("1 XA1C can swap amount XA2C: ", amount_out / DECIMAL)
    
# get current balance of account 2

old_XA1C_balance = XA1C.functions.balanceOf(ACCOUNT_2_ADDRESS).call() / DECIMAL
old_XA2C_balance = XA2C.functions.balanceOf(ACCOUNT_2_ADDRESS).call() / DECIMAL

# swap exact 1 XA1C for XA2C
# to = ACCOUNT_2_ADDRESS
# to = ACCOUNT_3_ADDRESS
to = "0x5736664454591251E3204e932408a4A52283E247"
swap_exact_ETH_for_tokens_trans = router_contract.functions.swapExactTokensForTokens(
    amount_XA1C_in,
    amount_XA2C_out_min,
    [XA1C_ADDRESS, XA2C_ADDRESS],
    to,
    DEADLINE
).buildTransaction({
    'from': ACCOUNT_2_ADDRESS,   # You are not specifying the from, so the default account is used. 
                                # Make sure that's what you want and that the account has enough funds and that its private key is the one you are using to sign.
    # 'value': amount_ETH_for_swap_exact_DAI,  # NOTE: missing this, it's will raise error: UniswapV2Library: INSUFFICIENT_AMOUNT
    # 'gasPrice': w3.toWei('100', 'gwei'), 
    'gasPrice': w3.eth.gas_price
    # 'to': '0x6Bc272FCFcf89C14cebFC57B8f1543F5137F97dE',
    # 'data': '0x7cf5dab00000000000000000000000000000000000000000000000000000000000000005',
    # 'gas': 43242,
    # 'maxFeePerGas': 2000000000,
    # 'maxPriorityFeePerGas': 1000000000,
    # 'chainId': 1  # network_id
    #  'maxFeePerGas': w3.toWei('2', 'gwei'),
    #  'maxPriorityFeePerGas': w3.toWei('1', 'gwei'),
})
swap_exact_ETH_for_tokens_trans.update({ 'nonce' : w3.eth.get_transaction_count(ACCOUNT_2_ADDRESS) })
signed_tx = w3.eth.account.sign_transaction(swap_exact_ETH_for_tokens_trans, ACCOUNT_2_PRIVATE_KEY)
txn_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
txn_receipt = w3.eth.wait_for_transaction_receipt(txn_hash)
print(json.dumps(txn_receipt, indent=4, sort_keys=True, cls=BlockchainDataJsonEncoder))

print("1 XA1C can swap amount XA2C: ", amount_out / DECIMAL)
print('old balance XA1C of account 2: ', old_XA1C_balance)
print('old balance XA2C of account 2: ', old_XA2C_balance)
print('new balance XA1C of account 2: ', XA1C.functions.balanceOf(ACCOUNT_2_ADDRESS).call() / DECIMAL)
print('new balance XA2C of account 2: ', XA2C.functions.balanceOf(ACCOUNT_2_ADDRESS).call() / DECIMAL)
print('new balance XA1C of account 3: ', XA1C.functions.balanceOf(ACCOUNT_3_ADDRESS).call() / DECIMAL)
print('new balance XA2C of account 3: ', XA2C.functions.balanceOf(ACCOUNT_3_ADDRESS).call() / DECIMAL)
