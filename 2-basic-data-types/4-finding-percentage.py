# https://www.hackerrank.com/challenges/finding-the-percentage/problem

import math

N = int(input())
records = {}

for i in range(N):
    name, *line = input().split()
    records[name] = list(map(float, line))

query_name = input()
marks = records[query_name]
average = math.fsum(marks) / len(marks)
# print(f'{average:.2f}')       (Python >=3.6)
print('{:.2f}'.format(average))
