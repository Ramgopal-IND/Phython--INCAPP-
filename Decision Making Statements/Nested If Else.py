m1=int (input ("Enter the marks of the first subject :"))
m2=int (input ("Enter the marks of the second subject :"))
m3=int (input ("Enter the marks of the third subject :"))
T = m1 + m2 + m3 
print ("Total of marks :",T)
P = T/300 * 100
print ("Percentage of marks :",round (P,2))
if P >=30:
    print ("You are pass")
    if P>=60:
        print ("You are first class")
    elif P>=45:
        print ("You are second class")
    else :
        print ("You are third class ")

else :
    print ("You are fail") 
    print ("Better luck next time")       