class people:
    def __init__(self,n,a,c=None):
        self.name=n
        self.age=a
        self.city=c
    def print_deta(self):
        print(f'Name: {self.name}\nAge: {self.age}')
        if self.city!=None:
            print("City :",self.city)
            
p1=people(input('Enter Name: '),int(input('Enter Age: ')))
p2=people(input('Enter Name: '),int(input('Enter Age: ')),input('Enter City: '))
p1.print_deta()
p2.print_deta()