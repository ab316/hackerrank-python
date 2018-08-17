# https://www.hackerrank.com/challenges/calendar-module/problem

import calendar

mm, dd, yyyy = map(int, input().split())
day = calendar.weekday(yyyy, mm, dd)
print(calendar.day_name[day].upper())
