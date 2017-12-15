import block
from pymongo import MongoClient

class Blockchain:
    def __init__(self):
        self.db = MongoClient().q


    def write_block(self, block):
        block_to_add = {
            'index': block.index,
            'timestamp': block.timestamp,
            'data': block.data,
            'previous_hash': block.previous_hash,
            'hash': block.hash
        }

        result = self.db.chain.insert_one(block_to_add)
        print(result)

    def block_at_index(self, index):
        result = self.db.chain.find_one({ 'index': index })
        if result:
            b = block.Block(result['index'], result['timestamp'], result['data'], result['previous_hash'])
            b.hash = result['hash']
            return b
        else:
            return None
