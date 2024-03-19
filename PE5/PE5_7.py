#A 
fruits = ["apple", "pear", 'python',]
for item in fruits:
 print(f"{item.title()} is my favorite!")
print(f"I want to have more {item}.\n")
#uses f string to concantenate the print statement with the elements of the list



#B 
numbers = [1,2,3,4,5]
for n in numbers:
    print(n)    #iterates through the list and prints the number the loop is on
    print("That’s all the numbers in the list.") #just a print statement
    print("numbers = ", numbers) #print statement that also prints the list "numbers"
    

#C 
n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
count = 0
for i in n:
    print(i, end = '\t')
    count += 1 #adds one to count for each time the function iterates through the list. this determines the number of items in the list
    print(f"\nThere are {count} numbers in the list.") # print statement with variable count
    print("n = ", n) #prints the whole list

#D 
languages = ["c++", "java", "python"]
for code in languages:
    print(code.upper(), end = " | ") #for each element in the languages list, capitalizes the element and prints it followed by space and |.
else:
    print("Enjoy coding!") # once it reaches the end of the list, it prints this statement.


#E 
n = -6, 7, 3, -2, 6, 3, 9
print(len(n), max(n), min(n), sum(n), sep = '\n') #prints the values of each function called and starts a new line after calling each function since the sepperator is set to "\n"
print(n.count(3), n.index(3), n[-6:6], sep = '\n') #determines the amount of times "3" is in the list (2), determines the index for the first instance of 3 (at index 2), and calls the list from -6 to 6 which produces the same thing as 1:7
print(n, sorted(n), sep = '\n') #prints the list then prints the list from least to greatest. also creates new line after each value since the sepperator is set to "\n"

#F 
a = 2
b = 3
print(type(a+b)) #a + b is equal to an integer; returns the data type "int"
print(type((a+b,))) #sets a+b as the first element of a tuple; returns the data type tuple
print(type(())) #creates an empty tuple; returns the data type tuple