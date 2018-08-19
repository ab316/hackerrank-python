# https://www.hackerrank.com/challenges/np-array-mathematics

import numpy

N, M = map(int, input().split())

arr1 = []
arr2 = []

for _ in range(N):
    arr1.append(input().split())

for _ in range(N):
    arr2.append(input().split())

numpy_arr1 = numpy.array(arr1, int)
numpy_arr2 = numpy.array(arr2, int)

print(numpy_arr1 + numpy_arr2)
print(numpy_arr1 - numpy_arr2)
print(numpy_arr1 * numpy_arr2)
print(numpy_arr1 // numpy_arr2)
print(numpy_arr1 % numpy_arr2)
print(numpy_arr1 ** numpy_arr2)
