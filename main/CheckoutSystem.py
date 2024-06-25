# imports
import os
import time
import random
from PCSelectionMenu import *

def clear_screen():
    # this clears the screen once called
    # 'cls' is for Windows systems, 'clear' is for Linux/macOS
    os.system('cls' if os.name == 'nt' else 'clear')

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
        self.initial_total = 0
        self.vat_total = 0
        # random delivery fee between P150 and P500
        # rounds it after two decimal places
        self.delivery_fee = round(random.uniform(150, 500), 2)
        self.compute_totals()
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

    def compute_totals(self):
        for component in self.components:
            # extracts the price by splitting "Component1: ComponentName - Pvalue"
            # to "Component1: ComponentName" "value"
            # removes the '- P"
            if '- P' in component:
                _, price_str = component.split(' - P')
                price = float(price_str)
                self.initial_total += price
                self.vat_total += price * 0.12

    def print_reciept(self):
        # this turns the components list variable into a text file and adding the total computation and the del. fee
        total_price = self.initial_total + self.vat_total + self.delivery_fee
        with open('World-of-Tomorrow_OfficialReceipt.txt', 'w+') as f:
            f.write('World-of-Tomorrow Official Receipt:')
            f.write('\n==================================\n')
            for component in self.components:
                f.write(component + '\n')
            f.write('==================================')
            f.write(f'\nInitial Total: P{self.initial_total:.0f}')
            f.write(f'\nDelivery Fee: P{self.delivery_fee:.0f}')
            f.write(f'\n12% VAT Total: P{self.vat_total:.0f}')
            f.write('\n==================================')
            f.write(f'\nTotal Price: P{total_price:.0f}')
            f.write('\nThank you for shopping with World-of-Tomorrow!')
            f.close()

    def show_reciept(self):
        # this shows the official receipt
        # the program will return to PCSelectionMenu.py after the user presses Enter
        total_price = self.initial_total + self.vat_total + self.delivery_fee
        print("\nWorld-of-Tomorrow Official Receipt:")
        print("==================================")
        for component in self.components:
            print(component)
        print("==================================")
        print(f'Initial Total: P{self.initial_total:.0f}')
        print(f'Delivery Fee: P{self.delivery_fee:.0f}')
        print(f'12% VAT Total: P{self.vat_total:.0f}')
        print("==================================")
        print(f'Total Price: P{total_price:.0f}')
        print("\nThank you for shopping with World-of-Tomorrow!")
        print("Your receipt is also saved as a text file, please check your file manager.")
        input('\nPress Enter to continue.')



# Code initialization
def main():
    clear_screen()
    CheckoutSys()


if __name__ == "__main__":
    main()
