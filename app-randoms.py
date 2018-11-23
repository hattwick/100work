# This is a mix of several use cases of the random function
# Tested in Python 3.7

import random
import sys

version = sys.version
print(version)


# first pass just select a random element from a string.
letters = "abcdefghjiklmnopqrstuvwxyz1234567890"
item = random.choice(letters)
print("Found random item: " + item)
item = random.choice(letters)  #do it again
print("Found random item: {0}".format(item))