import sys
import hashlib
import string
import random

x=0

def RSG():
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(6, 100))

sump = 0
def find_preimage(target,n):
    i=0
    while True:
        stringToHash = RSG()
        generated_hash = hashlib.sha256(stringToHash.encode())
        i+=1
        if generated_hash.digest()[0:n] == target[0:n]:
            print str(i) + ' p ' + str(x)
            # print stringToHash
            return i

plaintext = {}
hashes = set()

sumc = 0          
def find_collision(n):
    hashcounter = 0
    j=0
    while True:
        generated_string = RSG()
        generated_hash = hashlib.sha256(generated_string.encode()).digest()[:n]
        hashcounter += 1
        j+=1
        if generated_hash in hashes:
            print str(j) + ' c ' + str(x)

            return j
        else:             
            hashes.add(generated_hash)
            plaintext[generated_hash] = generated_string

while True:
    sump+=find_preimage('abcdef',2)
    sumc+=find_collision(2)
    x+=1
    if x==15:
        print str(sump/15) + 'avgp'
        print str(sumc/15) + 'avgc'
        break
