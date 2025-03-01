price = float(input("Enter the price of the item: Rs. "))

if price >= 500:
    discount = 10 / 100 * price
    print("You got a discount of Rs.", discount)
    price = price - discount

print("Amount to Pay: Rs.", price)