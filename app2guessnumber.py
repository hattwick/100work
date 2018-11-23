# Goofing around with Michael's "Build 10 Apps" tutorial at TalkPython Training

# This is App 2 from that course
# Program is a number guessing function to test loops, conditions, type conversion, truthiness
# Tested in Python 3.7

import random
import sys

version = sys.version
print(version)

print('--------------------------------------------')
print('           GUESS THE NUMBER GAME            ')
print('           Python Version:                  ')
print('--------------------------------------------')
print()

the_number = random.randint(0, 100)  # type: object
guess = -1  # Need to initialize the guess outside of the range.



while guess != the_number:
	guess_text = input('What is the correct number (between 0 and 100, inclusive)? ')
	guess = int(guess_text)  # converting the string input to integer
	if guess < the_number:
		print(f'Your guess {0} is too low.'.format(guess))
	elif guess > the_number:
		print('Your guess is high.')
	else:
		print('You guessed the correct number!!!')

print('Thank you for guessing.')
