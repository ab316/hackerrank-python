# https://www.hackerrank.com/challenges/find-angle/problem

from math import *

AB = int(input())
BC = int(input())

ACB = atan(AB / BC)
degrees = round(degrees(ACB))
print('{:}°'.format(degrees))
