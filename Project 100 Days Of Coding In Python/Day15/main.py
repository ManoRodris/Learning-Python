from art import logo

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

AMOUNT_OF_WATER = resources["water"]
AMOUNT_OF_MILK = resources["milk"]
AMOUNT_OF_COFFEE = resources["coffee"]
AMOUNT_OF_MONEY = 0

def process_coins():
    """This function ask which coins the costumer has and calculate the total amount of money"""
    print("Please insert coins")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))
    total_coins = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    return total_coins

def sufficient_resources():
    """This function verify if has the necessary amount of resources to do the coffee which the costumer want"""
    
    water = MENU[order]["ingredients"]["water"]
    coffee = MENU[order]["ingredients"]["coffee"]
    try:
        milk = MENU[order]["ingredients"]["milk"]
    except KeyError:
        pass
    
    if water <= AMOUNT_OF_WATER:
        lack_of_water = False
    else:
        lack_of_water = True

    try:
        if milk <= AMOUNT_OF_MILK:
            lack_of_milk = False
        else:
            lack_of_milk = True
    except NameError:
        pass

    if coffee <= AMOUNT_OF_COFFEE:
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
    """This function check if the customer has the right amount of money to buy the coffee he chose"""
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
    
def decrease_resources():
    global AMOUNT_OF_WATER
    global AMOUNT_OF_COFFEE
    global AMOUNT_OF_MILK

    if order == "espresso":
        AMOUNT_OF_WATER -= MENU[order]["ingredients"]["water"]
        AMOUNT_OF_COFFEE -= MENU[order]["ingredients"]["coffee"]
    else:
        AMOUNT_OF_WATER -= MENU[order]["ingredients"]["water"]
        AMOUNT_OF_MILK -= MENU[order]["ingredients"]["milk"]
        AMOUNT_OF_COFFEE -= MENU[order]["ingredients"]["coffee"]
        

def order_checker():
    """This function checks if the user want a coffee or want the report or choose a type of coffee which the machine don't offer"""
    global AMOUNT_OF_MONEY

    if order == "latte" or order == "espresso" or order == "cappuccino":
        if sufficient_resources():
            money_from_customer = process_coins()
            price_of_coffee = MENU[order]["cost"]
            payback = round(money_from_customer - price_of_coffee, 2)
            if sufficient_money(money_from_customer, price_of_coffee, payback):
                decrease_resources()
                profit = money_from_customer - payback
                AMOUNT_OF_MONEY += round(profit, 2) 
    elif order == "report":
        print(f"Water: {AMOUNT_OF_WATER}ml")
        print(f"Milk: {AMOUNT_OF_MILK}ml")
        print(f"Coffee: {AMOUNT_OF_COFFEE}g")
        print(f"Money: ${AMOUNT_OF_MONEY}")
    else:
        print("We don't have this type of coffee in our machine, please check your answer in accord with our options")

print(logo)
order = input("What would you like? (espresso/latte/cappuccino):").lower().strip()

while order != "stop":
    order_checker()
    print(logo)
    order = input("What would you like? (espresso/latte/cappuccino):").lower().strip()


