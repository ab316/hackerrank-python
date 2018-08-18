# https://www.hackerrank.com/challenges/reduce-function/problem

from fractions import Fraction
from functools import reduce


def product(fracs):
    t = reduce(lambda a, b: Fraction(a.numerator*b.numerator, a.denominator*b.denominator), fracs)
    return t.numerator, t.denominator


fracs = []
for _ in range(int(input())):
    fracs.append(Fraction(*map(int, input().split())))
result = product(fracs)
print(*result)
