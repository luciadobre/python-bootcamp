from constants import *
from back_end import *


def main():
    running = True
    while running:
        prompt = input("What would you like? (espresso/latte/cappuccino):")
        if prompt == 'off':
            running = False
        elif prompt == 'report':
            report()
        else:
            drink = prompt
            make_coffee(drink)


main()
