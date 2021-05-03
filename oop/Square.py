#тест
class Square:
    name = 'Square'

    def __init__(self, a):
      self.a = a

    def get_name (self):
        print(self.name)

    def area(self):
        s = self.a ** 2
        print(round(s))
        return s

    def angles(self):
        ang = 4
        print(ang)
        return ang

    def perimeter(self):
        d = 4 * self.a
        print(d)
        return d
