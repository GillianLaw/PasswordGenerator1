import random
import sqlite3
import string

"""An attempt to rewrite the password generator using oop principles"""
# def passwordlength():
#     length = 0
#     while 6 < length < 10:
#         try:
#             n = int(input('Enter your password length (minimum 6, maximum 10): '))
#         except ValueError:
#             print('Not a number')
#     return length


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


def main():
    website = input("Which site is this for? ")
    passwordlength = int(input("How many characters (min 6, max 10)? "))


    password = create_password(passwordlength)

    print('Generated password for {}: {}'.format(website, password))

run = True
while run:
    try:
        main()
    except KeyboardInterrupt:
        run = False
        print('Ctrl+c caught exiting')
