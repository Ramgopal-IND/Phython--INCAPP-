price = float(input("Enter The price of the item : Rs. ") )

if price >=500:
    discount = 10/100 * price 
else :
    discount = 5/100 * price    
print ("You got  discount of Rs: " ,discount)
price -=discount 
print ("Amound to pay : Rs.",price)
