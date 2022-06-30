from constants import *


def coins():
    quarters = int(input("How many quarters?"))
    dimes = int(input("How many dimes?"))
    nickles = int(input("How many nickles?"))
    pennies = int(input("How many pennies?"))
    all_coins = [quarters * 0.25, dimes * 0.10, nickles * 0.05, pennies * 0.01]
    return round(sum(all_coins), 2)


def report():
    print(
        f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${resources['money']}")


def make_coffee(drink):
    has_resources = True
    cost = MENU[drink]['cost']
    menu_water = MENU[drink]['ingredients']['water']
    if drink == 'espresso':
        menu_milk = 0
    else:
        menu_milk = MENU[drink]['ingredients']['milk']
    menu_coffee = MENU[drink]['ingredients']['coffee']

    water_left = resources['water']
    milk_left = resources['milk']
    coffee_left = resources['coffee']

    if menu_water > water_left:
        print("Not enough water!")
        has_resources = False
    if menu_milk > milk_left:
        print("Not enough milk!")
        has_resources = False
    if menu_coffee > coffee_left:
        print("Not enough coffee!")
        has_resources = False

    if has_resources:
        money = coins()
        if money < cost:
            print(f'Not enough! You entered ${money} and the cost is ${cost}. Coins refunded')
        elif money >= cost:
            change = round(money - cost, 2)
            print(f"Here's your change: ${change}")
            resources['water'] -= menu_water
            resources['milk'] -= menu_milk
            resources['coffee'] -= menu_coffee
            resources['money'] += cost
            print(f"Here is your {drink}! Enjoy ☕! ")
