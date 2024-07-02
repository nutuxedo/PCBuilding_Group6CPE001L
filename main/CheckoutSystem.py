# imports
import os
import time
import random
from PCSelectionMenu import *


# Global functions and variables
def clear_screen():
    # this clears the screen once called
    # 'cls' is for Windows systems, 'clear' is for Linux/macOS
    os.system('cls' if os.name == 'nt' else 'clear')


personal_info = {}


def collect_personal_info():
    global personal_info
    if not personal_info:
        personal_info = {
            "full name": "",
            "house number": "",
            "street": "",
            "subdivision": "",
            "barangay": "",
            "city": "",
            "region": ""
        }
        for field in personal_info:
            while True:
                clear_screen()
                print("We need your information for the delivery process.")
                value = input(f"Please enter your {field}:\n")
                if value == "":
                    print(f"Enter a {field}!")
                    time.sleep(1)
                    clear_screen()
                elif field == "full name" and any(char.isdigit() for char in value):
                    print("No numbers!")
                    time.sleep(1)
                    clear_screen()
                else:
                    personal_info[field] = value
                    break
    return personal_info


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
                time.sleep(1)
                collect_personal_info()
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
        self.personal_info = collect_personal_info()
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
        # it will give out an error if the file hasn't been created
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
        delivery_info = self.personal_info
        total_price = self.initial_total + self.vat_total + self.delivery_fee
        with open('World-of-Tomorrow_OfficialReceipt.txt', 'w+') as f:
            f.write('World-of-Tomorrow Official Receipt\n')
            f.write(f'for Mr./Mrs. {delivery_info["full name"]}:')
            f.write('\n==================================================\n')
            f.write('DELIVERY ADDRESS:\n')
            f.write(f'House No: {delivery_info["house number"]}\n')
            f.write(f'Street: {delivery_info["street"]}\n')
            f.write(f'Subdivision: {delivery_info["subdivision"]}\n')
            f.write(f'Barangay: {delivery_info["barangay"]}\n')
            f.write(f'City: {delivery_info["city"]}\n')
            f.write(f'Region: {delivery_info["region"]}')
            f.write('\n==================================================\n')
            f.write('COMPONENTS:\n')
            for component in self.components:
                f.write(component + '\n')
            f.write('==================================================')
            f.write('\nCHARGES:')
            f.write(f'\nInitial Total: P{self.initial_total:.0f}')
            f.write(f'\nDelivery Fee: P{self.delivery_fee:.0f}')
            f.write(f'\n12% VAT Total: P{self.vat_total:.0f}')
            f.write('\n==================================================')
            f.write(f'\nTOTAL PRICE: P{total_price:.0f}')
            f.write('\n==================================================')
            f.write('\nThank you for shopping with World-of-Tomorrow!')
            f.close()

    def show_reciept(self):
        # this shows the official receipt
        # the program will return to PCSelectionMenu.py after the user presses Enter
        delivery_info = self.personal_info
        total_price = self.initial_total + self.vat_total + self.delivery_fee
        print("\nWorld-of-Tomorrow Official Receipt")
        print(f'for Mr./Mrs. {delivery_info["full name"]}:')
        print("==================================================")
        print('DELIVERY ADDRESS:')
        print(f'House No: {delivery_info["house number"]}')
        print(f'Street: {delivery_info["street"]}')
        print(f'Subdivision: {delivery_info["subdivision"]}')
        print(f'Barangay: {delivery_info["barangay"]}')
        print(f'City: {delivery_info["city"]}')
        print(f'Region: {delivery_info["region"]}')
        print("==================================================")
        print('COMPONENTS:')
        for component in self.components:
            print(component)
        print("==================================================")
        print('CHARGES:')
        print(f'Initial Total: P{self.initial_total:.0f}')
        print(f'Delivery Fee: P{self.delivery_fee:.0f}')
        print(f'12% VAT Total: P{self.vat_total:.0f}')
        print("==================================================")
        print(f'TOTAL PRICE: P{total_price:.0f}')
        print("==================================================")
        print("\nThank you for shopping with World-of-Tomorrow!")
        print("Your receipt is also saved as a text file, please check your file manager.")
        input('\nPress Enter to continue.')


# Code initialization
def main():
    clear_screen()
    CheckoutSys()


if __name__ == "__main__":
    main()
