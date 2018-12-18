# Goofing around with Michael's "Build 10 Apps" tutorial at TalkPython Training

import sys
import datetime
from datetime import date

version = sys.version
print(version)


def program_header():
    print("----------------------------------")
    print("       DAYS UNTIL APP             ")
    print("----------------------------------")


def get_special_day_from_user():
    print("What is the day you are tracking toward?")
    year = int(input("Year [YYYY] "))
    month = int(input("Month [MM] "))
    day = int(input("Day [DD] "))
    targetday = datetime.date(year, month, day)
    print(targetday)
    return targetday


def compute_days_between_dates(original_date, target_date):
    dt = original_date - target_date
    # print('days' + dt)
    return dt.days


def findings():
    pass


if __name__ == "__main__":
    # execute only if run as a script
    program_header()
    day = get_special_day_from_user()
    now = date.today()  # TODO fix zero value being passed
    print(f"Today is {0}".format(now))
    number_of_days = compute_days_between_dates(day, now)
    print(f"Number of days: ".format(number_of_days))
    # findings(number_of_days)
