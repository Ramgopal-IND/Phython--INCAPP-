class Person:
    def set_details(self, n, a):
        self.name = n
        self.age = a

    def get_details(self):
        return "Name: " + self.name + "\nAge: " +  str(self.age)

p1 = Person()
p2 = Person()
p1.set_details(input("Enter name: "), int(input("Enter age: ")))
p2.set_details(input("Enter name: "), int(input("Enter age: ")))
print(p1.get_details())
print(p2.get_details())