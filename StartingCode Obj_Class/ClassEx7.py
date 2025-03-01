class Person:
    def set_details(self, name, age): # self is a reference to the objet itself and it is passed automatically by python when we call a method on an object . It is not passed when we call a method on a class. 
        self.name = name
        self.age = age

    def get_details(self):
        return "Name: " + self.name + "\nAge: " +  str(self.age)

p1 = Person()
p2 = Person()
p1.set_details(input("Enter name: "), int(input("Enter age: ")))
p2.set_details(input("Enter name: "), int(input("Enter age: ")))
print(p1.get_details())
print(p2.get_details())
