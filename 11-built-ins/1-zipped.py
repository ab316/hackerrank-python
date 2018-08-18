# https://www.hackerrank.com/challenges/zipped/problem

N, X = map(int, input().split())
marks = []
for _ in range(X):
    marks.append(map(float, input().split()))

students = zip(*marks)
for s in students:
    print('{:.1f}'.format(sum(s) / X))
