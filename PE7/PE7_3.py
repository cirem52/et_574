sum = 0

for x in range(1,101):
    sum = x + sum   #adds value of x into previous sum value. 

print(sum)


#B
sum_2 = 0
x = 0

while x <= 100:
    if x % 2 == 0:
        sum_2 = sum_2 + x       #creates a counter, x, and keeps increasing that x value by 1. If that x value, at any point, is even, adds it to a sum. Prints sum at the end.
        x += 1
    else:
        x += 1
print(sum_2)