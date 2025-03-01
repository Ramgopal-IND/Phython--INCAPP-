from sqlite3 import *

person_id = int(input("Enter the id: "))
name = input("Enter the new name: ")
age = int(input("Enter the new age: "))
city = input("Enter the new city: ")

con = connect("persons.db")

cur = con.cursor()
cur.execute("update Person set name = ?, age = ?, city = ? where Id = ?",
(name, age, city, person_id))
con.commit()

con.close()

print("Person details are updated successfully")