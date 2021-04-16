# тест
import math


class Figure:
    pass


class Square(Figure):
    name = 'Square'

    def __init__(self, a):
        self.a = a

    def get_name(self):
        return self.name

    def area(self):
        s = self.a ** 2
        return s

    def angles(self):
        ang = 4
        return ang

    def perimeter(self):
        d = 4 * self.a
        return d


class Rectangle(Figure):
    name = 'Rectangle'

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_name(self):
        return self.name

    def area(self):
        s = self.a * self.b
        return s

    def angles(self):
        ang = 4
        return ang

    def perimeter(self):
        d = (2 * self.a) + (2 * self.b)
        return d


class Triangle(Figure):
    name = 'Triangle'

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_name(self):
        return self.name

    def area(self):
        p = (self.c + self.b + self.a) / 2
        s = math.sqrt((p * (p - self.c) * (p - self.b) * (p - self.a)))
        return s

    def angles(self):
        ang = 3
        return ang

    def perimeter(self):
        d = self.c + self.b + self.a
        return d


class Circle(Figure):
    name = 'Circle'

    def __init__(self, r):
        self.r = r

    def get_name(self):
        return self.name

    def area(self):
        s = math.pi * (self.r ** 2)
        return s

    def angles(self):
        ang = 0
        return ang

    def perimeter(self):
        d = 2 * self.r * math.pi
        return d


def add_area(area_one, area_two):
    area_one = area_one
    area_two = area_two

    try:
        sum_area = area_one + area_two
        return sum_area
    except Exception:
        return "передан неправильный класс"
