import hashlib
import string
from string import *
import random

plaintext = {}
hashes = set()

def RSG():
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(6, 100))

def find_collision(n):
    while True:
        generated_string = RSG()
        generated_hash = hashlib.sha256(generated_string.encode()).digest()[:n]

        if generated_hash in hashes:
            return plaintext[generated_hash],generated_string
        else:             
            hashes.add(generated_hash)
            plaintext[generated_hash] = generated_string
