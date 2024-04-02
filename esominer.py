from flask import Flask, jsonify 
from blockchain import Blockchain

"""
CREATED BY EDSON OLIVEIRA 
EMAIL: EDSONGRDEVELOPER@GMAIL.COM
"""

app = Flask(__name__)

blockChain = Blockchain()

@app.route('/miner', methods = ['GET'])
def miner():
    previousBlock = blockChain.getPreviousBlock()
    previousProof = previousBlock['proof']
    
    proof = blockChain.proofOfWork(previousProof)
    previousHash = blockChain.hash(previousBlock)

    newBlock = blockChain.createBlock(proof, previousHash)

    response = {
                    'message': 'Congratulations, you found a block!',
                    'index': newBlock['index'],
                    'timestamp': newBlock['timestamp'],
                    'proof': newBlock['proof'],
                    'previousHash': newBlock['previousHash']
                }
    
    return jsonify(response), 200

@app.route('/get-chain', methods = ['GET'])
def getChain():
    response = {
                    'chain': blockChain.chain, 
                    'length': len(blockChain.chain)
                }

    return jsonify(response), 200

@app.route('/is-valid', methods = ['GET'])
def isValid():
    isValidBlock = blockChain.isChainValid(blockChain.chain)

    if isValidBlock:
        response = {'message': 'Successfully validated'}
    else: 
        response = {'message': 'It is not valid'}

    return jsonify(response), 200


app.run(host='0.0.0.0', port = 5000)
