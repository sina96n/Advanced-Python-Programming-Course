import mysql.connector as mysql
import re

# regular expression for compiling email address
regex = r"[\w\d]+@\w+.\w+"

# creating email validator function
def eamil_validator(email):
    if re.fullmatch(regex, email):
        return True
    else:
        return False 

# creating password validator function
def password_validator(password):
    if not (password == "") or (len(password) < 8):
        return True
    else:
        return False

# taking email from user
email = input()
# checking the eamil
email_flag = eamil_validator(email)

if email_flag:
    # taking password if the email is true
    password = input()
    pass_flag = password_validator(password)

    if pass_flag:
        # saving into database if the given information is true
        # creating connection to the database
        con = mysql.connect(
            user="username",
            password="password",
            database="users"
        )
        # creating a cursor
        cur = con.cursor()
        # writing query to save the data
        query = "insert into userinfo(username, password) values('{}','{}')".format(email, password)
        cur.execute(query)
        
        # applying changes and closing connection
        con.commit()
        con.close()

    else:
        "invalid password"
        print('invalid password')

else:
    # invalid email address
    print('''invalid E-mail address. your email address should match thos form:
    expression@string.string''')




# By Sina Kazemi
# https://github.com/sina96n