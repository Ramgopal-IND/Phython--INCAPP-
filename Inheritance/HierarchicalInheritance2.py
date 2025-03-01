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
        super().__init__(name, age, city)
        self.roll_number = roll_number

    def print_student_details(self):
        print("Roll Number:", self.roll_number)

class Employee(Person):
    def __init__(self, name, age, city, employee_id, salary):
        super().__init__(name, age, city)
        self.employee_id = employee_id
        self.salary = salary

    def print_employee_details(self):
        print("Employee Id:", self.employee_id)
        print("Salary:", self.salary)

s = Student("Vijay Kumar", 23, "Greater Noida", 101)
s.print_person_details()
s.print_student_details()

e = Employee("Manoj Pandey", 25, "New Delhi", 10001, 56500)
e.print_person_details()
e.print_employee_details()