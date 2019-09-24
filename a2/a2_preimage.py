import sys
import hashlib
import string

def find_preimage(target, n):
    i = 0
    generated_hash = hashlib.sha256(target.encode())
    while generated_hash.hexdigest()[:n] != target[:n]:
        i += 1
        stringToHash = target + str(n)
        generated_hash = hashlib.sha256(stringToHash.encode())
        if generated_hash.hexdigest()[:n] == target[:n]:
		return stringToHash
