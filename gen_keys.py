from web3 import Web3
import eth_account 
from eth_account import Account 
from eth_account.messages import encode_defunct
import os

def get_keys(challenge,keyId = 0, filename = "eth_mnemonic.txt"):
    """
    Generate a stable private key
    challenge - byte string
    keyId (integer) - which key to use
    filename - filename to read and store mnemonics

    Each mnemonic is stored on a separate line
    If fewer than (keyId+1) mnemonics have been generated, generate a new one and return that
    """

    w3 = Web3()
    private_key = "d4beb38bd527d38cb8f742a4bb7ab94eb8bcdd7d702f3c7f03a134d2781038e1"
    eth_addr = "0xd7b33084078F1269e21734bA4E73b7f085414194"

    msg = eth_account.messages.encode_defunct(challenge)
    account = Account.from_key(private_key)
    sig = account.sign_message(msg)



	#YOUR CODE HERE

    assert eth_account.Account.recover_message(msg,signature=sig.signature.hex()) == eth_addr, f"Failed to sign message properly"

    #return sig, acct #acct contains the private key
    return sig, eth_addr

if __name__ == "__main__":
    for i in range(4):
        challenge = os.urandom(64)
        sig, addr= get_keys(challenge=challenge,keyId=i)
        print( addr )
