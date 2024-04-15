p=0
n1 = int(input("Enter an integer "))
n2 = int(input("Enter another integer "))

if n1 < n2:
    while n1 < n2:
        print(n1, end=" ")
        n1 += 1
        if n1 == n2:
            print(n1)


elif n1 > n2:
    for x in range(n1):
        p = n1-x
        if p==n2:
            print(p)
            break
        else:
            print(p,end="|")
else:
    print("n1 = n2")
            
