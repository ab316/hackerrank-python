# https://www.hackerrank.com/challenges/hex-color-code/problem

import re

for _ in range(int(input())):
    matches = re.findall(r'(?<!^)(#(?:[0-9A-F]{3}){1,2})', input().strip(), re.IGNORECASE)
    [print(x) for x in matches]
