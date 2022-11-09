import os

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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


def coffee_machine():
    resources = {
        "water": 500,
        "milk": 275,
        "coffee": 120,
        "money": 25,
    }

    quarters = 0
    dimes = 0
    nickles = 0
    pennies = 0

    quarters_value = 0
    dimes_value = 0
    nickles_value = 0
    pennies_value = 0


    def report():
        print(f'Water: {resources["water"]}ml.')
        print(f'Milk: {resources["milk"]}ml.')
        print(f'Coffee: {resources["coffee"]}g.')
        print(f'Money: ${resources["money"]}.')

    def cost():
        print("Please insert coins.")
        quarters = int(input("how many quarters?: "))
        dimes = int(input("how many dimes?: "))
        nickles = int(input("how many nickles?: "))
        pennies = int(input("how many pennies?: "))
        return quarters, dimes, nickles, pennies

    def value_of_coins(quarters, dimes, nickles, pennies, cost_drink):
        quarters_value = .25 * quarters
        dimes_value = .10 * dimes
        nickles_value = .05 * nickles
        pennies_value = .01 * pennies
        total_put_in = quarters_value + dimes_value + nickles_value + pennies_value
        costs = cost_drink
        if total_put_in < costs:
            print("Sorry that is not enough money. Here is your refund. ")
        else:
            change = round(total_put_in - costs, 2)
            print(f"Here is your change: ${change}")

    def drink_choice(choose):
        chosen_drink = MENU[choose]["ingredients"]
        cost_drink = MENU[choose]["cost"]
        chosen_drink_name = choose
        print(chosen_drink)
        return chosen_drink, cost_drink, chosen_drink_name

    def resource_checker(chosen_drink, chosen_drink_name):
        if resources["coffee"] < 18 or resources["water"] < 50:
            print("Sorry, not enough ingredients to create more drinks. Please call 1-800-coffee-m for assistance!")
            return False
        elif resources["water"] < chosen_drink["water"]:
            print(f"Sorry, not enough water for {chosen_drink_name}.")
            return False
        elif resources["coffee"] < chosen_drink["coffee"]:
            print(f"Sorry, not enough coffee for {chosen_drink_name}.")
            return False
        elif resources["milk"] < chosen_drink["milk"]:
            print(f"Sorry, not enough milk for {chosen_drink_name}.")
            return False
        else:
            return True

    def turn_off():
        os.system('clear')
        print("Coffee machine off")
        return False

    def welcome():
        print("Welcome to Bin Bin's coffee machine.")

    machine = True
    while machine:
        welcome()
        choose = input("What would you like: espresso, latte, or cappuccino?: ").lower()
        if choose == "off":
            machine = turn_off()
        elif choose == "report":
            report()
        else:
            chosen_drink, cost_drink, chosen_drink_name = drink_choice(choose)
            if resource_checker(chosen_drink, chosen_drink_name):
                quarters, dimes, nickles, pennies = cost()
                value_of_coins(quarters, dimes, nickles, pennies, cost_drink)
                resources["money"] += round(cost_drink, 2)
                resources["water"] -= chosen_drink["water"]
                resources["milk"] -= chosen_drink["milk"]
                resources["coffee"] -= chosen_drink["coffee"]


coffee_machine()
