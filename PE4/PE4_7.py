#A
#myList = ['apple','banana','cherry']
#print(myList[3])

#Fixed:
myList = ['apple','banana','cherry']
print(myList[2])
#The mistake with this code was that the print function was calling for the fourth item in the list "myList" which does not exist. In order to refer to the third item in the list, the number 2 needs to be used since the first item in the list is indexed with 0

#B 
print(myList[-1:-4])
#In order to be included, an element must be at or to the right of the start position and to the left of the stop position.
#Fixed:
print(myList[-3:])

#C 
word = 'sea'
#word[0] = 'p'
#Indexing cannot be used to alter a string. Also, strings are immutable. Since this line tries to do these things, it fails.
print(word)
#Fixed:
wordList = list(word)
print(wordList)
wordList[0] = "p"
print(wordList)
print("".join(wordList))

#D 
#n = [1, "two", 'three', 4]
#print(" ".join(n))
#This does not work because the list n has both int data types and str data types. All the data types must be string for .join to work.
#Fixed:
n = ["1", "two", 'three', "4"]
print(" ".join(n))