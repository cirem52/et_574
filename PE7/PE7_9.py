lower = int(input("enter a lower bound: "))
upper = int(input("enter an upper bound: "))
incVal = int(input("enter an increment value: "))
forLoopL = lower
forLoopU = upper

print("Using While Loop")
while lower < upper:
    print(lower)
    lower += incVal
    if lower == upper:
        print(lower)        

print("Using For Loop")
for x in range(0,forLoopU,incVal):
    print(x + forLoopL)
    if (x+forLoopL) == upper:
        break
