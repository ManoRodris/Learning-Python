print("Welcome to the rollercoaster!")
height = float(input("What is your height? "))

if height > 1.20:
    print("You can go to the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        print("Your ticket will cost $5")
    elif age >= 12 and age <= 18:
        print("Your ticket will cost $7")
    else:
        print("Your ticket will cost $12")
else:
    print("Sorry, you can't go to the rollercoaster")

