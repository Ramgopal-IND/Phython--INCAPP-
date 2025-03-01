try:
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))
    r = n1 / n2
    print("Result:", r)
except Exception as e:
    print(e)    
print("Hello")