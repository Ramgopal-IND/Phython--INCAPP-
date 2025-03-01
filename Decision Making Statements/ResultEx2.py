Sub1=float(input("Enter the marks of the first subject :"))
Sub2=float(input("Enter the marks of the second  subject :"))
Sub3=float(input("Enter the marks of the third  subject :"))
T= Sub1 + Sub2 + Sub3
print ("Total Of marks :",T)
P=T/300 * 100
print ("Percentage Of Marks :",round (P,2))
if P>=33:
    print("You Are Pass")
else:
    print ("You Are Fail")    