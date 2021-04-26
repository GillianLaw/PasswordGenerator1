import sqlite3

db = sqlite3.connect('passwords.sqlite')

search = input("Which site are you looking for? ")
for row in db.execute("SELECT * FROM passwords WHERE name = ?", (search,)):
    print(row)

# for name, password in db.execute("SELECT * FROM passwords"):
#     print(name)
#     print(password)
#     print("-" * 20)


db.close()
