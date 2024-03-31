#A 
#n = eval(input("Enter a number: "))
#if n = 7:
# print("The square is", n*2)
    #Fixed Code
n = eval(input("Enter a number: "))
if n == 7:  #This was missing another equal sign. Two equal signs are used to check if two values are identical, one is used to asign value.
 print("The square is", n**2)   #This used only 1 multiplication symbol which resulted in 7 * 2 = 14. Instead, two * symbols should be used to raise seven to the second power.

#B 
#n = 6
#if n > 5 and < 9:
#    print("Yes")
#else:
#    print("No")
    #Fixed Code:
 n = 6
if n > 5 and n < 9: #The second part of the and statement was incomplete and needed an "n"
    print("Yes")
else:
    print("No")

#C 
#major = "Computer Science"
#if major == "Engineering Technology" Or "Computer Technology")
#print("Yes")
    #Fixed Code
major = "Computer Science"
if major == "Engineering Technology" or "Computer Technology": #the "or" logical operator was capitalized which is the wrong way of writing it. Also, there was a closing parenthesis that was misplaced.
    print("Yes")

#D 
#a, b = 1, 1.0
#if a = b:
#    print("same")
    #Fixed Code
a, b = 1, 1.0
if a == b:
    print("same")



