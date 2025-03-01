def iseven(n):
    return n % 2 == 0

numbers = [12, 2, 3, 23, 34]
even_numbers = []

for number in numbers:
    if iseven(number):
        even_numbers.append(number)

print(even_numbers)
