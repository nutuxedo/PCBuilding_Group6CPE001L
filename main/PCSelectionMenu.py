# imports
import os
import time
from ComponentsSelection import *


# Global functions

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# the PC Parts creator system - main menu
class PCPartsCreatorMenu:
    def __init__(self):
        self.selected_cpu = None
        self.selected_cooler = None
        self.selected_mobo = None
        self.selected_ram = None
        self.selected_rom = None
        self.selected_gpu = None
        self.selected_case = None
        self.selected_psu = None
        self.run()

    def run(self):
        while True:
            clear_screen()
            print('\nWelcome to the PC Selection menu')
            components = input('''Select your components to add/replace:

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
                cpu = CPUSel()
                self.selected_cpu = cpu.selected_cpu

            elif components == '2':
                cooler = CPUCoolerSel()
                self.selected_cooler = cooler.selected_cooler

            elif components == '3':
                mobo = MoboSel()
                self.selected_mobo = mobo.selected_mobo

            elif components == '4':
                ram = RAMSel()
                self.selected_ram = ram.selected_ram

            elif components == '5':
                rom = ROMSel()
                self.selected_rom = rom.selected_rom

            elif components == '6':
                gpu = GPUSel()
                self.selected_gpu = gpu.selected_gpu

            elif components == '7':
                case = CaseSel()
                self.selected_case = case.selected_case

            elif components == '8':
                psu = PSUSel()
                self.selected_psu = psu.selected_psu

            elif components == '9':
                print('\nSave/Load build function soon')
                time.sleep(1)

            elif components == '10':
                while True:  # Checkout system - modularize this to its own file (WIP @ CheckoutSystem.py)
                    clear_screen()
                    total_cost = 0
                    print('\nCheckout cart')
                    print('---------------------')
                    if self.selected_cpu:
                        print(f'CPU: {self.selected_cpu["name"]} - P{self.selected_cpu["price"]}')
                        total_cost += self.selected_cpu["price"]
                    else:
                        print("CPU: Not selected")
                    if self.selected_cooler:
                        print(f'CPU Cooler: {self.selected_cooler["name"]} - P{self.selected_cooler["price"]}')
                        total_cost += self.selected_cooler["price"]
                    else:
                        print("CPU Cooler: Not selected")
                    if self.selected_mobo:
                        print(f'Motherboard: {self.selected_mobo["name"]} - P{self.selected_mobo["price"]}')
                        total_cost += self.selected_mobo["price"]
                    else:
                        print("Motherboard: Not selected")
                    if self.selected_ram:
                        print(f'Memory: {self.selected_ram["name"]} - P{self.selected_ram["price"]}')
                        total_cost += self.selected_ram["price"]
                    else:
                        print("Memory: Not selected")
                    if self.selected_rom:
                        print(f'Storage: {self.selected_rom["name"]} - P{self.selected_rom["price"]}')
                        total_cost += self.selected_rom["price"]
                    else:
                        print("Storage: Not selected")
                    if self.selected_gpu:
                        print(f'GPU: {self.selected_gpu["name"]} - P{self.selected_gpu["price"]}')
                        total_cost += self.selected_gpu["price"]
                    else:
                        print("GPU: Not selected")
                    if self.selected_case:
                        print(f'Case: {self.selected_case["name"]} - P{self.selected_case["price"]}')
                        total_cost += self.selected_case["price"]
                    else:
                        print("Case: Not selected")
                    if self.selected_psu:
                        print(f'Power Supply: {self.selected_psu["name"]} - P{self.selected_psu["price"]}')
                        total_cost += self.selected_psu["price"]
                    else:
                        print("Power Supply: Not selected")
                    print("---------------")
                    print(f"\nInitial Total: P{total_cost}")
                    chkout_selection = input('''To replace one or more components, go back and select the component/s.\n
    [9] Back
    [10] Clear all components
    [Enter] Continue to checkout
                    
Choice: ''')
                    if chkout_selection == "9":
                        break
                    elif chkout_selection == "10":
                        while True:
                            clear_screen()
                            chkout_clear_confirmation = input("Are you sure that you want to clear your cart? (y/n) ")
                            if chkout_clear_confirmation.lower() == "y":
                                self.selected_cpu = None
                                self.selected_cooler = None
                                self.selected_mobo = None
                                self.selected_ram = None
                                self.selected_rom = None
                                self.selected_gpu = None
                                self.selected_case = None
                                self.selected_psu = None
                                print("Cart cleared. Returning to menu.")
                                time.sleep(1)
                                break
                            elif chkout_clear_confirmation.lower() == "n":
                                break
                            else:
                                print('Invalid choice. Please try again.')
                                time.sleep(1)
                    elif chkout_selection == '':
                        print('Proceeding to checkout....')
                        time.sleep(1)
                        break
                    else:
                        print("Invalid choice, please try again.")
                        time.sleep(1)

            elif components == '0':
                print('\nAre you sure that you want to go back to the main menu?')
                confirmation = input("Doing this will lose all of your pending items! (Y/n) ")
                if confirmation.lower() == "n":
                    continue
                else:
                    clear_screen()
                    print('Ending services...')
                    time.sleep(2)
                    print('Returning to the main menu...')
                    time.sleep(2)
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
