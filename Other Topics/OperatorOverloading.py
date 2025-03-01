class ComplexNumber:
    def __init__(self, r = 0, i = 0):
        self.real = r
        self.img = i

    def print_complex_number(self):
        print(self.real, "+", self.img, "i")

    def __add__(self, other):
        new = ComplexNumber()
        new.real = self.real + other.real
        new.img = self.img + other.img
        return new

c1 = ComplexNumber(4, 5)
c1.print_complex_number()
c2 = ComplexNumber(5, 2)
c2.print_complex_number()
c3 = c1 + c2
c3.print_complex_number()