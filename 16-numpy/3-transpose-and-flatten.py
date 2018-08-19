# https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem

import numpy

N, M = map(int, input().split())

arr = []
for _ in range(N):
    arr.append(input().split())

numpy_arr = numpy.array(arr, int)
print(numpy_arr.transpose())
print(numpy_arr.flatten())
