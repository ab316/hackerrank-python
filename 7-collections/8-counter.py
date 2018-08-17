# https://www.hackerrank.com/challenges/collections-counter/problem

from collections import Counter

X = int(input())
shoes = Counter(map(int, input().split()))
earnings = 0

for _ in range(int(input())):
    size, price = map(int, input().split())
    if shoes[size] > 0:
        shoes[size] -= 1
        earnings += price

print(earnings)
