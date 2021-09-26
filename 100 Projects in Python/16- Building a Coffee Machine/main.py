from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu = Menu()
money_machcine = MoneyMachine()
coffe_maker = CoffeeMaker()
Coffee_Machine = True
while Coffee_Machine:
    options = menu.get_items()
    user_input = input(f"What would you like? {options}:")
    if user_input in ['espresso', 'latte', 'cappuccino', 'report', 'off']:
        if user_input == 'off':
            Coffee_Machine = False
        elif user_input == 'report':
            coffe_maker.report()
            money_machcine.report()
        else:
            drink = menu.find_drink(user_input)
            is_enough_ingredients = (coffe_maker.is_resource_sufficient(drink))
            is_payment_successful = money_machcine.make_payment(drink.cost)
            if is_enough_ingredients and is_payment_successful:
                coffe_maker.make_coffee(drink)
    else:
        print("Enter Valid Value")
