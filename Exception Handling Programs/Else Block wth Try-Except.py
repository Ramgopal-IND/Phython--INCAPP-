try:
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))
    r = n1 / n2
except Exception:
    print("Something went wrong")
else:
    print("Result:", r)
print("Hello")