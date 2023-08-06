from products import *
############################ PRINTREPORT_FUN ###########################
def printReport():
    print(f"""
water:{resources["water"]} ml
milk:{resources["milk"]} ml
Coffee:{resources["coffee"]} g
Money:{resources["money"]} $
""")

#########################################################################  
############################ CHECKRESOURCES_FUN ###########################    
def checkEnoughResources(drink):
    water = MENU[drink]["ingredients"]["water"]
    coffee = MENU[drink]["ingredients"]["coffee"]
    milk = MENU[drink]["ingredients"]["milk"]
    if water <= resources["water"] and coffee <= resources["coffee"] and milk <= resources["milk"]:
        resources["water"] -= water
        resources["coffee"] -= coffee
        resources["milk"] -= milk
        return True
    else:
        return False   
#########################################################################
############################ PROCESSCOINS_FUN ########################### 
def processCoins(quarter,dimes,nickles,pennies):
     quartersValue,dimesValue,nicklesValue,penniesValue = 0.25,0.10,0.05,0.01
     result = (quarter * quartersValue) + (dimes * dimesValue) + (nickles * nicklesValue) + (pennies * penniesValue)
     return result
#########################################################################
############################ CHECKENOUGHMONEY_FUN ########################### 
def checkEnoughMoney(drink, transactionAmount):
    drinkPrice = MENU[drink]["cost"]
    # print(drinkPrice)
    # print(transactionAmount)
    if transactionAmount >= drinkPrice:
        inchageValue = round(transactionAmount - drinkPrice,2)
        resources["money"] = inchageValue
        return True
    else:
        return False
######################################################################### 
############################ COFFEEMACHINE_FUN ###########################  
def coffeMachine():
    isOn = True
    resources["money"] = 0
    while isOn:
        decision = input("What would you like? (espresso/latte/cappuccino): ")
        
        if decision == "report":
            printReport()
        elif decision == "off":
            isOn = False
        else:
            print("Please insert coins.")
            quartersAmount = int(input("How many quarters?: "))
            dimesAmount = int(input("How many dimes?: "))
            nicklesAmount = int(input("How many nickles?: "))
            penniesAmount = int(input("How many pennies?: "))
            transactionValue = processCoins(quartersAmount,dimesAmount,nicklesAmount,penniesAmount)
            drinkPrice = MENU[decision]["cost"]
            profit = round(transactionValue - drinkPrice,2)
            if checkEnoughMoney(decision,transactionValue):
                if checkEnoughResources(decision):
                    print(f"Here is ${profit} in change.")
                    print(f"Here is your {decision}. Enjoy!”")
                else:
                    print("There is no enough resources to make your drink")
            else:
                print("Sorry that's not enough money. Money refunded.")
                
#########################################################################
            
coffeMachine()              
        