# imports
import os
import time
from ComponentsSelection import CPUSel


# Global functions

def clear_screen():
    os.system('clear')


# Components here
class CPUs:

    # This is temporary, going to find a way on how to optimize this code
    # planning this to turn this into a list/dictionary on a different python file
    # For now, this would do
    def __init__(self):
        self.selected_cpu = None
        while True:
            clear_screen()
            print("\nSelect your CPUs")
            select_cpu = input('''
    [1] Intel Core i9
    [2] Intel Core i7
    [3] AMD Ryzen 9
    [4] AMD Ryzen 5
    
    [5] Cancel

Choice: ''')

            if select_cpu == "1":
                self.selected_cpu = 'Intel Core i9'
                print(f'You have selected {self.selected_cpu}')
                confirmation = input("Would you like to confirm this CPU? (Y/n) ")
                if confirmation == "n":
                    self.selected_cpu = None
                    print('Confirmation cancelled.')
                else:
                    break
            elif select_cpu == "2":
                self.selected_cpu = 'Intel Core i7'
                print(f'You have selected {self.selected_cpu}')
                confirmation = input("Would you like to confirm this CPU? (Y/n) ")
                if confirmation == "n":
                    self.selected_cpu = None
                    print('Confirmation cancelled.')
                else:
                    break
            elif select_cpu == "3":
                self.selected_cpu = 'AMD Ryzen 9'
                print(f'You have selected {self.selected_cpu}')
                confirmation = input("Would you like to confirm this CPU? (Y/n) ")
                if confirmation == "n":
                    self.selected_cpu = None
                    print('Confirmation cancelled.')
                else:
                    break
            elif select_cpu == "4":
                self.selected_cpu = 'AMD Ryzen 5'
                print(f'You have selected {self.selected_cpu}')
                confirmation = input("Would you like to confirm this CPU? (Y/n) ")
                if confirmation == "n":
                    self.selected_cpu = None
                    print('Confirmation cancelled.')
                else:
                    break
            elif select_cpu == "5":
                print("Cancelling operation...")
                time.sleep(1)
                break
            else:
                print("Wrong selection, please try again.")
                time.sleep(1)
                clear_screen()


# the PC Parts creator system - main menu
class PCPartsCreatorMenu:
    def __init__(self):
        self.selected_cpu = None
        self.run()

    def run(self):
        while True:
            clear_screen()
            print('\nWelcome to PC Parts Creator!')
            components = input('''Select your components to add/remove:

    [1] CPU
    [2] CPU Cooler
    [3] Motherboard
    [4] Memory
    [5] Storage
    [6] Video Card
    [7] Case
    [8] Power Supply
     
    [9] Save/Load build        
    [10] Checkout
    [0] Back to main menu
    
    Choice: ''')

            if components == '1':
                cpu = CPUs()
                self.selected_cpu = cpu.selected_cpu

            elif components == '2':
                print("\nSelect your Cooler:")
                # Cooler Class here

            elif components == '3':
                print("\nSelect your Motherboard")
                # MBoard Class here

            elif components == '4':
                print("\nSelect your Memory")
                # RAM Class here

            elif components == '5':
                print("\nSelect your Storage")
                # ROM Class here

            elif components == '6':
                print("\nSelect your Video Card")
                # GPU Class here

            elif components == '7':
                print("\nSelect your Case")
                # Case Class here

            elif components == '8':
                print("\nSelect your Power Supply")
                # PSU Class here

            elif components == '9':
                print('\nSave/Load build function soon')
                time.sleep(1)

            elif components == '10':
                while True:
                    clear_screen()
                    print('\nCheckout')
                    if self.selected_cpu:
                        print(f'CPU: {self.selected_cpu}')
                    else:
                        print("CPU: Not selected")
                    input('\nPress Enter to continue.')
                    break

            elif components == '0':
                print('\nAre you sure that you want to go back to the main menu?')
                confirmation = input("Doing this will lose all of your pending items! (Y/n) ")
                if confirmation == "n":
                    continue
                else:
                    clear_screen()
                    break

            elif components == '':
                print('\nPlease enter a value.')
                time.sleep(1)

            else:
                print("Invalid choice. Please try again.")


# Code initialization

def main():
    PCPartsCreatorMenu()


if __name__ == "__main__":
    main()
