import sys
import hashlib
import string
import random

def randomStringGenerator():
    def randomNumGenerator():
        return random.randrange(1, 100)

    return ''.join(random.choice(string.ascii_lowercase) for _ in range(randomNumGenerator()))

def find_preimage(target,n):
   
    while True:
        stringToHash = randomStringGenerator()
        generated_hash = hashlib.sha256(stringToHash.encode())
        
        if generated_hash.digest()[0:n] == target[0:n]:
            return stringToHash
   

