# тест
from oop import Figure


class example_for_test():
    pass


def test_circle():
    assert Figure.Circle.name == "Circle"
    assert Figure.Circle(a=2, b=0, c=3, name="Circle", r=3).area() == 28.274333882308138
    assert Figure.Circle(a=2, b=0, c=3, name="Circle", r=3).perimeter() == 18.84955592153876
    assert Figure.Circle.angles() == 0


def test_square():
    assert Figure.Square.angles() == 4
    assert Figure.Square(a=2, b=0, c=3, name="Square", r=1).area() == 4
    assert Figure.Square.name == 'Square'
    assert Figure.Square(a=2, b=0, c=3, name="Square", r=1).perimeter() == 8


def test_rectangle():
    assert Figure.Rectangle.name == 'Rectangle'
    assert Figure.Rectangle(a=3, b=8, c=3, name="Rectangle", r=3).area() == 24
    assert Figure.Rectangle(a=3, b=8, c=3, name="Rectangle", r=3).perimeter() == 22
    assert Figure.Rectangle.angles() == 4


def test_triangle():
    assert Figure.Triangle.name == 'Triangle'
    assert Figure.Triangle(a=2, b=3, c=4, name="Triangle", r=3).area() == 2.9047375096555625
    assert Figure.Triangle(a=2, b=3, c=4, name="Triangle", r=3).perimeter() == 9
    assert Figure.Triangle.angles() == 3


def test_add_area():
    assert Figure.add_area(figure1=Figure.Circle(a=2, b=3, c=4, name="Circle", r=3),
                           figure2=Figure.Triangle(a=2, b=3, c=4, name="Triangle", r=3)) == 31.1790713919637
    assert Figure.add_area(figure1=example_for_test(),
                           figure2=Figure.Circle(a=2, b=3, c=4, name="Circle", r=3)) == "передан неправильный класс"
