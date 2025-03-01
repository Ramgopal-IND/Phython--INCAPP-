class Person:
    def __init__(self, value1, value2):
        self.name = value1
        self.age = value2

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

p = Person("Vijay Mehra", 23)
print("Name:", p.name)
print("Age:", p.age)
