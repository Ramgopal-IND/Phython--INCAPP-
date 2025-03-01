class people:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    def print_details(self):
        print("-----------------------------")
        print("Name :",self.name)
        print("Age :",self.age)
        print("Gender :",self.gender)    
        print("-----------------------------")

print("If You can enter the details of the people and print so type 'Yes' otherwise type 'No' .")
i=0
while True:
    if i==0:
        ch=input("Enter your choice :")
    print()

    if ch=='Yes' or ch=='yes' or ch=='YES':
        P=people(input("Enter Name :"),int(input("Enter Age :")),input("Enter Gender (☉ Male , ☉ Female) :"))  
        P.print_details()
        i+=1
        print("You are entered ",i," Person details successfully.")
        print("If you want to enter the details again type 'Yes' otherwise type 'No' .")
        ch=input("Enter your choice :")
        if ch=='No' or ch=='no' or ch=='NO':
            print("Thank You For Using This Application ❤️ . And Returned To Service Once Again.")
            break

    elif ch=='No':
        break    

    else:
        print("Invalid choice entered")
        