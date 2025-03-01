class Person:
    pass

p1 = Person()
p2 = p1
p1.name = "Manoj Pandey"
p1.age = 23
print("Name:", p2.name)
print("Age:", p2.age)
print("Name:", p1.name)
print("Age:", p1.age)