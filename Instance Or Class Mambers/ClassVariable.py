class person:
    count_instance = 0 # This is class variable and it is shared by all objects of the class.
    def __init__(self):
        person.count_instance += 1

    def print_instance_count(self):
        print("No of instances created:", person.count_instance)

# Calss variable or Instance variable  difference: 
# 1. Instance variables are unique to each object.
# 2. Class variables are shared by all objects of the class.
# 3. Instance variables are defined inside the constructor.
# 4. Class variables are defined outside the constructor.
# 5. Instance variables are accessed using self keyword.
# 6. Class variables are accessed using class name.

p1=person()
p1.print_instance_count()         
p2=person()
p1.print_instance_count()
p2.print_instance_count()
