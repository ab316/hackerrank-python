# https://www.hackerrank.com/challenges/np-sum-and-prod/problem

import numpy

N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(input().split())

narr = numpy.array(arr, int)
print(numpy.product(numpy.sum(narr, 0)))
