# -*- coding: utf-8 -*-
"""
Created on Tue Jul 15 20:59:50 2025

@author: JdeDios4
"""

import hashlib
import json
from time import time
from flask import Flask, jsonify, request

class Blockchain:
    def __init__(self):
        self.chain = []
        self.transactions = []
        self.create_block(proof=1,previous_hash='0')
        
    def create_block(self,proof,previous_hash):
        block = {
            'index':len(self.chain)+1,
            'timestamp':time(),
            'transactions':self.transactions,
            'proof':proof,
            'previous_hash':previous_hash
            }
        self.transactions = []
        self.chain.append(block)
        return block
    def get_previous_block(self):
        return self.chain[-1]
    def proof_of_work(self,previous_proof):
        new_proof = 1
        while True:
            hash_value = hashlib.sha256(str(new_proof**2-previous_proof**2).encode()).hexdigest()
            if hash_value[:4] == '0000':
                return new_proof
            new_proof += 1
    def hash(self,block):
        encoded = json.dumps(block, sort_keys = True).encode()
        return hashlib.sha256(encoded).hexdigest()
    
    def is_chain_valid(self,chain):
        for i in range(1,len(chain)):
            prev = chain[i-1]
            curr = chain[i]
            if curr ['previous_hash'] != self.hash(prev):
                return False
            if not self.proof_of_work(prev['proof']) == curr['proof']:
                return False
        return True
    
    def add_transaction(self, sender, receiver, amount):
        self.transactions.append({
            'sender':sender,
            'receiver':receiver,
            'amount':amount
            })
        return self.get_previous_block()['index']+1
    
#create app

app = Flask(__name__)
blockchain = Blockchain()

@app.route('/mine',methods=['GET'])
def mine():
    previous_block = blockchain.get_previous_block()
    proof = blockchain.proof_of_work(previous_block['proof'])
    blockchain.add_transaction(sender = "network", receiver = "you", amount = 1)
    previous_hash = blockchain.hash(previous_block)
    block = blockchain.create_block(proof, previous_hash)
    return jsonify({'message':'New Block Mined!','block':block}),200
@app.route('/chain',methods=['GET'])
def full_chain():
    return jsonify({'chain':blockchain.chain,'length':len(blockchain.chain)}),200
@app.route('/transaction',methods=['POST'])
def new_transaction():
    data = request.get_json()
    required = ['sender','receiver','amount']
    if not all(k in data for k in required):
        return 'Missing values',400
    index = blockchain.add_transaction(data['sender'], data['receiver'], data['amount'])
    return jsonify({'message':f'Transaction will be added to block {index}'}),201
if __name__=='__main__':
    app.run(port=5000)




    
    
        