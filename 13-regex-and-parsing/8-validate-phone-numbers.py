# https://www.hackerrank.com/challenges/validating-the-phone-number/problem

import re

for _ in range(int(input())):
    S = input()
    print("YES" if bool(re.match(r'[789]\d{9}$', S)) else "NO")
