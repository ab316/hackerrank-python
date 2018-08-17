# https://www.hackerrank.com/challenges/defaultdict-tutorial/problem

from collections import defaultdict

n, m = map(int, input().split())
A = defaultdict(list)

for i in range(n):
    A[input()].append(i+1)


for i in range(m):
    s = input()
    if s in A:
        print(*A[s])
    else:
        print(-1)
