# https://www.hackerrank.com/challenges/itertools-product/problem

import itertools

A = map(int, input().split())
B = map(int, input().split())

print(list(itertools.product(A, B)))
