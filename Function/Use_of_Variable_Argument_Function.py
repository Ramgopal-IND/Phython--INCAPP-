def add(*numbers):
    s = 0
    for n in numbers:
        s += n
    return s

print(add(10, 20, 30))
print(add(10, 20))
print(add(10, 20, 30, 40, 50)) # Not error because *number is variable argument function.