# https://www.hackerrank.com/challenges/np-zeros-and-ones/problem

import numpy

dims = list(map(int, input().split()))
print(numpy.zeros(dims, int))
print(numpy.ones(dims, int))
