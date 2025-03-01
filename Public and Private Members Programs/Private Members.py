class Person:
    def __init__(self, value):
        self.__age = value

    def print_age(self):
        print(self.__age)

p = Person(23)
p.print_age()
print(p.__age) # Error as __age is private member of class Person and can't be accessed outside the class Person .