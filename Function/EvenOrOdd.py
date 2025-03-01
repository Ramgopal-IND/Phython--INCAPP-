#Pro Type Code for Even or Odd
def find_even_odd(num):
    if num%2==0:
        return "Even(True)"
    else:
        return"Odd(Fales)"

print("Num is :",find_even_odd(num=int(input("Enter a number:"))))    


#Normal Type Code for Even or Odd
def find_even_odd(num):
    if num%2==0:
        return"Even"
    else:
        return"Odd"
    

#num=int(input("Enter anumber:"))
Find=find_even_odd(num=int(input("Enter a number:")))
print("Num is :",Find)  



