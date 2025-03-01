class people:
    def __init__(self,name,age,city=None):
        self.name=name
        self.age=age
        self.city=city
    def print_deta(self):
        print(f'Name: {self.name}\nAge: {self.age}\nCity: {self.city}')
p1=people(input('Enter Name: '),int(input('Enter Age: ')))
p2=people(input('Enter Name: '),int(input('Enter Age: ')),input('Enter City: '))
p1.print_deta()
p2.print_deta()