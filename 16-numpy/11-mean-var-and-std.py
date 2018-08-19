# https://www.hackerrank.com/challenges/np-mean-var-and-std/problem

import numpy


N, M = map(int, input().split())
arr = numpy.array([input().split() for _ in range(N)], int)
numpy.set_printoptions(legacy='1.13')
print(arr.mean(1))
print(arr.var(0))
print(arr.std())
