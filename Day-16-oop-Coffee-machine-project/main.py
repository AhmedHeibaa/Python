from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()


def coffeMachine():
    isOn = True
    while isOn:
        options = menu.get_items()
        choice = input(f"What would you like? {options}: ")
        
        if choice == "report":
            coffee_maker.report()
            money_machine.report()
        elif choice == "off":
            isOn = False
        else:
            drink = menu.find_drink(choice)
            # print("Please insert coins.")
            # quartersAmount = int(input("How many quarters?: "))
            # dimesAmount = int(input("How many dimes?: "))
            # nicklesAmount = int(input("How many nickles?: "))
            # penniesAmount = int(input("How many pennies?: "))
            # transactionValue = processCoins(quartersAmount,dimesAmount,nicklesAmount,penniesAmount)
            # drinkPrice = MenuItem().cost
            # profit = round(transactionValue - drink.cost,2)
            if money_machine.make_payment(drink.cost):
                if coffee_maker.is_resource_sufficient(drink):
                    coffee_maker.make_coffee(drink)
                    # print(f"Here is ${profit} in change.")
                    # print(f"Here is your {choice}. Enjoy!”")
            #     else:
            #         print("There is no enough resources to make your drink")
            # else:
            #     print("Sorry that's not enough money. Money refunded.")
            
coffeMachine()