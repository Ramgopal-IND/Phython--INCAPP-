class Student:
    College_Name="ABC Collge"
    College_director="Vijay Kumar"

    def __init__(self, r, n, p):
        self.roll_number = r
        self.name = n
        self.phone_number = p

    def print_student_details(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll_number)
        print("Phone Number:", self.phone_number)
        print("College Name:", self.College_Name)
        print("College Director:", self.College_director)

    def change_phone_number(self, np):
        self.phone_number = np

    def change_college_director(self, nd):
        Student.College_director = nd

s1 = Student(101, "Vijay Yadav", 9811234511)
s2 = Student(102, "Manoj Pandey", 8833114567)
s1.print_student_details()
s2.print_student_details()
s1.change_phone_number(7988112345)
s2.change_college_director("Sanjeev Kumar")
s1.print_student_details()
s2.print_student_details() 
