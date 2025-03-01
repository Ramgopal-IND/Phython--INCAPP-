from sqlite3 import *

person_id = int(input("Enter the id: "))

con = connect("peoples.db")

cur = con.cursor()
cur.execute("delete from people where Id = ?", (id,))
con.commit()

con.close()

print("Person details are deleted successfully")