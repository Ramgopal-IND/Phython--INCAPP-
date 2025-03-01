class Person:
    def __init__(self,n,age):
        self.name=n
        self.age=age

    def print_details(self):
        print("Name :",self.name)
        print("Age :",self.age)

p1=Person(input("Enter Name :"),int(input("Enter Age :")))
p2=Person(input("Enter Name :"),int(input("Enter Age :")))

p1.print_details()
p2.print_details()

