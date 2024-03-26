usernames = ["admin", "jonathan", "gilbert", "jon", "alex"]

if usernames:
    for x in usernames:
        if x != "admin":
            print("Hello, " + x + ", thank you for logging in again!")
        elif x == "admin":
            print("Hello Admin, would you like to see a status report?")
else:
    print("We need to find more users")       
    