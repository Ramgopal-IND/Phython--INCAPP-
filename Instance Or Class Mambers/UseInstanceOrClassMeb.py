class Employee:
    company_name, company_address = "", ""

    def __init__(self, employee_id, name, salary):
        self.employee_id = employee_id
        self.name = name
        self.salary = salary

    def print_details(self):
        n=0
        if (n==1):
           print("--------------------------")
        n=1
        print(" ")
        print("Employee Id:", self.employee_id)
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Company Name:", self.company_name)
        print("Company Address:", Employee.company_address)
        print("--------------------------")

    @classmethod
    def set_company_details(cls, company_name, company_address):
        cls.company_name = company_name
        cls.company_address = company_address

    def change_salary(self, new_salary):
        self.salary = new_salary

    @classmethod
    def change_company_address(cls, new_company_address):
        cls.company_address = new_company_address

print("--------------------------")
Employee.set_company_details(input("Enter Company Name :"), input("Enter City Name :"))
print("--------------------------")
e1 = Employee(int(input("Enter Employee ID :")), input("Enter Employee Name :"), int (input("Enter Employee Salary :")))
print("--------------------------")
print("--------------------------")
e2 = Employee(int(input("Enter Employee ID :")), input("Enter Employee Name :"), int (input("Enter Employee Salary :")))
print("--------------------------")
print(" ")
print("      -: Employee Detaails :-     ")
e1.print_details()
e2.print_details()
e1.change_salary(24250)
e2.change_company_address("Pune")
e1.print_details()
e2.print_details()
    
        
        