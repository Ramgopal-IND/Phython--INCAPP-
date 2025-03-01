try:
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))
    r = n1 / n2
    print("Result:", r)
except ValueError:
    print("Not a number")
except ZeroDivisionError:
    print("Can't divide by zero")
except Exception:
    print("Something went wrong")
print("Hello")