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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}")

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

def process_coins():
    """Returns the total Coins"""
    print("Please insert the amount")
    total = int(input("How many Quarters: ")) * 0.25
    total += int(input("How many Dimes: ")) * 0.10
    total += int(input("How many Nickels: ")) * 0.05
    total += int(input("How many Pennies: ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    """Return True when payment is sufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is your change ${change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry not enough Money")
        return False

flag = True
while flag:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    
    if user_choice == 'off':
        flag = False
    elif user_choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        if user_choice in MENU:
            drink = MENU[user_choice]
            if is_resource_sufficient(drink["ingredients"]):
                payment = process_coins()
                if is_transaction_successful(payment, drink["cost"]):
                    make_coffee(user_choice, drink["ingredients"])
        else:
            print("Invalid choice. Please select from the menu.")
