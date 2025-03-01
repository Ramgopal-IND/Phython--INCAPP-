contacts = {'+91-9811234522' : "Vijay Verma", "+91-8823114567" : 'Mahima Gupta'}
print(type(contacts))
print(contacts)
print(contacts["+91-8823114567"])
contacts["+91-7911234533"] = 'Manoj Pandey'
print(contacts)
contacts["+91-9811234522"] = 'Pankaj Mishra'
print(contacts)
for phone_number in contacts:
    print(phone_number, ":->", contacts[phone_number])
del contacts['+91-9811234522']
print(contacts)
print("+91-9811234522" in contacts)
print("+91-8823114567" in contacts)
print("+91-9811234522" not in contacts)
print("+91-7911234533" not in contacts)