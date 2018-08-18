# https://www.hackerrank.com/challenges/class-2-find-the-torsional-angle/problem

import math


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, other):
        return Point(self.x-other.x, self.y-other.y, self.z-other.z)

    def dot(self, other):
        return self.x*other.x + self.y*other.y + self.z*other.z

    def cross(self, other):
        x = self.y*other.z - self.z*other.y
        y = self.x*other.z - self.z*other.x
        z = self.x*other.y - self.y*other.x
        return Point(x, y, z)

    def absolute(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)


A = Point(*map(float, input().split()))
B = Point(*map(float, input().split()))
C = Point(*map(float, input().split()))
D = Point(*map(float, input().split()))

AB = B - A
BC = C - B
CD = D - C
X = AB.cross(BC)
Y = BC.cross(CD)

phi = math.acos(X.dot(Y) / (X.absolute() * Y.absolute()))
print('{:.2f}'.format(math.degrees(phi)))
