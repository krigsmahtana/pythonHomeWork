from oop import Figure


def test_circle():
  assert Figure.Circle.name == "Circle"
  assert Figure.Circle(r=3).area() == 28.274333882308138
  assert Figure.Circle(r=3).perimeter() ==18.84955592153876
  assert Figure.Circle.angles(self=3) == 0


def test_square():
    assert Figure.Square.angles(self=2) == 4 # а почему так?
    assert Figure.Square(a=3).area() == 9
    assert Figure.Square.name == 'Square'
    assert Figure.Square(a=3).perimeter() == 12

def test_rectangle():
    assert Figure.Rectangle.name == 'Rectangle'
    assert Figure.Rectangle(a=3, b=8).area() == 24
    assert Figure.Rectangle(a=3, b=8).perimeter() == 22
    assert Figure.Rectangle.angles(self=2) == 4

def test_triangle():
    assert Figure.Triangle.name == 'Triangle'
    assert Figure.Triangle(a=2,b=3,c=4).area() == 2.9047375096555625
    assert Figure.Triangle(a=2,b=3,c=4).perimeter() == 9
    assert Figure.Triangle.angles(self=2) == 3

def test_add_area():
    assert Figure.add_area(area_one=10, area_two=20) == 30
    assert Figure.add_area(Figure.Circle(r=3).area(), Figure.Triangle(a=2,b=3,c=4).area()) == 31.1790713919637
    assert Figure.add_area(Figure.Square(a=3).area(), Figure.Rectangle(a=3, b=8).area()) == 33

