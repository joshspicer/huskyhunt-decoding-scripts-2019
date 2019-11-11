import random
import sys


def insert_backslash_u(word):
    new_word = ""
    for (i, c) in enumerate(word):
        if i % 4 == 0:
            new_word += "\\u"
        new_word += c
    return new_word

out = open("output_unicode.txt", "w")

with open(sys.argv[1]) as f:
    # For each clue of the file.
    for idx, line in enumerate(f):
        # Split by space
        words = line.split()
        # For every word add a u in the front...
        # And for every 4 characters add a \u
        uwords = [insert_backslash_u(word)  for word in words]
        #out.write(" ".join(uwords))
        print('u'+" ".join(uwords))

