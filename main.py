print ("Welcome to the tip calculator")

totalBill = float(input("What was the total bill? $"))

print(totalBill)

percentageTip = int(input("How much tip would you like to give? 10, 12 or 15? "))

print(percentageTip)

amountOfPersons = int(input("How many people to split the bill? "))

print(amountOfPersons)

result = round((totalBill / amountOfPersons) * (1.00 + percentageTip),2)

print(f"Each person should pay: ${result}")