#тест
# General class
from oop.Rectangle import Rectangle
from oop.Circle import Circle
from oop.Square import Square
from oop.Triangle import Triangle


class Figure:
    _instance = None
    # просто тестовые данные
    a = 3
    b = 8
    c = 7

    # Работа с треугольником
    triangle = Triangle(a, b, c)
    triangle.get_name()
    triangle.area()
    triangle.perimeter()
    triangle.angles()

    # работа с окружностью
    circle = Circle(r=a)
    circle.get_name()
    circle.area()
    circle.perimeter()
    circle.angles()

    # работа с квадратом
    square = Square(a)
    square.get_name()
    square.area()
    square.perimeter()
    square.angles()

    # работа с прямоугольником
    rectangle = Rectangle(a, b)
    rectangle.get_name()
    rectangle.area()
    rectangle.perimeter()
    rectangle.angles()

    # складывание площадей
def add_area(area_one, area_two):
    area_one = area_one
    area_two = area_two

    try:
        sum_area = area_one + area_two
        print(sum_area)
        return  sum_area
    except ValueError:
        print("передан неправильный класс")


