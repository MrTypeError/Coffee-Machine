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


def Process_coins(quarter, dimes, nickel, pennies ):
    total_currency = 0
    toatal_dollar =  float (0.25*quarter + 0.1*dimes + 0.05*nickel + 0.01*pennies)
    return toatal_dollar
    '''
    Calculate the moneary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
    penny -> 1 cent -> $0.01
    nikel -> 5 cent -> $0.05
    Dime ->  10 cent -> $0.10
    quarter -> 25 cent ->$0.25
    pass
    '''


            
def shutdown():
    return 

def Check_transaction():
    pass

def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def generate_report():
    pass


def make_espresso(menu):
    if resource_checker():
        # 50ml water | 18ml coffee
        for k,v in MENU:
            print(f'key={k} and value={v}')



def make_cappuccino():
   if resource_checker():
        # 200ml water | 24g coffee | 150ml milk
        pass
   
def make_latte():
   if resource_checker():
        # 250ml water | 24g coffee | 100ml milk
        pass 

def options_checker(option):
    if option == "espresso":
        make_espresso()
    if option == "cappuccino":
        make_cappuccino()
    if option == "latte":
        make_latte()
    if option == "off":
        shutdown()


is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
