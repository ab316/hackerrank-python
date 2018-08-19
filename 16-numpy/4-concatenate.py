# https://www.hackerrank.com/challenges/np-concatenate/problem

import numpy

N, M, P = map(int, input().split())

arr1 = []
arr2 = []
for _ in range(N):
    arr1.append(input().split())

for _ in range(M):
    arr2.append(input().split())

print(numpy.concatenate((numpy.array(arr1, int), numpy.array(arr2, int))))
