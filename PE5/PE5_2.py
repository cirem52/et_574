#a) Use a list comprehension to generate a list of all even numbers from 0 to 100 inclusive.
#b) Use slicing to print the first five even numbers in the list.
#c) Use slicing to print the last five even numbers in the list.
#d) Use slicing to print all list numbers between 20 and 30 inclusive.
even_numbers = [x for x in range(0,101,2)]
print(even_numbers[0:6]) #first 5 even numbers
print(even_numbers[-5:]) #last 5 even numbers
print(even_numbers[10:16]) #even numbers between 20 and thirty