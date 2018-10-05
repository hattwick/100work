# Goofing around with Michael's "Build 10 Apps" tutorial at TalkPython Training

# This is a mix of several use cases of the random function


import random


# first pass just select a random element from a string.
letters = "abcdefghjiklmnopqrstuvwxyz1234567890"
item = random.choice(letters)
print("Found random item: " + item)
item = random.choice(letters)  #do it again
print("Found random item: {0}".format(item))


