# https://www.hackerrank.com/challenges/python-time-delta/problem

import datetime

for _ in range(int(input())):
    dt1 = datetime.datetime.strptime(input(), "%a %d %b %Y %H:%M:%S %z")
    dt2 = datetime.datetime.strptime(input(), "%a %d %b %Y %H:%M:%S %z")
    diff = int(abs(dt2.timestamp() - dt1.timestamp()))
    print(diff)

