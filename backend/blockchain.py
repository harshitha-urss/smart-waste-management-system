# backend/blockchain.py
import hashlib, json, time
from typing import List

class SimpleChain:
    def __init__(self):
        self.chain = []
        self._create_genesis()

    def _create_genesis(self):
        genesis = {
            "index": 0,
            "timestamp": time.time(),
            "data": "genesis",
            "prev_hash": "0",
        }
        genesis["hash"] = self._hash_block(genesis)
        self.chain.append(genesis)

    def _hash_block(self, block: dict) -> str:
        # deterministic representation
        block_string = json.dumps(block, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()

    def add_block(self, data: dict) -> dict:
        prev = self.chain[-1]
        block = {
            "index": prev["index"] + 1,
            "timestamp": time.time(),
            "data": data,
            "prev_hash": prev["hash"]
        }
        block["hash"] = self._hash_block(block)
        self.chain.append(block)
        return block

    def latest(self):
        return self.chain[-1]

    def to_list(self) -> List[dict]:
        return self.chain

# module-level singleton
_chain = SimpleChain()

def get_chain():
    return _chain
