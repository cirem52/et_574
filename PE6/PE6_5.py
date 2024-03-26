vehicles = ["Truck", "boat", "PLANE"]
position = []

character = input("Enter a letter to be searched")

for x in vehicles:
    if character in x:
        for i in x:
            if i == character:
                position.append(i)
        print(x + " contains the letter " + character + " and it is in position" + position)