#Validated User Details
#username not more than 12 characters
#username must not contain any spaces
#username must not contain number
valid= False;
username = input("Enter your username: ")
if len(username) > 12:
    print("Username must not be more than 12 characters.")
elif " " in username:
    print("Username must not contain any spaces.")
elif any(char.isdigit() for char in username):
    print("Username must not contain numbers.")
else:
    print("Username is valid.")
    valid = True
    if valid:# Password validation
        password = input("Enter your password: ")
        if len(password) < 8:
            print("Password must be at least 8 characters long.")