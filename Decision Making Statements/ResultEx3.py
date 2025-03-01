m1 = int(input("Enter marks of first subject: "))
m2 = int(input("Enter marks of second subject: "))
m3 = int(input("Enter marks of third subject: "))
t = m1 + m2 + m3
print("Total of marks:", t)
p = t / 300 * 100
print("Percentage of marks:", round(p, 2))
if p >= 60:
    print("Result: First Division")
elif p >= 45:
    print("Result: Second Division")
elif p >= 33:
    print("Result: Third Division")
else:
    print ("Result: Fail")