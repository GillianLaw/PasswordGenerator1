import random
import sqlite3

"""A password generator and a database of the passwords created"""

website = input("Which site is this for? ")

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!”#$%&'()*+,-./:;<=>?@[]^_`{|}~"

"""A lot of sites request a password with all four of these, so I want to make
sure each password has each type of character"""

p1 = "".join(random.sample(lower, 2))
p2 = "".join(random.sample(upper, 2))
p3 = "".join(random.sample(numbers, 3))
p4 = "".join(random.sample(symbols, 3))

"""Add these together in a string and then randomise again."""
all = p1 + p2 + p3 + p4

random_password = "".join(random.sample(all, 10))

print("Your password for {} is {}".format(website, random_password))

"""Store the passwords in a database"""

db = sqlite3.connect('passwords.sqlite')
db.execute("CREATE TABLE IF NOT EXISTS passwords (name TEXT, password TEXT)")
db.execute("INSERT INTO passwords (name, password) VALUES (?, ?)", (website, random_password))

update_sql = "SELECT * FROM passwords"
cursor = db.cursor()
cursor.execute(update_sql)

cursor.connection.commit()
cursor.close()

"""Print the sites and passwords. I should really move this to another file, as it will
create a really long list soon!"""

for name, password in db.execute("SELECT * FROM passwords"):
    print(name)
    print(password)
    print("-" * 20)

db.close()
