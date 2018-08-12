# https://www.hackerrank.com/challenges/nested-list/problem

results = [[input(), float(input())] for i in range(int(input()))]
second_lowest = sorted(set(r[1] for r in results))[1]
for s in sorted(r[0] for r in results if r[1] == second_lowest):
    print(s)
