n = input("Enter integer: ")
o = 0
values = []

n = int(n)


if n > 0:
    while n >= o:
        if o % 2 == 1 and o % 5 == 0:
            values.append(o)
            o += 1
        else:
            o += 1

else:
    while n <= 0:
        if n % 2 == 0 and n % 6 == 0:
            values.append(n)
            n += 1
        else:
            n += 1

print(values)