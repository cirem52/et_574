#4_2
#a) Create an empty list called n.
n=[]
#b Add 2 and 4 into the list. use append method
n.extend([2,4])
print(n)
#d)Add 0, 1 and 3 in proper order.
n.insert(0,0) #0 is inserted to the list in first position
n.insert (1,1) #1 is added to the list in second position
n.insert (3,3) #3 is added to the list in third position
print (n)
#f) Add 5 in proper order.
n.append(5)
print(n)
#h) Remove 0 from the list.
n.remove(0)
#i print the list
print (n)
#j Remove and print 2 from the list.
var1 = n.pop(1)
print(var1)
print (n)
#l) Remove and print 4 from the list.
var2 = n.pop(2)
print(n)
#n) Add all the removed numbers and print the sum.
print(var1+var2)
#o) Change the first item to 100 and last item to 9.9.
n.remove(1)
n.insert(0,100)
n.remove(5)
n.insert(4,9.9)
print (n)
#Copy the list n to a newNum list.
newNum=list(n)
#q) Clear the list n.
n.clear()
#r) Print the original list, n and the newNum list.
print (n, newNum)
#s) Delete the list n.
del n


