"""
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

#use datetime module

import datetime
import calendar
count = 0

for year in range(1901, 2001):
    x = calendar.Calendar()
    list_of_dates = x.yeardays2calendar(year)
    # the list is heavily nested (by week and month) so flatten it 
    flattened1 = [val for sublist in list_of_dates for val in sublist]
    flattened2 = [val for sublist in flattened1 for val in sublist]
    flattened3 = [val for sublist in flattened2 for val in sublist]
    for date in flattened3:
        if date == (1, 6): # first day of month (1) is Sunday (6)
            count += 1
            
print count

# calendar module takes care of leap years
# the answer this gave was 171, which is correct