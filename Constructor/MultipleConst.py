class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
    # 1. In Python, we can define multiple constructors in a class.
    # 2. The last constructor will be considered. And the previous constructors will be overridden. 
    # 3. It is called Constructor Overloading.
    # 4. It is not supported in Python.
    # 5. It is not possible to define multiple constructors in a class.
    

    def print_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("City:", self.city)

p1 = Person("Manoj Pandey", 23)
p2 = Person('Vijay Verma', 22, "Greater Noida")
p1.print_details()
p2.print_details()