#1
for i in range(3):
    for j in range(4):
        print("*", end = "")
    print()



print()
#2
st = 1
for i in range(3):
    for j in range(st):
        print("*", end = "")
    print()
    st += 1



print()
#3
sp, st = 2, 1
for i in range(3):
    for j in range(sp):
        print(end = " ")
    for k in range(st):
        print(end = "*")
    print()
    sp -= 1
    st += 1


print()
#4
sp,st=4,1
for i in range (5):
    for j in range (sp):
        print (end=" ")
    for a in range (st):
        print(end= "*")    
    print ()
    sp -=1
    st +=2  



print()
#5 
sp,st=4,1
for i in range (8):
    for j in range (sp):
        print (end=" ")
    for a in range (st):
        print(end= "*")    
    print ()
    if i<3:
        sp -=1
        st +=2  
    else:
        sp +=1
        st -=2  
   
   