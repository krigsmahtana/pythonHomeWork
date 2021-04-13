#тест
import math

class Circle:
    name = 'Circle'

    def __init__(self, r):
        self.r = r


    def get_name (self):
        print(self.name)
        return self.name

    def area (self):
        s = math.pi*(self.r**2)
        print(s)
        return s

    def angles (self):
        ang = 0
        print(ang)
        return ang

    def perimeter (self):
        d = 2*self.r*math.pi
        print(d)
        return d




