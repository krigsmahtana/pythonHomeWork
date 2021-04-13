import math


class Triangle:
    name = 'Triangle'

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_name (self):
        print(self.name)
        return self.name

    def area(self):
        p = (self.c+self.b+self.a)/2
        s = math.sqrt((p*(p-self.c) * (p-self.b) * (p-self.a)))
        print(s)
        return s

    def angles(self):
        ang = 3
        print(ang)
        return ang

    def perimeter(self):
        d = self.c + self.b + self.a
        print(d)
        return d

