# https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers/problem

import math


class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imaginary - other.imaginary)

    def __mul__(self, other):
        r = self.real*other.real - self.imaginary*other.imaginary
        i = self.imaginary*other.real + self.real*other.imaginary
        return Complex(r, i)

    def __truediv__(self, other):
        denominator = other.real**2 + other.imaginary**2
        r = self.real*other.real + self.imaginary*other.imaginary
        i = self.imaginary*other.real - self.real*other.imaginary
        return Complex(r / denominator, i / denominator)

    def __abs__(self):
        return Complex(math.sqrt(self.real**2 + self.imaginary**2), 0)

    def __str__(self):
        if self.imaginary == 0:
            result = "{:.2f}+0.00i".format(self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+{:.2f}i".format(self.imaginary)
            else:
                result = "0.00-{:.2f}i".format(abs(self.imaginary))
        elif self.imaginary > 0:
            result = "{:.2f}+{:.2f}i".format(self.real, self.imaginary)
        else:
            result = "{:.2f}-{:.2f}i".format(self.real, abs(self.imaginary))
        return result


r1, i1 = map(float, input().split())
r2, i2 = map(float, input().split())
c1 = Complex(r1, i1)
c2 = Complex(r2, i2)

print(c1 + c2)
print(c1 - c2)
print(c1 * c2)
print(c1 / c2)
print(abs(c1))
print(abs(c2))
