from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    def __init__(self):
        self.area = 0

    @abstractmethod
    def find_area(self):
        pass

class Square(Shape):
    def __init__(self, s):
        Shape.__init__(self)
        self.side = s

    def find_area(self):
        self.area = self.side ** 2

    def __str__(self):
        return str(self.area)

class Rectangle(Shape):
    def __init__(self, l, b):
        Shape.__init__(self)
        self.length = l
        self.breadth = b

    def find_area(self):
        self.area = self.length * self.breadth

    def __str__(self):
        return str(self.area)

class Circle(Shape):
    def __init__(self, r):
        Shape.__init__(self)
        self.radius = r

    def find_area(self):
        self.area = pi * self.radius ** 2

    def __str__(self):
        return str(self.area)

shape = None
while True:
    print("Enter s to find area of square")
    print("Enter r to find area of rectangle")
    print("Enter c to find area of circle")
    ch = input("Enter your choice: ")
    if ch == 's':
        shape = Square(int(input("Enter side of square: ")))
    elif ch == 'r':
        shape = Rectangle(int(input("Enter length of rectangle: ")), int(input("Enter breadth of rectangle: ")))
    elif ch == 'c':
        shape = Circle(float(input("Enter radius of circle: ")))
    else:
        print("Wrong choice entered")
    if shape is not None:
        shape.find_area()
        print(shape)
    ch = input("Do you want to continue? [yes/no]: ")
    if ch != 'yes':
        break