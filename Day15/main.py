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
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.00,
}

# TODO: 1. Print report of all the coffee machine resources
def print_report():
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${resources['money']:.2f}")

# TODO: 2. Check resouces are sufficent when someone orders a dring
def check_resources(coffee):
    for ingridient in MENU[coffee]["ingredients"]:
        if resources[ingridient] >= MENU[coffee]["ingredients"][ingridient]:
            pass
        else:
            print(f"Sorry there is not enough {ingridient}.")
            return False
    return True

# TODO: 3. Process coins
def process_coins():
    '''Return the total calulated from coins inserted.'''
    print("Please insert coins.")
    quarters = input("How many quarters? ")
    dimes = input("How many dimes? ")
    nickles = input("How many nickles? ")
    pennies = input("How many pennies? ")
    return int(quarters) * 0.25 + int(dimes) * 0.10 + int(nickles) * 0.05 + int(pennies) * 0.01

# TODO: 4. Check if the transaction is successful
def check_transaction(total, coffee):
    if total == MENU[coffee]["cost"]:
        return True
    elif total > MENU[coffee]["cost"]:
        resources["money"] += MENU[coffee]["cost"]
        refund = total - MENU[coffee]["cost"]
        print(f"Here is ${refund:.2f} dollars in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")

# TODO: 5. Make coffee
def make_coffee(coffee):
    for ing in MENU[coffee]["ingredients"]:
        resources[ing] -= MENU[coffee]["ingredients"][ing]
    print(f"Here is your {coffee}. Enjoy! 🍵")

turnOff = False
while turnOff == False:
# TODO: 6. Create the user interface
    selection = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if selection in ["espresso", "latte", "cappuccino"]:
        if check_resources(selection) == True and check_transaction(process_coins(), selection) == True:
            make_coffee(selection)
    elif selection in ["report"]:
        print_report()
    elif selection in ["off"]:
        print("Turning off the coffee machine for maintenance. Goodbye.")
        turnOff = True
    else:
        print(f"'{selection}' is an invalid input. Try again.")





# print_report()
# check_resources("espresso")
# insertedCoins = process_coins()
# check_transaction(insertedCoins, "espresso")
# make_coffee("espresso")
# print_report()