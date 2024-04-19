from hashlib import sha256
import json
import time


# Adapted from CS 4301 Programming Assignment 1
class Block:
    def __init__(self, index, transactions, timestamp, previous_hash):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = 0

    def compute_hash(self):
        """
        A function that returns the hash of the block contents.
        """
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return sha256(block_string.encode()).hexdigest()


class Blockchain:
    # Difficulty of Proof of Work. This is the number of zeros that the hash of the block must begin with.
    difficulty = 2

    def __init__(self):
        self.unconfirmed_transactions = []
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        """
        Create the genesis block and append it to the chain.
        The block has index 0, previous_hash as 0, and a valid hash.
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
        b) The previous_hash referred in the block and the hash of the latest block
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
        Check if block_hash is a valid hash of the block and satisfies
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
        until the hash of the block begins with the defined number of 0s.
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
    print("Executed")
