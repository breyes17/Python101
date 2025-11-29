print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? "))
tip_input = int(input("How much tip you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

tip = total_bill * (tip_input / 100)
calculate = round((total_bill + tip) / people,2)

print(f"Each person should pay: ${calculate:.2f}")