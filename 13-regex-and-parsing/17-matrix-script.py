# https://www.hackerrank.com/challenges/matrix-script/problem

import re


N, M = map(int, input().split())
rows = []
for _ in range(N):
    rows.append(input())

matrix = list(map(list, zip(*rows)))
str = ''.join([''.join(x) for x in matrix])
print(re.sub(r'(\w)([\W]+)(\w)', r'\1 \3', str))
