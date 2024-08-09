print("Welcome to Rodrigo's Pizza!")
size_pizza = input("Do you prefer the small, medium or large pizza? (s/m/l): ").lower().strip()
add_pepperoni = input("Add pepperoni to your pizza? (y/n): ").lower().strip() == "y"
add_cheese = input("Add extra cheese to your pizza? (y/n): ").lower().strip() == "y"

match size_pizza:
    case 's':
        bill = 15
    case 'm':
        bill = 20
    case 'l':
        bill = 25

if size_pizza == "s" and add_pepperoni == True:
    bill += 2
elif (size_pizza == "m" or size_pizza == "l") and add_pepperoni == True:
    bill += 3

if add_cheese == True:
    bill += 1

print(f"Thank you for choosing Rodrigo's Pizza!\nYour final bill is: ${bill}")