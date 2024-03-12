#A 
a = list(range(5))
print(a)
#output:
#[0, 1, 2, 3, 4]

#B 
b = []
for i in range (5):
 b.append(i)
print(b)
#output:
#[0, 1, 2, 3, 4]

#C 
x = list(range(-10, 10))
print(x)
print(min(x), max(x), sum(x))
#[-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9] <- result of print(x)
#-10 9 -10 <- result of min and max

#D 
even_num = list(range(2, 11, 2))
print(even_num[0], even_num[-1])
#2 10

#E - Print all the odd numbers from 1 to 9 inclusive in a list, odd_num.
odd_num = list(range(1,10,2))
#starts at 1 and jumps by 2 until it reaches 9.
print(odd_num)

#F - Make a list of the first 10 cubes and use a for loop to print out the value of each cube in a new line (see output below).
cubes = []
for i in range(1,11):
    cubes.append(i**3)
    #takes each value in range and cubes it then adds it to the empty list "cube"
    print(i**3)
print(cubes)

#G - Use a list comprehension to generate a list of the first 10 cubes. Use a for loop to print out the value of each cube in a row separated by a ‘|’ (see output below).
cubes_2 = []
cubes_2 = [x**3 for x in range(1,11)] #assigns cubes_2 to each value from range after cubing it.
print(cubes_2)
for x in cubes_2:
   print(x,end="|") # prints each value in cubes with "|" as the end character instead of creating a newline everytime it prints.


