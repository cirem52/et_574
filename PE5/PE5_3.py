multiples = [x*4 for x in range(0,11)] #multiples of 4 between 0 to 10
i = []
i = [x/2 for x in multiples] #adding all elements of the first list into a second, empty list, and dividing by 2 before entering them into the second list.
print(i)
#copying second list into a third list
a = i[:]
print(a)
#dividing each element of list a by two. resulting in a list of numbers from 1-10
a = [x/2 for x in a]
print(a)