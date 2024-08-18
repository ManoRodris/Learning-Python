MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 18,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def process_coins():
    """This function checks the amount of money the customer has in coins and calculate the total amount of money"""
    print("Please insert coins")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))
    amount_of_money = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    return amount_of_money

def sufficient_resources():
    """This function verify if has the necessary amount of resources to do the coffee which the costumer want"""
    
    water = MENU[order]["ingredients"]["water"]
    coffee = MENU[order]["ingredients"]["coffee"]
    try:
        milk = MENU[order]["ingredients"]["milk"]
    except KeyError:
        pass
    
    if water <= amount_of_water:
        lack_of_water = False
    else:
        lack_of_water = True

    try:
        if milk <= amount_of_milk:
            lack_of_milk = False
        else:
            lack_of_milk = True
    except NameError:
        pass

    if coffee <= amount_of_coffee:
        lack_of_coffee = False
    else:
        lack_of_coffee = True

    try:
        if lack_of_water or lack_of_milk or lack_of_coffee:
            if lack_of_milk:
                print("Sorry, there is not enough milk")
            if lack_of_water:
                print("Sorry, there is not enough water")
            if lack_of_coffee:
                print("Sorry, there is not enough coffee")
            return False
        else:
            return True
    except NameError:
        if lack_of_water or lack_of_coffee:
            if lack_of_water:
                print("Sorry, there is not enough water")
            if lack_of_coffee:
                print("Sorry, there is not enough coffee")
            return False
        else:
            return True

def sufficient_money(money_from_customer, price_of_coffee, payback):
    if money_from_customer > price_of_coffee:
        print(f"Here is ${payback} in change")
        print(f"Here is your {order}, enjoy!")
        return True
    elif money_from_customer < price_of_coffee:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        print(f"Here is your {order}, enjoy!")
        return True
    
def decrease_resources(amount_of_water, amount_of_milk, amount_of_coffee):
    if order == "espresso":
        amount_of_water -= MENU[order]["ingredients"]["water"]
        amount_of_coffee -= MENU[order]["ingredients"]["coffee"]
    else:
        amount_of_water -= MENU[order]["ingredients"]["water"]
        amount_of_milk -= MENU[order]["ingredients"]["milk"]
        amount_of_coffee -= MENU[order]["ingredients"]["coffee"]
        

def order_checker(amount_of_water, amount_of_milk, amount_of_coffee, amount_of_money):
    """This function checks if the user want a coffee or want the report or choose a type of coffee which the machine don't offer"""
    
    if order == "latte" or order == "espresso" or order == "cappuccino":
        if sufficient_resources():
            money_from_customer = process_coins()
            price_of_coffee = MENU[order]["cost"]
            payback = round(money_from_customer - price_of_coffee, 2)
            if sufficient_money(money_from_customer, price_of_coffee, payback):
                decrease_resources(amount_of_water, amount_of_milk, amount_of_coffee)
                profit = money_from_customer - payback
                amount_of_money += profit
                return amount_of_money
    elif order == "report":
        print(f"Water: {amount_of_water}ml")
        print(f"Milk: {amount_of_milk}ml")
        print(f"Coffee: {amount_of_coffee}g")
        print(f"Money: ${amount_of_money}")
    else:
        print("We don't have this type of coffee in our machine, please check your answer in accord with our options")

order = input("What would you like? (espresso/latte/cappuccino):").lower().strip()

amount_of_water = resources["water"]
amount_of_milk = resources["milk"]
amount_of_coffee = resources["coffee"]
amount_of_money = 0

while order != "stop":
    amount_of_money = round(order_checker(amount_of_water, amount_of_milk, amount_of_coffee, amount_of_money), 2)
    order = input("What would you like? (espresso/latte/cappuccino):").lower().strip()

