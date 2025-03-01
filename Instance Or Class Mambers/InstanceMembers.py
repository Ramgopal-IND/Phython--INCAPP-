class Person:
    def __init__(self,name,age,city):
        self.name=name
        self.age=age
        self.city=city

    def print_details(self): 
        print("Name :",self.name)  
        print("Age :",self.age)
        print("City :",self.city)

    def change_city(self,new_city):
        self.city=new_city
        
# def change_city or def print_details is called instance members . they are called by instance methods.
# And self.name, self.age, self.city are instance variables.
 
p1 = Person("Radha", 23, "Barasana")
p2 = Person('Krishn', 22, 'Nandgaon')
p1.print_details()
p2.print_details()
p1.change_city('Vrindavan')
p1.print_details()
p2.print_details()       

