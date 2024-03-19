#asking for values
multiples = input("Enter a range: ")
number = input("Enter an integer number: ")

#turns the str into int
multiples = int(multiples)
number = int(number)

for x in range(1, multiples+1): #iterates through the range given by the user + 1 (since this is exclusive)
    print(str(x) + "\t" + "*" + "\t" + str(number) + "\t" + "=" + "\t" + str(x*number))