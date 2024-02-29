height = float(input("Enter your height (In cm): "))
weight = float(input("Enter your weight (In kg): "))
bmi = round((weight / (height**2)) * 703,3)
print("Your bmi is: " + str(bmi))
