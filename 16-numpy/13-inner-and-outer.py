# https://www.hackerrank.com/challenges/np-inner-and-outer/problem

import numpy

A = numpy.array(input().split(), int)
B = numpy.array(input().split(), int)
numpy.set_printoptions(legacy='1.13')
print(numpy.inner(A, B))
print(numpy.outer(A, B))
