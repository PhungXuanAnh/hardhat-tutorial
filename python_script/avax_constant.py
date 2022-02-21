import json
from web3 import Web3
RPC_URL = 'https://api.avax-test.network/ext/bc/C/rpc'
w3 = Web3(Web3.HTTPProvider(RPC_URL))
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

PANGOLIN_FACTORY_ADDRESS = "0xE4A575550C2b460d2307b82dCd7aFe84AD1484dd"
PANGOLIN_ROUTER_V2_ADDRESS = "0x2D99ABD9008Dc933ff5c0CD271B88309593aB921"

XA1C_ADDRESS = "0x5bF8cd4411849385d6245CAF2a10095a86aC93C9"
XA2C_ADDRESS = "0x51dCC77071A2996EF73c50997C80003a3D2c1cC8"
LIFE_ADDRESS = "0x19984415D191514fC50aE7dc44fbd885EABb00AF"

OPERATOR_ADDRESS = "0xFFa2a2845924326045538DA9a72C40614001C561"
OPERATOR_PRIVATE_KEY = "5dc0c12f82b98c275040b5c3526514603f0df98b9ef27317cb5e51807c1fd79c"
ACCOUNT_2_ADDRESS = "0x3A2db9C94F98F9c97607A38CFC6fe08e13b8F883"
ACCOUNT_2_PRIVATE_KEY = "a3285aa134985833dfa82dc6cedf32f36c5c271c0fe3665849fe32435acaf111"

amount_XA1C_desired = 50 * 10**2
amount_XA1C_min = 30 * 10 ** 2
amount_XA2C_desired = 25 * 10**2
amount_XA2C_min = 15 * 10 ** 2
DEADLINE = 2000000000


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