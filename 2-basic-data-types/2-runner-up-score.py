# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

N = int(input())
arr = map(int, input().split())
s = list(sorted(set(arr)))

print(s[-2])
