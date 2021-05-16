import random
import sqlite3
import string

"""An attempt to rewrite the password generator using oop principles"""

def create_password(passwordlength):

    p1 = "".join(random.sample(string.ascii_lowercase, 2))
    p2 = "".join(random.sample(string.ascii_uppercase, 2))
    p3 = "".join(random.sample(string.digits, 3))
    p4 = "".join(random.sample(string.punctuation, 3))

# Add these together then randomise again.
# Don't want a password lower case first, then upper, etc

    all = p1 + p2 + p3 + p4

    random_password = "".join(random.sample(all, passwordlength))
    return random_password


def save_to_db(website, password):
    db = sqlite3.connect('passwordOOP.sqlite')
    db.execute("CREATE TABLE IF NOT EXISTS passwordOOP (name TEXT, pass TEXT)")
    db.execute("INSERT INTO passwordOOP (name, pass) VALUES (?, ?)", (website, password))

    update_sql = "SELECT * FROM passwordOOP"
    cursor = db.cursor()
    cursor.execute(update_sql)

    cursor.connection.commit()
    cursor.close()
    db.close()


def main():
    website = input("Which site is this for? ")
    passwordlength = int(input("How many characters (min 6, max 10)? "))
    # TODO the below should prob be in a sep function
    if 5 < passwordlength < 10:
        length = passwordlength
    else:
        length = 10
        print("Password must be between 6 and 10 characters. I have given you 8.")


    password = create_password(length)
    print('Generated password for {}: {}'.format(website, password))

    save_to_db(website, password)
    # working!!

experiment = main()
print(experiment)
