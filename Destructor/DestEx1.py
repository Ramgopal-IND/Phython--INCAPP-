class A:
    def __init__(self):
        print("Hello, I am Constructor")
    def __del__(self): # 1.Destructor is a special method which is called when the object is no longer in use. 
        print("Hello, I am Destructor") # 2.It is called before the object is destroyed. It is also called destructor method.
        # 3. It is used to clean up the resources.
        # 4. It is called when the reference count becomes zero.
        # 5. It is called when the program exits.
        # 6. It is called when the object is deleted using del keyword.
        # 7. It is called when the object is garbage collected.
        # 8. It is called when the object is destroyed.
a1=A()
a2=A()
del a1 # 1.del is a keword to delete the object. 
del a2 #2.It will call the destructor of the class A and delete the object O1 and O2 .
#3. It will print the message "Hello, I am Destructor" two times.
#4. It will delete the object O1 and O2.


