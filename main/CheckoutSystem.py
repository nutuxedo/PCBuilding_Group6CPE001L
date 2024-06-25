# imports
import os
import time
import random
from PCSelectionMenu import *
from main import clear_screen

class CheckoutSys:
    def __init__(self):
        while True:
            clear_screen()
            payment_system = input('''\nSelect a payment method.
            
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
        self.print_reciept()
        self.show_reciept()

    def load_components(self):
        # loads the draftreceipt.txt from PCSelectionMenu.py
        # it will give out an error if the file hasnt been created
        # this will load the txt file and write it into a list variable 'components'
        components = []
        with open('draftreceipt.txt', 'r') as file:
            for line in file:
                    components.append(line.strip())
            return components

    def print_reciept(self):
        # this turns the components list variable into a text file and adding the total computation and the del. fee
        with open('World-of-Tomorrow_OfficialReceipt.txt', 'w+') as f:
            f.write('World-of-Tomorrow Official Receipt:')
            f.write('\n==================================\n')
            for component in self.components:
                f.write(component + '\n')
            f.write('==================================')
            f.write('\nInitial Total: ')
            f.write('\nDelivery Fee: ')
            f.write('\n==================================')
            f.write('\nTotal Price: ')
            f.close()

    def show_reciept(self):
        # this shows the official receipt
        # the program will return to PCSelectionMenu.py after the user presses Enter
        print("\nWorld-of-Tomorrow Official Receipt:")
        print("==================================")
        for component in self.components:
            print(component)
        print("==================================")
        print('Initial Total:')
        print('Delivery Fee: ')
        print('==================================')
        print('Total Price: ')
        print("\nThank you for shopping with World-of-Tomorrow!")
        print("Your receipt is also saved as a text file, please check your file manager.")
        input('\nPress Enter to continue.')



# Code initialization
def main():
    clear_screen()
    CheckoutSys()


if __name__ == "__main__":
    main()
