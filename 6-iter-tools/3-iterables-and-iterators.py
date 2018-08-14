# https://www.hackerrank.com/challenges/iterables-and-iterators/problem

import itertools

N = int(input())
S = input().split()
K = int(input())

C = list(itertools.combinations(S, K))
F = list(itertools.filterfalse(lambda x: 'a' not in x, C))
p = len(F) / len(C)
print('{:.3f}'.format(p))


