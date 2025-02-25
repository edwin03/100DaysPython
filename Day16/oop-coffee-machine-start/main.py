from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True

while is_on:
    selection = input(f"What would you like? {menu.get_items()}: ").lower()
    if selection == "report":
        print(f"{coffee_maker.report()}")
        print(f"{money_machine.report()}")
    elif selection == "off":
        print("Turning off the coffee machine for maintenance. Goodbye.")
        is_on = False
    else: 
        order = menu.find_drink(selection)
        if order is None:
            pass
        else: 
            if coffee_maker.is_resource_sufficient(order) == True and money_machine.make_payment(order.cost) == True:
                coffee_maker.make_coffee(order)