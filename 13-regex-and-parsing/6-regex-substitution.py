# https://www.hackerrank.com/challenges/re-sub-regex-substitution/problem

import re

for _ in range(int(input())):
    S = input()
    S = re.sub(r'(?<= )&{2}(?= )', 'and', S)
    S = re.sub(r'(?<= )\|{2}(?= )', 'or', S)
    print(S)
