import hashlib
import json
import datetime

"""
CREATED BY EDSON OLIVEIRA 
EMAIL: EDSONGRDEVELOPER@GMAIL.COM
"""
class Blockchain:

    def __init__(self) -> None:
        self.chain = []
        
        # Create Genesis Block
        self.createBlock(1, '0')

    def createBlock(self, proof:int, previousHash:str) -> dict:
        # Block structure
        block = {
                    'index': len(self.chain) + 1,
                    'timestamp': str(datetime.datetime.now()),
                    'proof': proof,
                    'previousHash': previousHash
                }
        
        # add this block in the chain list
        self.chain.append(block)
        return block
    
    def getPreviousBlock(self) -> dict:
        return self.chain[-1]
    
    def proofOfWork(self, previosProof: int) -> int:
        newProof = 1
        found = False

        while found is False: 
            hashOperation = hashlib.sha256(str(newProof**2 - previosProof**2).encode()).hexdigest()

            if hashOperation[:4] == '0000':
                found = True
            else: 
                newProof +=1

        return newProof
    
    def hash(self, block: dict) -> str: 
        encodedBlock = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encodedBlock).hexdigest()
    
    def isChainValid(self, chain: dict): 
        previousBlock = chain[0]
        blockIndex = 1

        while blockIndex < len(chain):
            block = chain[blockIndex]

            if block['previousHash'] != self.hash(previousBlock):
                return False
            
            previousProof = previousBlock['proof']
            proof = block['proof']
            hashOperation = hashlib.sha256(str(proof**2 - previousProof**2).encode()).hexdigest()

            if hashOperation[:4] != '0000':
                return False 
            
            previousBlock = block
            blockIndex += 1
        
        return True
    