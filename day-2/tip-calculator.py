print("Tip Calculator - Let's split the bill!")

# Get inputs from the user
total_bill = float(input("Enter the total bill amount: $"))
tip_percent = int(input("Choose a tip percentage (e.g., 10, 12, 15): "))
num_people = int(input("How many people are sharing the bill? "))

# Calculate total with tip
tip_amount = total_bill * (tip_percent / 100)
grand_total = total_bill + tip_amount

# Determine how much each person should pay
amount_per_person = round(grand_total / num_people, 2)

print(f"Each person owes: ${amount_per_person}")
