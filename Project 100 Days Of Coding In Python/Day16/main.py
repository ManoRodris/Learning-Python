from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

stop_machine = False
type_of_coffee = Menu()
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()

while not stop_machine:
    display_coffees = type_of_coffee.get_items()

    order = input(f"What would you like? {display_coffees}: ")

    chosen_coffee = type_of_coffee.find_drink(order)

    if chosen_coffee is not None:
        sufficient_resources = coffee_machine.is_resource_sufficient(chosen_coffee)
        if sufficient_resources:
            price = chosen_coffee.cost
            if money_machine.make_payment(price):
                coffee_machine.make_coffee(chosen_coffee)
    elif order == "report":
        coffee_machine.report()
        money_machine.report()
    else:
        stop_machine = True



