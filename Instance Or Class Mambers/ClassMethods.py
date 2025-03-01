#1. 
class Person:
    
    count = 0

    def __init__(self):
        Person.count += 1

    def print_objects_count(cls):
        print("No of objects created:", cls.count)

#Person.print_objects_count = classmethod(Person.print_objects_count)
#Or
Person.print=classmethod(Person.print_objects_count)
 
#Variable name can be same or diff . both are posible.

#Person.print_objects_count()
Person.print()

p1 = Person()
#p1.print_objects_count()
p1.print()

p2 = Person()
#p2.print_objects_count()
p2.print()

#2. 
class People:
    
    count = 0

    def __init__(self):
        People.count += 1

    @classmethod    # Advance virsion . In Python, the @ symbol is used as a decorator. Decorators are a way to modify the behavior of a function or class without directly changing its source code.
    def print_objects_count(cls):
        print("No of objects created:", cls.count)

People.print_objects_count()
pe1 = People()
pe1.print_objects_count()
pe2 = People()
pe2.print_objects_count()