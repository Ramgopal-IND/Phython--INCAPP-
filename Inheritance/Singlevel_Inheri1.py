class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def print_person_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("City:", self.city)

class Student(Person):
    def __init__(self, name, age, city, roll_number):
        Person.__init__(self, name, age, city)
        self.roll_number = roll_number

    def print_student_details(self):
        print("Roll Number:", self.roll_number)

s = Student("Vijay Kumar", 23, "Greater Noida", 101)
s.print_person_details()
s.print_student_details()