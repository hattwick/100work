# Python Workouts with Reuven
# Exercises 1.2.1 - Random Integer Guess

import random
import locale

systemencoder = locale.getpreferredencoding(False)

answer = random.randint(0, 100)

while True:
    user_guess = int(input("What is your guess? "))  # out of bounds value is a fatal error
    print(f"Test value = {answer}")

    if user_guess == answer:
        print(f"Correct! The answer is {user_guess}")
        print(f"System encoder was {systemencoder}")
        break

    else:
        print(f"Sorry. The answer was {answer}")
        print("Try again.")

#todo move to try/except and also handle error use case