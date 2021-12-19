import re 

# regular expression for email
email_regex = r"[\w+\d]+@\w+\.\w+"

# email validator function
# matches the written regex with given email address
def email_validator(email):
    if re.fullmatch(email_regex,email):
        return True
    else:
        return False

# taking user email address
email = input()
flag = email_validator(email)

# output 
if flag:
    print("OK")
else:
    print("WRONG")



# By Sina Kazemi
# https://github.com/sina96n