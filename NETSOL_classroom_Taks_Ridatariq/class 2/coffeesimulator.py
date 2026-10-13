resources = {
    "water": 500,
    "milk": 300,
    "coffee": 100,
    "cups": 5,
    "money": 0,
}

menu = {
    "espresso": {"water": 50, "milk": 0, "coffee": 18, "cost": 50},
    "latte": {"water": 200, "milk": 150, "coffee": 24, "cost": 80},
    "cappuccino": {"water": 250, "milk": 100, "coffee": 24, "cost": 100},
}


def report():
    """Display the current inventory and money earned."""
    print("\n----- Machine report -----")
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Cups: {resources['cups']}")
    print(f"Money earned: Rs.{resources['money']}")
    print("--------------------------\n")


def check_resources(drink):
    """Return False and explain the first missing resource."""
    ingredients = menu[drink]
    resource_names = {
        "water": "water",
        "milk": "milk",
        "coffee": "coffee",
    }

    for resource, amount in ingredients.items():
        if resource in resource_names and resources[resource] < amount:
            print(f"Sorry, there is not enough {resource_names[resource]}.")
            return False

    if resources["cups"] < 1:
        print("Sorry, there are no cups left.")
        return False
    return True


def take_payment(drink):
    """Collect a whole-rupee payment and return whether it is sufficient."""
    price = menu[drink]["cost"]
    print(f"Price of your {drink}: Rs.{price}")

    while True:
        try:
            payment = int(input("Enter payment in rupees: Rs."))
        except ValueError:
            print("Please enter a whole number.")
            continue

        if payment < 0:
            print("Payment cannot be negative.")
            continue
        if payment < price:
            print(f"Payment is not enough. Rs.{payment} refunded.")
            return False

        change = payment - price
        if change:
            print(f"Here is your change: Rs.{change}")
        return True


def make_coffee(drink):
    """Use the ingredients, record the sale, and serve the drink."""
    ingredients = menu[drink]
    for resource in ("water", "milk", "coffee"):
        resources[resource] -= ingredients[resource]
    resources["cups"] -= 1
    resources["money"] += ingredients["cost"]
    print(f"Here is your {drink}. Enjoy!")


def main():
    print("Coffee machine ready.")
    while True:
        choice = input(
            "\nWhat would you like? (espresso/latte/cappuccino): "
        ).strip().lower()

        if choice == "off":
            print("Machine turned off.")
            break
        if choice == "report":
            report()
        elif choice in menu:
            if check_resources(choice) and take_payment(choice):
                make_coffee(choice)
        else:
            print("Invalid choice. Please select a valid coffee.")


if __name__ == "__main__":
    main()