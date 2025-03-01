class Person:
    def __init__(self, value):
        self.__age = value
        self.__print_age()

    def __print_age(self):
        print(self.__age)

p = Person(23)
p.__print_age()
