import sys
import hashlib
import string
import random

def RSG():
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(6, 100))

def find_preimage(target,n):
   
    while True:
        stringToHash = RSG()
        generated_hash = hashlib.sha256(stringToHash.encode())
        
        if generated_hash.digest()[0:n] == target[0:n]:
            return stringToHash
