# https://www.hackerrank.com/challenges/re-start-re-end/problem

import re

S = input()
k = input()

pattern = re.compile(k)
match = pattern.search(S)

if not match:
    print((-1, -1))

while match:
    print((match.start(), match.end() - 1))
    start = match.start() + 1
    match = pattern.search(S, start)
