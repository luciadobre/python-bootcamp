from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

def coffee_machine():
    running = True
    while running:
        options = menu.get_items()
        prompt = input(f"What would you like? ({options}):")
        if prompt == 'off':
            running = False
        elif prompt == 'report':
            coffee_maker.report()
            money_machine.report()
        else:
            drink = menu.find_drink(prompt)
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)



coffee_machine()
