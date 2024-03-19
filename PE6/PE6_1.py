a = 2
b = 3
c = 0
#A 
print(a ** b == b ** a) 
#False

#B 
print(a < b or b < a)
#True


#C 
print('dog' > 'cat' + 'mouse') 
#True


#D 
print('Car' < 'Train')
#True


#E 
print((a == b) and ((a * a < b * b) or (b < a) and (2 * a < b)))
#False


#F 
print((a <= b) or ((a * a < b * b) or (b < a) and (2 * a < b)))
#True



#G 
print(not ((a < b) and (a < (b + a))))
#False


#H 
print("small" > "large" and (not c ))
#True



#I 
print(isinstance(c, int)) 
#True


#J 
print(isinstance(3.14, float))
#True
