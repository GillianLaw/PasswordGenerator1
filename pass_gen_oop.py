import random
import sqlite3
import string

"""An attempt to rewrite the password generator using oop principles"""

def create_password(passwordlength):

    """I know I could use 'string.ascii_letters + string.punctuation'
    but I want to ensure there is some of each type in each password.
    I've chosen (for the moment) to make each password 10 digits long
    rather than offer a choice"""

    p1 = "".join(random.sample(string.ascii_lowercase, 2))
    p2 = "".join(random.sample(string.ascii_uppercase, 2))
    p3 = "".join(random.sample(string.digits, 3))
    p4 = "".join(random.sample(string.punctuation, 3))

    """Add these together in a string and then randomise again.
    I don't want a password that is lower case first, then upper, etc"""

    all = p1 + p2 + p3 + p4

    random_password = "".join(random.sample(all, passwordlength))#TODO consider offering choice of length
    return random_password

#TODO the database stuff isn;t working...
# def save_to_db():
#     db = sqlite3.connect('passwords1.sqlite')
#     db.execute("CREATE TABLE IF NOT EXISTS passwordsOOP (name TEXT, password TEXT)")
#     db.execute("INSERT INTO passwordsOOP (name, password) VALUES (?, ?)", (main.website, main.password))
#
#     update_sql = "SELECT * FROM passwordsOOP"
#     cursor = db.cursor()
#     cursor.execute(update_sql)
#
#     cursor.connection.commit()
#     cursor.close()
#     db.close()

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

    # save_to_db()

run = True
while run:
    try:
        main()
    except KeyboardInterrupt:
        run = False
        print('Ctrl+c caught exiting')
