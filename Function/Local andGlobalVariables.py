#1
def fun():
    a = 2 # This is local varrialbe.
    print(a)

fun()
#print(a) #This will give error because a is local variable .




def fun():
    a = 5
    print(a)# This is local varrialbe.

a = 2 # This is global variable .
print(a)
fun()
print(a)