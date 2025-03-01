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
        
        print("----------------------")
        self.roll_number = roll_number

    def print_student_details(self):
        print("Roll Number:", self.roll_number)

class Result(Student):
    def __init__(self, name, age, city, roll_number, marks1, marks2, marks3):
        Student.__init__(self, name, age, city, roll_number)
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

    def print_result_details(self):
        
        total = self.marks1 + self.marks2 + self.marks3
        percentage = total / 300 * 100
        print("Marks of first subject:", self.marks1)
        print("Marks of second subject:", self.marks2)
        print("Marks of third subject:", self.marks3)
        print("Total of marks:", total)
        print("Percentage of marks:", round(percentage, 2))
        print("----------------------")


r = Result(input("Enter Student Name :"),int(input("Enter Age :")), input("Enter City :"),  int (input("Enter Roll Number :")),
        int (input("Enter 1st Sub Marks :")), int (input("Enter secend Sub Marks :")),int (input("Enter 3rd Sub Marks :")))

r.print_student_details()
r.print_person_details()
r.print_result_details()



