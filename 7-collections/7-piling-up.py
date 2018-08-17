# https://www.hackerrank.com/challenges/piling-up/problem

from collections import deque

T = int(input())
for _ in range(T):
    n = int(input())
    sides = deque(map(int, input().split()))
    valid = True

    while len(sides) > 1:
        if sides[0] >= sides[1]:
            sides.popleft()
        elif sides[-1] >= sides[-2]:
            sides.pop()
        else:
            valid = False
            break

    if valid:
        print('Yes')
    else:
        print('No')
