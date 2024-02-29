#1a
print("012345678901234567890")
#This is printed as a string data type.
#Output: 012345678901234567890

print('A'.rjust(5), 'B'.center(5), 'C'.ljust(5), sep = "")
#In this statement, the methods .rjust, .center, and .ljust are used to justify the position characters A, B and C. Sep is also used to define the space between the characters. 
#Output:     A  B  C    

#1b
print("01234567890123456") 
#Prints the following number as a string
print("{0:^7}{1:4}{2:>6s}".format("one", "two", "three"))
print(f"{'one':^7}{'two':4}{'three':>6s}")
#The two statements above have the same result but show two different ways of formating the print statement. The firs tone uses the format() method and the second uses F-string.
#Output:
#01234567890123456
#  one  two  three
#  one  two  three 

#1c
n=1234
print("01234567890123456789")
print(f"{n:10}{n:^10}")
#Justifies the position of the first argument to have 10 spaces from the left and 
print("01234567890123456789")
print(f"{n:<10}{n:>10}")
#Justifies the position of the first argument to the left and justifies the position of the second argument to the right by 10. 
print("01234567890123456789")
print(f"{n:10.3f}{n:10,.2f}{n}")
print("012345678901234567890123456789")
print(f"{n:10.2%}{n:12,.2%}")
#Output:
#01234567890123456789
#      1234   1234
#01234567890123456789
#1234            1234
#01234567890123456789
#  1234.000  1,234.001234
#012345678901234567890123456789
#123400.00% 123,400.00%

#1d
q1= '''"If {0:s} dream it, {0:s} do it. - Walt Disney"'''
print(q1.format('you can'))
a = "ONE"
b = "DAY"
q2 = f"\"{a} {b} or {b} {a}. You decide. Paulo Coelho\""
print(q2)
#"If you can dream it, you can do it. - Walt Disney"
#"ONE DAY or DAY ONE. You decide. Paulo Coelho"



