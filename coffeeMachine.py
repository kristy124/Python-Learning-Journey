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
}

money = 0


def sufficient_resources(resources, drink_ingredients):
    """Checks resources available and returns True if resources are sufficient"""
    for ingredient in drink_ingredients:
        if resources[ingredient] < drink_ingredients[ingredient]:
            print(f"Sorry, there's not enough {ingredient}")
            return False
        else:
            return True


def calc_coins(quarters_amount, dimes_amount, nickels_amount, pennies_amount):
    """Returns the total sum of coins inserted"""
    total = 0.25 * quarters_amount + 0.10 * dimes_amount + 0.05 * nickels_amount + 0.01 * pennies_amount
    return total


def transaction_successful(drink_cost, coins_total):
    """Returns True if money is sufficient and calculates change, or returns False if the money is insufficient"""
    if coins_total >= drink_cost:
        global money
        money += drink_cost
        change = round(coins_total - drink_cost, 2)
        print(f"Here is ${change} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(resources, drink_ingredients):
    """Deducts from resources based on ingredients used to make coffee"""
    for ingredients in drink_ingredients:
        resources[ingredients] -= drink_ingredients[ingredients]
    print(f"Here is your {choice}☕️. Enjoy!")


machine_on = True

while machine_on:
    choice = input("What would you like? (espresso $1.5 /latte $2.5 /cappuccino $3.0): ")
    if choice == "espresso" or choice == "latte" or choice == "cappuccino":
        drink = MENU[choice]
        if sufficient_resources(resources, drink['ingredients']):
            print("Please insert coins")
            quarters_amount = int(input("How many quarters?: "))
            dimes_amount = int(input("How many dimes?: "))
            nickles_amount = int(input("How many nickles?: "))
            pennies_amount = int(input("How many pennies?: "))
            coins_total = calc_coins(quarters_amount, dimes_amount, nickles_amount, pennies_amount)
            if transaction_successful(drink['cost'], coins_total):
                make_coffee(resources, drink['ingredients'])

    elif choice == "off":
        machine_on = False

    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")

    else:
        print("Please select a valid option. ")


