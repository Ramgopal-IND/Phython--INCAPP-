from sqlite3 import *

name = input("Enter the name: ")
age = int(input("Enter the age: "))
city = input("Enter the city: ")

con = connect("persons.db")

cur = con.cursor()
cur.execute("insert into Person(name, age, city) values(?, ?, ?)", (name, age, city))
con.commit()

con.close()

print("Person details are saved successfully")