# https://www.hackerrank.com/challenges/python-tuples/problem

input()
integers = tuple(map(int, input().split()))
print(hash(integers))
