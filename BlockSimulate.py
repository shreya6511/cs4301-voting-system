from hashlib import sha256
import json
import time

"""
This code contains a skeleton for a single node Blockchain, for the purpose of simulating how a blockchain system works. 
Important utility functions are provided. Your task is to use them to complete this skeleton for the Blockchain class.
"""

"""
Do NOT delete comments from this file.
"""


class Block:
    def __init__(self, index, transactions, timestamp, previous_hash):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = 0

    def compute_hash(self):
        """
        A function that return the hash of the block contents.
        """
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return sha256(block_string.encode()).hexdigest()


class Blockchain:
    # difficulty of Proof of Work. This is the number of zeros that the hash of the block must begin with
    difficulty = 2

    def __init__(self):
        self.unconfirmed_transactions = []
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        """
        Create the gensis block, and append it to the chain.
        The block has index 0, previous_hash as 0, and
        a valid hash.
        """
        if len(self.chain) == 0:
            genesis_block = Block(0, [], time.time(), "0")
            self.chain.append(genesis_block)

    @property
    def last_block(self):
        return self.chain[-1]

    def add_block(self, block, proof):
        """
        Verify that a given block is valid:
        a) Checking if the proof is valid.
        b) The previous_hash referred in the block and the hash of latest block
          in the chain match.
        If so, add it to the blockchain.
        """
        if not self.is_valid_proof(block, proof):
            return False

        prev_hash = self.last_block.compute_hash()
        if prev_hash != block.previous_hash:
            return False

        self.chain.append(block)
        return True

    def is_valid_proof(self, block, block_hash):
        """
        Check if block_hash is valid hash of block and satisfies
        the difficulty criteria.
        """
        return (
            block_hash.startswith("0" * self.difficulty)
            and block_hash == block.compute_hash()
        )

    def proof_of_work(self, block):
        """
        Implement the basic proof of work.
        Specifically, update the nonce value from its default of 0
        until the hash of the block begins with the defined number of 0s,
        """
        block.nonce = 0
        computed_hash = block.compute_hash()
        while not computed_hash.startswith("0" * self.difficulty):
            block.nonce += 1
            computed_hash = block.compute_hash()
        return computed_hash

    def add_new_transaction(self, transaction):
        self.unconfirmed_transactions.append(transaction)

    def mine(self):
        """
        This function serves as an interface to add the pending
        transactions to the blockchain by adding them to the block
        and figuring out Proof Of Work.
        """
        if not self.unconfirmed_transactions:
            return False

        last_block = self.last_block

        new_block = Block(
            index=last_block.index + 1,
            transactions=self.unconfirmed_transactions,
            timestamp=time.time(),
            previous_hash=last_block.compute_hash(),
        )

        proof = self.proof_of_work(new_block)
        self.add_block(new_block, proof)

        self.unconfirmed_transactions = []
        return new_block.index


if __name__ == "__main__":
    """
    This is where you instantiate the Blockchain class and demonstrate how it all comes together.
    Do the following
    - Create an instance of a Blockchain
    - Ensure the genesis block is created for the blockchain, and display this.
    - "Mine": Run the mine function to see if your proof of work implementation is working as expected
    - Show the final blockchain after "mining" once.
    """
    blockchain = Blockchain()

    # print block chain to show creation of genesis block using transactions as an identifier
    print("Blockchain after instantiation (only genesis) ", end="")
    for link in blockchain.chain:
        print(link.transactions)

    # add five new transactions
    blockchain.add_new_transaction("$500")
    blockchain.add_new_transaction("-$200")
    blockchain.add_new_transaction("+$1500")
    blockchain.add_new_transaction("-$100")
    blockchain.add_new_transaction("$2500")

    # mine block (irl every 10 minutes on average)
    blockchain.mine()

    # print contents of chain using transactions as a indicator of idenity
    print("Blockchain after mining ", end="")
    for link in blockchain.chain:
        print(link.transactions, end="")
