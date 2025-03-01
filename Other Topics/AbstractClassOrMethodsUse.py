from abc import ABC, abstractmethod

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

s = Square(int(input("Enter side of square: ")))
s.find_area()
print("Area of square:", s)
s = Rectangle(int(input("Enter length of square: ")),
int(input("Enter breadth of square: ")))
s.find_area()
print("Area of rectangle:", s)