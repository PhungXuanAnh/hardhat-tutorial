import json
from web3 import Web3
INFURA_URL = 'https://rinkeby.infura.io/v3/209b0f36b12b4e50951ce0f0d5b241e3'
w3 = Web3(Web3.HTTPProvider(INFURA_URL))
print('is connected: {}'.format(w3.isConnected()))

# fix error when running with rinkeby.infura network: 
#   web3.exceptions.ExtraDataLengthError: The field extraData is 97 bytes, but should be 32. It is quite likely that you are connected to a POA chain.
# reference: 
# https://github.com/blockchain-etl/ethereum-etl/issues/178#issuecomment-613488883
# https://stackoverflow.com/a/69981086/7639845
# https://web3py.readthedocs.io/en/stable/middleware.html#geth-style-proof-of-authority
from web3.middleware import geth_poa_middleware
w3.middleware_onion.inject(geth_poa_middleware, layer=0)
# print(w3.clientVersion)


UNISWAP_FACTORY_ADDRESS = "0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f"
UNISWAP_ROUTER_V2_ADDRESS = "0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D"


C1_ADDRESS = "0x02380CF743A453B279190eE4Ec0EBa376e69d0E4"
C2_ADDRESS = "0xc725f6243562C445b0352fc9Db99Ec17EB0Ad393"
XA1C_ADDRESS = C1_ADDRESS
XA2C_ADDRESS = C2_ADDRESS
DECIMAL = 10**18
# for add liquidity
amount_XA1C_desired = 60 * DECIMAL
amount_XA1C_min = 40 * DECIMAL
amount_XA2C_desired = 30 * DECIMAL
amount_XA2C_min = 20 * DECIMAL
DEADLINE = 2000000000
# for swap
amount_XA1C_in = 1 * DECIMAL  # 1 XA1C
amount_XA2C_out_min = int(0.1 * DECIMAL) # 0.1 XA2C

abi = json.load(open('rinkeby_abi.json', 'r'))


# XA1C_ADDRESS = "0x202A8cCB480b458520c03462f922CC0Ee7ab342A"
# XA2C_ADDRESS = "0x32D94D19E90F807cDcD0978f56690BCd141046bF"
# DECIMAL = 10**18
# amount_XA1C_desired = 50 * DECIMAL
# amount_XA1C_min = 30 * DECIMAL
# amount_XA2C_desired = 25 * DECIMAL
# amount_XA2C_min = 15 * DECIMAL
# DEADLINE = 2000000000


OPERATOR_ADDRESS = "0xFFa2a2845924326045538DA9a72C40614001C561"
OPERATOR_PRIVATE_KEY = "5dc0c12f82b98c275040b5c3526514603f0df98b9ef27317cb5e51807c1fd79c"
ACCOUNT_2_ADDRESS = "0x3A2db9C94F98F9c97607A38CFC6fe08e13b8F883"
ACCOUNT_2_PRIVATE_KEY = "a3285aa134985833dfa82dc6cedf32f36c5c271c0fe3665849fe32435acaf111"
ACCOUNT_3_ADDRESS = "0x095D56941dE7e086bD127BA7a2D6BFadF64D4370"

from web3.datastructures import AttributeDict
from hexbytes import HexBytes
class BlockchainDataJsonEncoder(json.JSONEncoder):
    """
        from web3._utils.events import get_event_data
        from web3.datastructures import AttributeDict
        from web3.types import EventData
    """
    def default(self, obj):
        if isinstance(obj, AttributeDict):
            return obj.__dict__
        if isinstance(obj, HexBytes):
            return obj.hex()
        return super().default(obj) 