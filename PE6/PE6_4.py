current_users = ["gilbert", "jonathan", "nathaniel", "volkanovski","merab"]
username = input("Enter your username:")

if username.upper() in [x.upper() for x in current_users]:
    print("Sorry, " + username + ", is already taken")
    print(current_users)
else:
    print("Great, " + username + ", is available")