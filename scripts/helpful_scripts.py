from brownie import network, config, accounts, MockV3Aggregator
from web3 import Web3

# Variables to deploy the MockV3Aggregator
DECIMALS = 8
STARTING_PRICE = 200000000000

# To distinguish between ethereum chains and our local ganache chain (dev)
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]

def get_account():
    if (network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

def deploy_mocks():
        print(f"The active network is {network.show_active()}")
        print("Deploying Mocks...")

        # Deploy MockV3Aggregator only if there are no existing ones
        if len(MockV3Aggregator) <= 0:
            MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": get_account()})
        
        print("Mocks Deployed!")