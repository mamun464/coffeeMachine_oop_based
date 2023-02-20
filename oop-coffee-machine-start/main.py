from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
Coffee_Maker=CoffeeMaker()
Money_Machine=MoneyMachine()
menu=Menu()




while True:
    option = menu.get_items()
    user_choise = input(f"  What would you like? {option}: ").lower()
    if user_choise=="off":
        exit()
    elif user_choise=="report":
        Coffee_Maker.report()
        Money_Machine.report()
    else:
        MenuItem=menu.find_drink(user_choise)
        resource_available=(Coffee_Maker.is_resource_sufficient(MenuItem))
        if resource_available:
           payment_clear=Money_Machine.make_payment(MenuItem.cost)
           if payment_clear:
               Coffee_Maker.make_coffee(MenuItem)



