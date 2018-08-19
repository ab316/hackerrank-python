# https://www.hackerrank.com/challenges/np-dot-and-cross/problem

import numpy

N = int(input())
arr1 = numpy.array([input().split() for _ in range(N)], int)
arr2 = numpy.array([input().split() for _ in range(N)], int)
numpy.set_printoptions(legacy='1.13')
print(numpy.dot(arr1, arr2))
