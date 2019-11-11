import random
import sys

alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 'zyxwvutsrqponmlkjihgfedcba'


def decrypt(cipher, key, alphabet):
    keyMap = dict(zip(key, alphabet))
    return ''.join(keyMap.get(c.lower(), c) for c in cipher)


out = open("output.txt", "w")

with open(sys.argv[1]) as f:
    for idx, line in enumerate(f):
        out.write(decrypt(line, key, alphabet))
        print(decrypt(line, key, alphabet))
