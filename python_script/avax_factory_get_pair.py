import json
from avax_constant import PANGOLIN_FACTORY_ADDRESS, XA1C_ADDRESS, XA2C_ADDRESS, w3, LIFE_ADDRESS

avax_abi = open('avax_abi.json', "r")
avax_abi = json.load(avax_abi)
factory_abi = avax_abi["factory"]
factory = w3.eth.contract(address=PANGOLIN_FACTORY_ADDRESS, abi=factory_abi)
pair_address = factory.functions.getPair(LIFE_ADDRESS, XA1C_ADDRESS).call()
print(pair_address)

avax_abi = open('avax_abi.json', "r")
avax_abi = json.load(avax_abi)
pair_abi = avax_abi["pair"]
pair = w3.eth.contract(address=pair_address, abi=pair_abi)
reverses = pair.functions.getReserves().call()
print("reverses: ", reverses)