# tip calcultor by goutham-sathya
print("Welcome to the tip calculator!")
# taking input values from the user
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
# calculations
tip_percent = tip / 100
tip_amount = bill * tip_percent
total_bill = bill + tip_amount
bill_per_person = total_bill / people
pay_amount = round(bill_per_person, 2)
# output
print(f"Each person should pay: ${pay_amount} ")
