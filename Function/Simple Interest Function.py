def simple_Interest(P,R,T):
    return(P*R*T)/100

P=float(input ("Enter The Principle Amound :"))
R=float(input("Enter The Rate of Interest :"))
T=float(input ("Enter The Time Period (Year) : "))
print ("Simple Interest is :",simple_Interest(P,R,T))