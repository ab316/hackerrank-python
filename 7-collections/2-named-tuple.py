# https://www.hackerrank.com/challenges/py-collections-namedtuple/problem

from collections import namedtuple

N = int(input())
columns = input().strip().split()
Student = namedtuple('Student', columns)
students = []

for i in range(N):
    students.append(Student(*input().strip().split()))

average = sum([int(s.MARKS) for s in students]) / len(students)
print('{:.2f}'.format(average))
