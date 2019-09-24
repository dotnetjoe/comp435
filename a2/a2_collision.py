import hashlib
import string
from string import *
import random

plaintext = {}
hashes = set()

def RSG():
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(6, 100))

def collision():
    hashcounter = 0
    while True:
        generated_string = RSG()
        generated_hash = hashlib.sha256(generated_string.encode()).hexdigest()[:6]
        hashcounter += 1
        if generated_hash in hashes:
            print(plaintext[generated_hash] + " " + generated_string)
            print(hashcounter)
            return False
        else:
            hashes.add(generated_hash)
            plaintext[generated_hash] = generated_string
