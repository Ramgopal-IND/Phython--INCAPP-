class A:
    def __del__(self):
        print("Bye")
        
    def __init__(self):
        print("Hi")

a1=A()
a2=A()
