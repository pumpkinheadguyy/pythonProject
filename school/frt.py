﻿import math


class Line:
    def __init__(self, p0, normal):
        self.p0 = p0
        self.normal = normal

    # line = Line.from_abc(a, b, c)
    def from_abc(a, b, c):
        normal = Vec(a, b)
        p0 = normal * (-c / normal.len2())
        return Line(p0, normal)

    # line = Line.from_points(A, B)
    def from_points(A, B):
        normal = (A - B).left()
        return Line(A, normal)


class Vec:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vec({self.x!r}, {self.y!r})"

    def __str__(self):
        return f"{self.x} {self.y}"

    def __neg__(self):
        return Vec(-self.x, -self.y)

    def __add__(self, v):
        pass

    def __sub__(self, v):
        pass

    # Скалярное произведение (dot product)
    # или умножение вектора на число, если a — не вектор
    def __mul__(self, a):
        if type(a) is Vec:
            return self.x * a.x + self.y * a.y
        return Vec(self.x * a, self.y * a)

    # Квадрат длины вектора
    def len2(self):
        pass

    def length(self):
        pass

    def left(self):
        pass

    def right(self):
        pass


def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
       raise Exception('lines do not intersect')

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return x, y


if __name__ == '__main__':
    with open('intersec.in', 'r') as input_file:
        a, b, c, d, e, i = (map(int, input_file.read().split()))
    line1 = Line.from_abc(a, b, c)
    line2 = Line.from_abc(c, d, e)
    print(line_intersection(line1, line2))
