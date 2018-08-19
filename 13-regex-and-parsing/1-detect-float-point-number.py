# https://www.hackerrank.com/challenges/introduction-to-regex/problem

import re


for _ in range(int(input())):
    N = input()
    print(bool(re.match('^[+-]?\d*\.\d+$', N)))
