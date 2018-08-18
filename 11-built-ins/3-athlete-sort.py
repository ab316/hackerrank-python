# https://www.hackerrank.com/challenges/python-sort-sort/problem

N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
K = int(input())

arr.sort(key=lambda x: x[K])
for a in arr:
    print(' '.join(map(str, a)))
