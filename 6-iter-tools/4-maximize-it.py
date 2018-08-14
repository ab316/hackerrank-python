# https://www.hackerrank.com/challenges/maximize-it/problem

import itertools

K, M = map(int, input().split())
L = []
for i in range(K):
    N_i, *x = map(int, input().split())
    L.append(map(lambda x: x**2, x))

sums = map(lambda x: sum(x) % M, itertools.product(*L))
print(max(sums))
