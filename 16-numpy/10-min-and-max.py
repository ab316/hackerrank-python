# https://www.hackerrank.com/challenges/np-min-and-max/problem

import numpy

N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(input().split())

narr = numpy.array(arr, int)
print(numpy.max(numpy.min(narr, 1)))
