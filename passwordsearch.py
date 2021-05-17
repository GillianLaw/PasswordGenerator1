import sqlite3

def lookup():
    db = sqlite3.connect('passwordOOP.sqlite')

    search = input("Which site are you looking for? ")
    for row in db.execute("SELECT * FROM passwordOOP WHERE name LIKE ?", (search,)):
        # print(row)
        print("The password for {} is {}".format(row[0], row[1]))

    # for name, password in db.execute("SELECT * FROM passwords"):
    #     print(name)
    #     print(password)
    #     print("-" * 20)
    # print("The password for {} is {}".format(row[0], row[1]))

    db.close()

hunt = lookup()
print(hunt)

# Now need to work on GUI
