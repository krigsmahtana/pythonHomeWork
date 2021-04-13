#тест
class Rectangle:
    name = 'Rectangle'

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_name (self):
        print(self.name)
        return self.name

    def area(self):
        s = self.a * self.b
        print(s)
        return s

    def angles(self):
        ang = 4
        print(ang)
        return ang

    def perimeter(self):
        d = (2 * self.a) + (2*self.b)
        print(d)
        return d