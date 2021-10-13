from math import *


def is_zero(val):
    if (type(val) is int):
        return (val == 0)
    elif (type(val) is float):
        return abs(val) < 0.000013
    else:
        raise BaseException


class vec:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"vec({self.x!r}, {self.y!r})"

    def __str__(self):
        return f"{self.x} {self.y}"

    def __neg__(self):
        return vec(-self.x, -self.y)

    def __add__(self, v):
        if (not (type(v) is vec)):
            raise BaseException
        return vec(self.x + v.x, self.y + v.y)

    def __sub__(self, v):
        if (not (type(v) is vec)):
            raise BaseException
        return vec(self.x - v.x, self.y - v.y)

    def __mul__(self, val):
        if (type(val) is vec):
            return self.x * val.x + self.y * val.y

        return vec(self.x * val, self.y * val)

    def length2(self):
        return self.x * self.x + self.y * self.y

    def length(self):
        return sqrt(self.length2())

    def angle(self):
        return atan2(self.y, self.x)

    def left(self):
        return vec(-self.y, self.x)

    def right(self):
        return vec(self.y, -self.x)


class line:
    def __init__(self, p0, normal):
        self.p0 = p0
        self.normal = normal

    def __repr__(self):
        return f"line({self.p0.__repr__()}, {self.normal.__repr__()})"

    def __str__(self):
        return f"{self.p0} {self.normal}"

    def from_abc(a, b, c):
        normal = vec(a, b)
        p0 = normal * (-c / normal.length2())
        return line(p0, normal)

    def to_abc(self):
        A = self.p0
        B = A + self.normal.right()
        delta = B - A
        a = 1
        b = 1
        c = 1
        if (delta.x == 0):
            b = 0
            c = -A.x
        elif (delta.y == 0):
            a = 0
            c = -A.y
        else:
            a = -(delta.y / delta.x)
            c = -(a * self.p0.x + self.p0.y)
        return (a, b, c)

    def from_points(A, B):
        normal = (A - B).left()
        return line(A, normal)

    def contains(self, point):
        if not (type(point) is vec):
            raise BaseException
        return is_zero((point - self.p0) * self.normal)


class reader:
    def __init__(self, file_name):
        f = open(str(file_name), "rt")
        self.buf = f.read()
        f.close()
        self.buf = list(self.buf.strip().split())
        self.i = 0

    def r_int(self):
        self.i += 1
        return int(self.buf[self.i - 1])

    def r_flt(self):
        self.i += 1
        return float(self.buf[self.i - 1])


class writer:
    def __init__(self, file_name):
        self.f = open(str(file_name), "wt")

    def __del__(self):
        self.f.close()

    def w_int(self, n):
        print(int(n), file=self.f, end='')

    def w_flt(self, n):
        print(float(n), file=self.f, end='')

    def w_yes_no(self, n):
        if (n):
            print("YES", file=self.f, end='')
        else:
            print("NO", file=self.f, end='')

    def w_raw(self, data):
        print(data, file=self.f, end='')


if (__name__ == "__main__"):
    in_f = reader("line2.in")
    out_f = writer("line2.out")

    tmp1 = vec(in_f.r_flt(), in_f.r_flt())
    tmp2 = vec(in_f.r_flt(), in_f.r_flt())
    tmp3 = line(tmp1, tmp2)
    tmp4 = tmp3.to_abc()

    out_f.w_raw(f"{tmp4[0]} {tmp4[1]} {tmp4[2]}")
