# Goofing around with Michael's "Build 10 Apps" tutorial at TalkPython Training

import sys
import datetime

version = sys.version
print(version)


def program_header():
    print("----------------------------------")
    print("       DAYS UNTIL APP             ")
    print("----------------------------------")


def get_special_day_from_user():
    print("What is the day you are tracking toward?")
    year = input("Year [YYYY}")
    month = input("Month [MM}")
    day = input("Day [DD}")
    targetday = datetime.date
    print(f"Target date locked in as".format(targetday))


def compute_days_between_dates():
    pass


def findings():
    pass


def main():
    program_header()
    day = get_special_day_from_user()
    now = None
    number_of_days = compute_days_between_dates(day, now)
    findings(number_of_days)
