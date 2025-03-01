from sqlite3 import *

person_id = int(input("Enter person id: "))

con = connect("persons.db")

cur = con.cursor()
cur.execute("select * from Person where Id = ?", (person_id,))

person = cur.fetchone()

con.close()

print(person)

if person is not None:
    print("Id:", person[0])
    print("Name:", person[1])
    print("Age:", person[2])
    print("City:", person[3])
else:
    print("Person of id", person_id, 'does not exist')