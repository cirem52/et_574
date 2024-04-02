value = input("Enter an integer and I will tell you if it is a multiple of ten: ")

if int(value) % 10 == 0:
    print(value + " is a multiple of ten")
else:
    print(value + " is not a multiple of ten")