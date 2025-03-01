numbers = [12, 2, 3, 23, 34]
even_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

print(even_numbers)