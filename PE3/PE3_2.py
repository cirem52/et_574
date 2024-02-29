bill = float(input("Input the bill amount: "))
tip = int(input("Enter the tip amount (Exclude the percentage sign): "))

tipAmount = tip / 100

print("Your tip is " + str(round(bill * tipAmount, 2)))
print("Total: " + str(round(bill + (bill * tipAmount), 2)))

