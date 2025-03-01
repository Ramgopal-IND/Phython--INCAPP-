class Account:
    def __init__(self):
        self.account_number = int(input("Enter account number: "))
        self.name = input("Enter name: ")
        self.balance = 0

    def view_account_details(self):
        print("Account Number:", self.account_number)
        print("Name:", self.name)
        print("Balance:", self.balance)

    def deposit(self):
        amount = int(input("Enter amount to deposit: "))
        self.balance += amount
        print("Balance after deposit:", self.balance)

    def withdraw(self):
        if self.balance > 0:
            amount = int(input("Enter amount to withdraw: "))
            if amount <= self.balance:
                self.balance -= amount
                print("Balance after withdraw:", self.balance)
            else:
                print("Insufficient Balance")
        else:
            print("No Balance")

a = Account()

print("Account is created successfully")
print("Enter v to view account details")
print("Enter d to deposit an amount")
print("Enter w to withdraw an amount")
print("Enter e to exit")

while True:
    ch = input("Enter your choice: ")
    if ch == 'v':
        a.view_account_details()
    elif ch == 'd':
        a.deposit()
    elif ch == 'w':
        a.withdraw()
    elif ch == 'e':
        break
    else:
        print("Invalid choice entered")
    