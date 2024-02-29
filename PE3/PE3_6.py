#A phoneNum = 718-710-4756
#print("QCC phone number is " + phoneNum + '.')
#Debug
phoneNum = "718-710-4756"
print("QCC phone number is " + phoneNum + '.')
#Initially the variable phoneNum was was in the integer data type and could not be concatenated with a str data type. After putting quotation marks around the number when defining the variable, the variable changed to a str data type and was able to be combined with "QCC phone number is" in the print statement. 



#B finally = "happily ever after."
#print("They lived " + finally)
#Debug

newVariable = "happily ever after."
print("They lived " + newVariable)
#The word "finally" cannot be used as a variable name since it is also used as syntax for code. Changing the variable name to another valid name fixes this issue. 



#C age = 20
#print("I am " + age + " years old.")
#Debug

age = "20"
print("I am " + age + " years old.")
#String concatenation cannot be done with an int data type so changing the data type of the variable "age" to str fixes this issue.

#D age = input("Enter your age: ")
#print("Next year you will be " + (age+1))
age = input("Enter your age: ")
int(age)
1 =+ age 
print("Next year you will be " + str(age)