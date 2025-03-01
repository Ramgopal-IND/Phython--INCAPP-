class A:
    def m1(self):
        print("Hello")

class B(A):
    def m2(self):
        print("Hi")

class C:
    def m3(self):
        print("Welcome")

class D(B, C):
    def m4(self):
        print("Bye")

d = D()
d.m1()
d.m2()
d.m3()
d.m4()