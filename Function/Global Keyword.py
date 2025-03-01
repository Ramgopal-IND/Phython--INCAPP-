#1
def display():
    global a
    a = 3

display()
print(a)

#2
def display():
    global a
    a = 5

a = 2
print(a)
display()
print(a)
