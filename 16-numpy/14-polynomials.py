# https://www.hackerrank.com/challenges/np-polynomials/problem

import numpy

P = numpy.array(input().split(), float)
x = float(input())
print(numpy.polyval(P, x))
