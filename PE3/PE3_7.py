#A 
str0 = "py"
print(str0[0])
print(str0[-1])
print(str0[:])
print(str0[0], str0[-1],
str0[:], sep = ' ')
#These are all uses of indexing in a variable with string data. 0 refers to the first character in the string, -1 refers to the last, and the colon prints the whole string. The last print statement combines all of these elements into one print statement and uses the "sep" argument to give spaces between the outputs. 

#B
print('C'[0])
print("C"[-1])
print('C'[:])
print('C'[0], 'C'[-1],
'C'[:], sep = '\t')
#This code does the same thing as example A but since the string being used in this is only 1 character long it all results in the same character.

#C
str1 = "coDE"
print(str1.capitalize()+'\n'+str1.upper()+'\n'+str1.lower())
print(str1)
#This shows various functions being called on the str1 variable. The .capitalize function capitilizes the first letter of the word. The .upper capitilizes every character in the string. And the .lower lowercases every character in the string.

#D
str2 = "computer science"
print(str2.title(),'|',str2[0:8],'|',str2[:3],'|',
str2[-5:-1], '|', str2[-2:] )
print(str2.title(), str2[0:8], str2[:3],
str2[-5:-1], str2[-2:], sep = ' | ')
#This example prints the variable "str2" which holds the string "computer science" and prints various indexes of the string. The indexes are called by using the following format: a:b where a is an inclusive integer and b is an exclusive integer. If the integers are positive, the indexing is done from left to right but if they are negative the indexing is done right to left. 

#E
str3 = "mississippi"
print("i =",str3.count('i'))
print("s = index[", str3.find('s'), ']')
print('p = ', str3.rfind('p'))
print("Miss = ", str3.find("Miss"))
#This example demonstrates the .count, .find, and .rfind functions. The .count function counts how many instances of a specific character is used in a string. The .find function finds the first instance of a specified character from left to right and outputs its index. The .rfind function does the same thing but goes from right to left. The last statement shows that the .find function can also be used to find groups of characters in a string and outputs the position of the specified group of characters. The function is case sensitive and since "mississippi" is not capitalized, it outputs "-1" meaning there are no instances of "Miss" in the string.

#F
str4 = "  Today's program  "
print('lstrip():',str4.lstrip())
print('rstrip():',str4.rstrip())
print('strip():',str4.strip() + " – Basic IO")
#The strip function removes any whitespaces in a string. lstrip removes white spaces towards the left of the string and rstrip removes whitespaces to the right of the string.

#G
print("Price: ", '$', 19.99)
print("Price: ", '$', 19.99, sep = '')
#the sep argument specifies what should be in between the parameters of the print function. In the second example, the space between the parameters is removed and results in a better-looking output.

#H
print('Py', 'th', 'on', sep = '')
print('Py', 'th', 'on', sep = '\t')
print('Py', 'th', 'on', sep = '\n')
#This example shows more uses of the sep parameter. The first example prints the arguments of the print function without a space resulting in the word python, the second puts tab spaces between each argument, and the last creates a new line between each argument.

#I
print('tic', 'tac', 'toe', sep = '-', end = ' ')
print("game starts", end = '!\n')
print('in'.title(), 'person'.capitalize(), sep = '-', end = ' ')
print('tutoring'.upper())
#The first and second print statements are printed in one line since the end parameter is "\n" by default. Since that is changed, both the print statements are on the same line. The third and fourth print statements show .title, .capitalize, sep, and, end in use. .title capitalizes the first letter of each word while lowercasing the other letters. .capitalize capitalizes the first letter of the string while lowercasing the rest of the characters. .upper uppercases all the characters.

#J
print("Number\tSquare")
print(str(2) + '\t' + str(2**2))
print(str(3) + '\t' + str(3**2))
print(2, '\t', 2**2)
print(3, '\t', 3**2)
#The second and third print statements uses the str() function to turn the result of the exponent operations into a string data type so they can be concantanated. 

#K
print("STATE\tCAPITAL".expandtabs(15))
print('North Dakota\tBismarck'.expandtabs(15))
print('South Dakota\tPierre'.expandtabs(15))
print('Ohio\tColumbus'.expandtabs(15))
print('North Dakota\tBismarck')
print('South Dakota\tPierre')
print('Ohio\tColumbus') 
#the .expandtabs() parameter specifies how many spaces should be used when a tab space is called.

