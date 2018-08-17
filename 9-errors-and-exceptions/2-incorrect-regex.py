# https://www.hackerrank.com/challenges/incorrect-regex/problem

import re

for _ in range(int(input())):
    S = input()
    try:
        re.compile(S)
        print("True")
    except Exception as e:
        print("False")
