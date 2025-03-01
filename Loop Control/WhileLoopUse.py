s, c = 0, 0

while c < 5:
    n = int(input("Enter a number: "))

    if n > 0:
        c = c + 1
        s = s + n

    print("No of non-zero positive numbers entered:", c)
    print("No of remaining non-zero positive numbers:", 5 - c)

print("Sum:", s)