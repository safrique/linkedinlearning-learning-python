#
# Example file for working with Calendars
#

# import the calendar module
import calendar
from datetime import date

# create a plain text calendar
d = date.today()
c = calendar.TextCalendar(calendar.SUNDAY)
# st = c.formatmonth(d.year, d.month, 0, 0)
# print(st)

# create an HTML formatted calendar
# hc = calendar.HTMLCalendar(calendar.SUNDAY)
# st = hc.formatmonth(d.year, d.month)
# print(st)

# loop over the days of a month
# zeroes mean that the day of the week is in an overlapping month

# The Calendar module provides useful utilities for the given locale,
# such as the names of days and months in both full and abbreviated forms
# for i in c.itermonthdays(d.year, d.month):
#     print(i)
# for name in calendar.month_name:
#     print(name)


# Calculate days based on a rule: For example, consider
# a team meeting on the first Friday of every month.
# To figure out what days that would be for each month,
# we can use this script:
print("Team meetings will be on: ")
for m in range(1, 13):
    cal = calendar.monthcalendar(d.year, m)
    # print(cal)
    weekone = cal[0]
    weektwo = cal[1]
    # print(weekone)
    # print(weekone[calendar.FRIDAY])

    if weekone[calendar.FRIDAY] != 0:
        meetday = weekone[calendar.FRIDAY]
    else:
        meetday = weektwo[calendar.FRIDAY]

    print("%10s %2d" % (calendar.month_name[m], meetday))
