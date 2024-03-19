#A 
#fruits = ["apple", "banana", "cherry"]
#for item in fruits
# print(item)

#Fixed:
fruits = ["apple", "banana", "cherry"]
for item in fruits:
 print(item)
#The mistake was the lack of a semi-colon in the for loop

#B 
# for i in range (1, 4):
#print(i + '\t' + 2**i)
 
 #Fixed Code:
for i in range (1, 4):
    print(str(i) + '\t' + str(2**i))
#Needed to convert i and 2**i into string values before trying to concantenate
    

#C 
#Why is there no output when you run the code?
#for j in range (1, 6, -1):
#print(j)

#This printed nothing because the range function is telling the loop to go from 1 through 6 but is telling it to go by -1. This would cause the function to go to 0 from 1 which is invalid. It is out of the bounds of the function
    



#D 
#How to display all the elements in uppercase?
#letters = ['a', 'b', 'c']
#for letter in letters:
# letter = letter.upper()
#print(letters)

#Fixed Code:

letters = ['a', 'b', 'c']
for letter in letters:
    letter = letter.upper()
    print(letter) #The mistake was that the function was calling the list "letters" but modifying the variable "letter".



#E 
#fruits = ('apple', 'banana', 'cherry')
#print(fruits)
#fruits[0] = 'orange'
#fruits.append('pineapple')
#print(fruits)
    
fruits = ['apple', 'banana', 'cherry']
print(fruits)
fruits[0] = 'orange'  
fruits.append('pineapple') 
print(fruits)
#The error was that fruits was defined as a tuple. Since tuples are immutable, the first element of fruits could not have been assigned to "orange" and the .append() variable was not usable

