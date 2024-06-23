# Not yet integrated
# imports
import os
import time
import random
from PCSelectionMenu import *


# global functions
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


class CheckoutSys:
    def __init__(self):
        while True:
            clear_screen()
            payment_system = input('''Select a payment method.
            
    [1] Cash-on-Delivery
    [2] Card
    
    Type your choice and press Enter to select: ''')

            if payment_system == "1":
                print("Cash-on-Delivery selected!")
                print("World-of-Tomorrow will now pinpoint your location for the delivery process...")
                time.sleep(1)
                print("Pinpointing location....")
                time.sleep(5)
                print("Success!")
                time.sleep(1)
                RecieptSys()
                break

            elif payment_system == "2":
                print("Payment system for credit/debit cards is down for maintenance.")
                time.sleep(1)
                continue


class RecieptSys:
    def __init__(self):
        clear_screen()
        print("We will now print your official receipt...")
        time.sleep(1)
        print("Printing....")
        time.sleep(5)
        self.components = self.load_components()
        self.print_receipt()

    def load_components(self):
        components = []
        try:
            with open('draftreceipt.txt', 'r') as file:
                for line in file:
                    components.append(line.strip())
        except FileNotFoundError:
            print("Error: draftreceipt.txt file not found.")
        return components

    def print_receipt(self):
        print("Official Receipt:")
        print("=================")
        for component in self.components:
            print(component)
        print("=================")
        print("Thank you for shopping with World-of-Tomorrow!")
        input('\n Press Enter to continue.')



# Code initialization
def main():
    clear_screen()
    CheckoutSys()


if __name__ == "__main__":
    main()
