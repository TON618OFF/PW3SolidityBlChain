from web3 import Web3
from web3.middleware import geth_poa_middleware
from contract_info import abi, contract_address

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

contract = w3.eth.contract(address=contract_address, abi=abi)

print(contract_address)
print(f"Баланс смарт-контракта: {w3.eth.get_balance(contract_address)}")
print(f"Баланс первого аккаунта: {w3.eth.get_balance('0x640Ba9133DD9B9364DE91Fbf146fE4b1Da93468e')}")
print(f"Баланс второго аккаунта: {w3.eth.get_balance('0x1dfda777dE3c69097A3A81f7563c91f5fcc14c19')}")
print(f"Баланс третьего аккаунта: {w3.eth.get_balance('0x33EDa0Bcff267662fB87F4818223F2bc03A29065')}")
print(f"Баланс четвёртого аккаунта: {w3.eth.get_balance('0xbe665932E164EB9a68F0F20Fae5f12208f41A8B5')}")
print(f"Баланс пятого аккаунта: {w3.eth.get_balance('0x2bfF989F3A7b64aD374032b29F9fc5a368EcF515')}")