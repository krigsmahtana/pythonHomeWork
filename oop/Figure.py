# тест
import math


class Figure:
    def __init__(self, a,b,c,r,name):
        self.name = name
        self.a = a
        self.b = b
        self.c = c
        self.r = r

class Square(Figure):
    name = 'Square'
    def get_name(self):
        return self.name

    def area(self):
        s = self.a ** 2
        return s

    def angles(self=4):
        ang = 4
        return ang

    def perimeter(self):
        d = 4 * self.a
        return d

class Rectangle(Figure):
    name = 'Rectangle'
    def get_name(self):
        return self.name

    def area(self):
        s = self.a * self.b
        return s

    def angles(self=4):
        ang = 4
        return ang

    def perimeter(self):
        d = (2 * self.a) + (2 * self.b)
        return d

class Triangle(Figure):
    name = 'Triangle'
    def get_name(self):
        return self.name

    def area(self):
        p = (self.c + self.b + self.a) / 2
        s = math.sqrt((p * (p - self.c) * (p - self.b) * (p - self.a)))
        return s

    def angles(self=3):
        ang = 3
        return ang

    def perimeter(self):
        d = self.c + self.b + self.a
        return d

class Circle(Figure):
    name = 'Circle'
    def get_name(self):
        return self.name

    def area(self):
        s = math.pi * (self.r ** 2)
        return s

    def angles(self=0):
        ang = 0
        return ang

    def perimeter(self):
        d = 2 * self.r * math.pi
        return d


def add_area(figure1, figure2):
    area_one = figure1
    area_two = figure2
    if  (isinstance(area_one,Figure) and isinstance(area_two, Figure)):
            sum_area = area_one.area() + area_two.area()
            return sum_area
    else:
        return "передан неправильный класс"


