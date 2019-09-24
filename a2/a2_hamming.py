import sys

def hammingdistance(s1, s2):
    # convert system arguments into base 16 hexadecimals
    s1 = int(s1, 16)
    s2 = int(s2, 16)
    
    # convert to binary string, XOR the 2 hex values and count 1's to determine hamming distance
    distance = bin(s1 ^ s2).count('1')
    return distance

