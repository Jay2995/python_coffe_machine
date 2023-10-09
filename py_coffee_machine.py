import os
import sys
import random

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

profit = 0;

# function that shwos report()
def report(resources):
    for key, value in resources.items():
        unit = "ml" if key in ("water", "milk") else "g"
        print(f"{key} {value} {unit}");

# report = report(resources);



# def make_cofee(coffee_type, order_ingredients):
def make_coffe(order_ingredients):
    for i in order_ingredients:
        resources[i] -= order_ingredients[i];






##functions 

def print_report():
    for key, value in resources.items():
         print(f"{key}, {value}");


#check resources

def check_resource_sufficient(order_ingredients):
    for i in order_ingredients:
        if order_ingredients[i] > resources[i]:
            print(f"Sorry there is not enough {i}");    
            return False;
        else:
            return True;

# check_resource_sufficient(MENU[order_ingredients]["ingredients"]);

def process_coins():
    print("Please insert coins")
    total = int(input("How many quarters :")) * 0.25;
    total += int(input("How manny dimes? :")) * 0.10;
    total += int(input("How many nickles? :")) * 0.05;
    total += int(input("How many pennies? :")) * 0.01;
    return total



def check_transaction_successful(total_received, coffe_cost):
    global profit;
    if total_received < coffe_cost:
        print("Sorry, not enough money. Money refunded");
        return False;
    elif total_received == coffe_cost:
        profit += coffe_cost;
        return True;
    elif total_received > coffe_cost:
        change = round(total_received - coffe_cost, 2)
        profit += coffe_cost
        print(f"Your change is $ {change}");
        return True;



power_on = True

while power_on:
    coffee_choice = input("What would you like? (espresso/latte/cappuccino): ")

    if coffee_choice == "off":
        print("Machien urning off");
        power_on = False;
    elif coffee_choice == "report":
        report(resources); 
    
    elif check_resource_sufficient(MENU[coffee_choice]["ingredients"]) :
        total = process_coins()
        if check_transaction_successful(total,MENU[coffee_choice]["cost"]):
            make_coffe(MENU[coffee_choice]["ingredients"]);
            report(resources)





