price = float(input("Enter the price of the item: Rs. "))
if price >=1000:
    discound = 25 / 100* price 
elif price >= 500:
    discound = 10 / 100 * price 
else :
    discound = 10 / 100 * price   

print ("You got a discound of Rs .",discound)  
price -= discound
print ("Amound to Pay : Rs. " , price ) 
