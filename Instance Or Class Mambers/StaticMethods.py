# This is 3rd type methods in python (OOP). Remember : 1. Instance Methods , 2. Class Methods , 3. Static Methods.

#a.
#Simple:-
class Calculator:
    def add(n1, n2):
        return n1 + n2
    
    def sub(n1, n2):
        return n1 - n2

Calculator.add = staticmethod(Calculator.add)
Calculator.sub = staticmethod(Calculator.sub)
print(Calculator.add(12, 23))
print(Calculator.sub(12, 23))

#b.
#With @ :-
class Calculator:
    @staticmethod
    def add(n1, n2):
        return n1 + n2
    
    @staticmethod
    def sub(n1, n2):
        return n1 - n2

print(Calculator.add(12, 3))
print(Calculator.sub(12, 3))
        
        
