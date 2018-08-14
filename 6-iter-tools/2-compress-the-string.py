# https://www.hackerrank.com/challenges/compress-the-string/problem

from itertools import groupby

S = map(int, list(input()))

for k, g in groupby(S):
    print((len(list(g)), k), end=' ')
