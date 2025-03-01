class Person:
    def __init__(self):
        self.count = 0
        self.count += 1

    def print_objects_count(self):
        print("No of objects created:", self.count)

# In the above code, we have created an instance variable count and initialized it to 0. 
# We have also created a method print_objects_count() that prints the value of the count variable.
# In the constructor, we have initialized the count variable to 0 and incremented it by 1.


p1 = Person()
p1.print_objects_count()
p2 = Person()
p2.print_objects_count()
