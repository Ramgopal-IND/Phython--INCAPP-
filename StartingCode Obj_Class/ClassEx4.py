class Person:
    pass

p1 = Person()
p2 = Person()
p1.name = input("Enter name: ")
p1.age = int(input("Enter age: "))
p2.name = input("Enter name: ")
p2.age = int(input("Enter age: "))
print("Name:", p1.name)
print("Age:", p1.age)
print("Name:", p2.name)
print("Age:", p2.age)
