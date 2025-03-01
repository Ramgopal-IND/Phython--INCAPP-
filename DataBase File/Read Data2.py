from sqlite3 import *

con = connect("persons.db")

cur = con.cursor()
cur.execute("select * from Person")

persons = cur.fetchall()

con.close()

print("------------------------------------------------------")
print("Id\tName\t\tAge\tCity")
print("------------------------------------------------------")
for person in persons:
    print(person[0], "\t", person[1], "\t", person[2], "\t", person[3])
print("------------------------------------------------------")
