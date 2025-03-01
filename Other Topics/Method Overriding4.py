class Square:
    def __init__(self, s):
        self.side = s

    def find_area(self):
        self.area = self.side ** 2

    def __str__(self):
        return "Area of square: " + str(self.area)

class Cube(Square):
    def __init__(self, s):
        Square.__init__(self, s)

    def find_area(self):
        self.area = 6 * self.side ** 2

    def __str__(self):
        return "Area of cube: " + str(self.area)

shapes = [Cube(int(input("Enter side of cube: "))),
Square(int(input("Enter side of square: ")))]

for shape in shapes:
    shape.find_area()
    print(shape)
