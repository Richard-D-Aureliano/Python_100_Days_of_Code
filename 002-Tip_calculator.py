print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
perc = int(input("What percentage tip would you like to give?10, 12 or 15? "))
numPeople = int(input("How many people to split the bill? "))

perc = perc / 100
tip = bill * perc + bill 
divided_bill = tip / numPeople

print(f"Each person should pay: ${divided_bill:.2f}")