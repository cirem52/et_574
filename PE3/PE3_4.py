a = input("Enter an integer ")
b = input("Enter another integer ")
c = input("Enter a third integer ")

print("Before Sorting:" + a, b, c)

a = int(a)
b = int(b)
c = int(c)



highest_value = max(a,b,c)
lowest_value = min(a,b,c)
middle_value = (a + b + c) - (highest_value + lowest_value)
print(lowest_value, middle_value, highest_value)
