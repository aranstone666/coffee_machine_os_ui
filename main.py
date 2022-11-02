from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

restart = True

menu = Menu()
menuItems = menu.get_items()

coffeeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()

while restart:
    userInput = input(f"What do you like to drink {menuItems}?: ")
    if userInput in menuItems:
        drink = menu.find_drink(userInput)
        if coffeeMaker.is_resource_sufficient(drink) and moneyMachine.make_payment(drink.cost):
            coffeeMaker.make_coffee(drink)
    elif userInput == "off":
        restart = False
    elif userInput == "report":
        coffeeMaker.report()
        moneyMachine.report()
