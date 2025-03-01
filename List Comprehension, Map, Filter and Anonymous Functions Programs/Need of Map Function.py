def square(n):
    return n ** 2

numbers = [1, 2, 3, 4, 5]
squares_numbers = []

for number in numbers:
    squares_numbers.append(square(number))

print(squares_numbers)
