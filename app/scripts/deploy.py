from brownie import SolidityStorage, VyperStorage, accounts, network, Wei


def main():
    # En mi caso, HackAccount tiene fondos en la testnet
    owner = accounts.load('HackAccount')        

    # requires brownie account to have been created
    if network.show_active()=='development':
        # add these accounts to metamask by importing private key
        accounts[0].transfer(owner.address, Wei('10 ether'))

        SolidityStorage.deploy({'from':owner})
        VyperStorage.deploy({'from':owner})

    elif network.show_active() == 'kovan':
        # add these accounts to metamask by importing private key
        SolidityStorage.deploy({'from':owner})
        VyperStorage.deploy({'from':owner})