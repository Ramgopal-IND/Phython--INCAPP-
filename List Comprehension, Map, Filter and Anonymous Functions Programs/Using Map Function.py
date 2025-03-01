def square(n):
    return n ** 2

numbers = [1, 2, 3, 4, 5]

squares_numbers = list(map(square, numbers))

print(squares_numbers)