class Person:
    def __init__(self, fn, ln):
        self.first_name = fn
        self.last_name = ln

    def __str__(self):
        return self.first_name + " " +  self.last_name

persons = []

for i in range(int(input("Enter how many persons record you want to store: "))):
    print("IInput details of person", i + 1)
    persons.append(Person(input("Enter first name: "), input("Enter last name: ")))

print("Details of all persons are")
for p in persons:
    print(p)