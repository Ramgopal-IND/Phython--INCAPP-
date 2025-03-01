class Square:
    def __init__(self, s):
        self.side = s

    def find_area(self):
        self.area = self.side ** 2
        print("Area of square:", self.area)

class Cube(Square):
    def __init__(self, s):
        Square.__init__(self, s)

    def find_area(self):
        self.area = 6 * self.side ** 2
        print("Area of cube:", self.area)

s = Cube(4)
s.find_area()
s = Square(5)
s.find_area()