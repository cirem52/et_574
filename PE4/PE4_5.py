name = input("Please enter your full name:")

name_list = name.split()
#splits user input into words and assigns them to the list "name_list"
print("First name:" + name_list[0])
print("Last name:" + name_list[-1])
#calls the first element of name_list for the first name and the last element of name_list for the last name