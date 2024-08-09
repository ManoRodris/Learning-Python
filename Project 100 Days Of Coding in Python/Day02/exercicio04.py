print("Welcome to the tip calculator!\n")
bill_without_tip = input("What was the total bill? $")
tip_percentage = input("How much tip would you like to give? $")
people_count = input("How many people to split the bill? ")

total_bill = float(bill_without_tip) * float(tip_percentage)/100 + float(bill_without_tip)
amount_of_each = round(total_bill/int(people_count), 2)

print(f"Each person should pay ${amount_of_each}")

