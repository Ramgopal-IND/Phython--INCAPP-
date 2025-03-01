class Square:
    def __init__(self,s):
        self.side=s
    def find_area(self):
        self.area = self.side ** 2 

    def  get_area(self):
        return "Area of Square:"+ str(self.area)
    
class Cube(Square):
    def __init__(self, s):
        Square.__init__(self, s)

    def find_area(self):
        self.area = 6 * self.side ** 2

    def get_area(self):
        return "Area of cube: "+ str(self.area)

shapes = [Square(int(input("Enter side of square: "))),
Cube(int(input("Enter side of cube: ")))]

for shape in shapes:
    shape.find_area()
    print(shape.get_area())
