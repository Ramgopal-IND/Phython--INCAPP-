#1
"""   class Person:
    def input_details(p):
        p.name = input("Enter name: ")
        p.age = int(input("Enter age: "))

    def print_details(p):
        print("Name:", p.name)
        print("Age:", p.age)        

p1 = Person()
p2 = Person()
Person.input_details(p1)
Person.input_details(p2)
Person.print_details(p1)
Person.print_details(p2)   """

#2
class Person:
    def input_details(self):
        self.name = input("Enter Name  :")
        self.age = int (input("Enter Age :"))

    def print_details(self):
        print("Name :",self.name )
        print("Age :",self.age )

p1=Person()
p2=Person()
p1.input_details()
p2.input_details()
p1.print_details()
p2.print_details()

