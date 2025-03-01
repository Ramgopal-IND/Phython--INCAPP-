# Without Inheritance :
class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def print_person_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("City:", self.city)

class Student:
    def __init__(self, name, age, city, roll_number):
        self.name = name
        self.age = age
        self.city = city
        self.roll_number = roll_number

    def print_student_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("City:", self.city)
        print("Roll Number:", self.roll_number)

p = Person("Ajay Kumar", 22, "Noida")
p.print_person_details()

s = Student("Vijay Kumar", 23, "Greater Noida", 101)
s.print_student_details()