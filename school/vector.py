import math


class Vec:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __sub__(self, v):
        return Vec(self.x - v.x, self.y - v.y)

    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)


class Scanner:
    def __init__(self, file_name):
        self.tokens = []
        self.input_file = open(file_name, 'rt')

    def __del__(self):
        self.input_file.close()

    def read_token(self):
        while not self.tokens:
            t = self.input_file.readline().split()
            self.tokens = t[::-1]  # reverse order
        return self.tokens.pop()

    def read_float(self):
        return float(self.read_token())

    def read_vec(self):
        x = self.read_float()
        y = self.read_float()
        return Vec(x, y)


if __name__ == '__main__':
    s = Scanner("length.in")
    A = s.read_vec()  # радиус-вектор OA
    B = s.read_vec()  # радиус-вектор OB
    result = open('length.out', 'w')
    result.write(str((A - B).length()) + '\n')
    result.close()
