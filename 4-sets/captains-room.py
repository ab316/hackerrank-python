# https://www.hackerrank.com/challenges/py-the-captains-room/problem

K = int(input())
rooms = list(map(int, input().split()))

print((sum(set(rooms))*K - sum(rooms)) // (K - 1))
