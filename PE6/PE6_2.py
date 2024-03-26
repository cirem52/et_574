age = 17
if age < 0:
    print("Error: Invalid Age")
elif age < 2:
    print("You are a baby")
elif age >= 2 and age < 4:
    print("You are a toddler")
elif age >= 4 and age < 13:
    print("You are a kid")
elif age >= 13 and age <20:
    print("You are a teenager")
elif age >= 20 and age < 65:
    print("You are an adult")
elif age >= 65:
    print("You are an elder")

#Each if and elif statement checks if the age variable is within a certain range and prints a statement to the console