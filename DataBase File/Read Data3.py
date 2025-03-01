from sqlite3 import *

con = connect("persons.db")

cur = con.cursor()
cur.execute("select * from Person")

persons = cur.fetchmany(3)

con.close()

print(persons)

for person in persons:
    print(person)
    print("Id:", person[0])
    print("Name:", person[1])
    print("Age:", person[2])
    print("City:", person[3])
    



