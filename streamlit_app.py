import streamlit as st
import random
import sqlite3
import string

st.write("Gillian's password generator")

import streamlit as st
import sqlite3
import random
import string

def create_password(passwordlength):
    p1 = "".join(random.sample(string.ascii_lowercase, 2))
    p2 = "".join(random.sample(string.ascii_uppercase, 2))
    p3 = "".join(random.sample(string.digits, 3))
    p4 = "".join(random.sample(string.punctuation, 3))

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

def search_db(search):
    db = sqlite3.connect('passwordOOP.sqlite')
    for row in db.execute("SELECT * FROM passwordOOP WHERE name LIKE ?", (search,)):
        st.write(row)
    db.close()

def main():
    website = st.text_input("Which site is this for?")
    passwordlength = st.number_input("How many characters (min 6, max 10)?", min_value=6, max_value=10, value=8, step=1)

    if st.button('Generate Password'):
        if 5 < passwordlength < 10:
            length = passwordlength
        else:
            length = 10
            st.write("Password must be between 6 and 10 characters. I have given you 8.")

        password = create_password(length)
        st.write('Generated password for {}: {}'.format(website, password))

        save_to_db(website, password)

    search = st.text_input("Which site are you looking for?")
    if st.button('Search Passwords'):
        search_db(search)

if __name__ == "__main__":
    main()
    
#####
# def create_password(passwordlength):
#     p1 = "".join(random.sample(string.ascii_lowercase, 2))
#     p2 = "".join(random.sample(string.ascii_uppercase, 2))
#     p3 = "".join(random.sample(string.digits, 3))
#     p4 = "".join(random.sample(string.punctuation, 3))

#     all = p1 + p2 + p3 + p4

#     random_password = "".join(random.sample(all, passwordlength))
#     return random_password

# def save_to_db(website, password):
#     db = sqlite3.connect('passwordOOP.sqlite')
#     db.execute("CREATE TABLE IF NOT EXISTS passwordOOP (name TEXT, pass TEXT)")
#     db.execute("INSERT INTO passwordOOP (name, pass) VALUES (?, ?)", (website, password))

#     update_sql = "SELECT * FROM passwordOOP"
#     cursor = db.cursor()
#     cursor.execute(update_sql)

#     cursor.connection.commit()
#     cursor.close()
#     db.close()

# def main():
#     website = st.text_input("Which site is this for?")
#     passwordlength = st.number_input("How many characters (min 6, max 10)?", min_value=6, max_value=10, value=8, step=1)

#     if st.button('Generate Password'):
#         if 5 < passwordlength < 10:
#             length = passwordlength
#         else:
#             length = 10
#             st.write("Password must be between 6 and 10 characters. I have given you 8.")

#         password = create_password(length)
#         st.write('Generated password for {}: {}'.format(website, password))

#         save_to_db(website, password)

# if __name__ == "__main__":
#     main()


