"""oops"""
# 4 pillars of oops. real world entity is represented in the form of class and object in oops concept.
"""
inheritance
encapsulation
abstraction
polymorphism
"""
#class --> blueprint for creating a object . it is a collection of objects and methods that are used to create objects of the calss type. 
#object --> instance of a class . it is a real world entity that has attributes and behavior. 


class car:
    color='red'
    model=2020

    def start_engine(self):
        print("Vroom")

    def stop(self):
        print("Stop")


thar= car()
thar.color='black'

print(thar.color)
# thar.start_engine()
# thar.stop()

fortuner=car()
print(fortuner.color)
# fortuner.start_engine()