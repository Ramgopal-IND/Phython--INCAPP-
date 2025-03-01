#1
s = 0
for i in range(5):
    n = int(input("Enter a number: "))
    
    if n <= 0:
        continue
    
    s += n

print("Sum:", s)



#2
for i in range(1, 6):
    if i == 3:
        continue
    print(i)