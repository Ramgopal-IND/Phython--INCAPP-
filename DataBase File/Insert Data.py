from sqlite3 import *

con = connect("persons.db")

cur = con.cursor()
cur.execute("insert into Person(name, age, city) values('Pankaj Mishra', 22, 'Greater Noida')")
con.commit()

con.close()

print("Person details are saved successfully")