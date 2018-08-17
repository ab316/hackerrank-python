# https://www.hackerrank.com/challenges/py-collections-deque/problem

from collections import deque


N = int(input())
q = deque()

for _ in range(N):
    op = input().split()
    if op[0] == 'append':
        q.append(op[1])
    elif op[0] == 'pop':
        q.pop()
    elif op[0] == 'popleft':
        q.popleft()
    elif op[0] == 'appendleft':
        q.appendleft(op[1])

print(' '.join(q))
