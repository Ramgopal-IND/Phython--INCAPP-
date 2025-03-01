n1 = int(input("Enter number of students in class: "))
n2 = int(input("Enter number of subjects each student have: "))

students = []

for i in range(n1):
    print("Input details of student", i + 1)
    marks = []
    for j in range(n2):
        marks.append(int(input("Enter marks of subject " + str(j + 1) + ": ")))
    students.append(marks)

print("Sub1\tSub2\tSub3")
for student in students:
    for m in student:
        print(m, end = "\t")
    print()