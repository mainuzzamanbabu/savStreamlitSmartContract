from web3 import Web3
from solcx import compile_source

# Solidity source code
with open("sav.sol", "r") as f:
    contract_source_code = f.read()
# Compile the contract
compiled_sol = compile_source(contract_source_code, output_values=["abi", "bin"])

# Retrieve the contract interface
contract_id, contract_interface = compiled_sol.popitem()

# Get bytecode / bin
bytecode = contract_interface["bin"]

# Get ABI
abi = contract_interface["abi"]

# Web3.py instance
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

# Set pre-funded account as sender
w3.eth.default_account = w3.eth.accounts[0]

student_management = w3.eth.contract(abi=abi, bytecode=bytecode)

tx_hash = student_management.constructor().transact()
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
# Instantiate the contract at the deployed address
student_management = w3.eth.contract(
    address=tx_receipt.contractAddress,
    abi=abi
)

# Interact with the contract using its functions
def add_achievement (descriotion, addr):
    student_management.functions.addAchievement(descriotion, addr).transact()

account = w3.eth.account.create()
# registerwallet('')
# Print the new wallet address and private key
print('New wallet address:', account.address)
print('Private key:', account.privateKey.hex())

# add_achievement('Python Workshop', account.address)

def view_function(addr):
    student = student_management.functions.getAchievements(addr).call()
    return student

# def registerwallet():
#     student = student_management.functions.registerWallet().transact()

# print(view_function(account.address))


# print(registerwallet())
