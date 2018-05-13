# 100days - week 1

from datetime import datetime
from datetime import timedelta

t = timedelta(days =4, hours = 10)
hours = t.seconds / 3600

print("Executing at current time", datetime.today())
print("\n During of delta is:\n)")
print("days", t.days)
print("hours", hours)
print("\nEstimate ending:", datetime.today() + t)