# Robbie posed a question.
# A network guy is just one of the many things he is.
# The question:  Given a string aaacchhhc, write a function to return 3a2c2h1c

import sys
import collections

version = sys.version
print(version)


def main():
    program_header()
    get_and_transform()


def program_header():
    print("--------------------------------------------")
    print("           ROBBIE's CODE MUNGER             ")
    print("--------------------------------------------")
    print()




def get_and_transform():
    """
    Get a value (e.g. aabbbbccdaaa) and return a shorthand(?)
    version (e.g. 2a4b2c1d3a).
    :return: is optional

    TODO: error handling, loop capability
    """

    codedictionary = {}  #initialize dictionary of letters and count
    robbieinput = input("Enter your string? ")
    print(f"Original string: {robbieinput}")

    for item in robbieinput:
        tempval = item
        counter = 1
        print (f"{tempval}, {counter} ")




if __name__ == "__main__":
    main()
