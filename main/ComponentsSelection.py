# Components Selection menu
# Run this file for testing purposes
# imports
import os
import time


# Global Functions
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# Components
class CPUSel:
    # Convert this into a list or dictionary (dictionary done)
    # Add functionalities:
    # - When user already confirmed a CPU and wants to re-pick, user should see a selected CPU from the picker (hard)
    # - Make the variable accessible to PCSelectionMenu.py and others (done)
    #
    # When all functionalities done - REPEAT FOR THE OTHER COMPONENTS (done)
    # OPTIMIZE THIS WHOLE SECTION - TOO LONG
    def __init__(self):
        self.selected_cpu = None
        self.cpu_options = {
            "1": {'name': "Intel Core i9", 'price': 1000},
            "2": {'name': "Intel Core i5", 'price': 500},
            "3": {'name': "AMD Ryzen 9", 'price': 500},
            "4": {'name': "AMD Ryzen 5", 'price': 500}
        }
        while True:
            clear_screen()
            print("\nSelect your CPUs")
            select_cpu = input(f'''
    [1] Intel Core i9 - P1000
    [2] Intel Core i7 - P500
    [3] AMD Ryzen 9 - P500
    [4] AMD Ryzen 5 - P500

    [9] Remove component
    [10] Cancel

    Choice: ''')

            if select_cpu in self.cpu_options:
                self.selected_cpu = self.cpu_options[select_cpu]
                print(f'You have selected {self.selected_cpu["name"]} for P{self.selected_cpu["price"]}')
                confirmation = input("Would you like to confirm this CPU? (Y/n) ")
                if confirmation.lower() == "n":
                    self.selected_cpu = None
                    print('Confirmation cancelled.')
                    time.sleep(1)
                elif confirmation.lower() != 'y':
                    print('\nInvalid input! Please type y or n to confirm!')
                    time.sleep(1)
                else:
                    print(f'\nYou have confirmed {self.selected_cpu['name']} for P{self.selected_cpu['price']}.')
                    print('Returning to components list....')
                    time.sleep(1)
                    break
            elif select_cpu == "9":
                if self.selected_cpu is None:
                    print("\nYou have not selected a CPU!")
                    time.sleep(1)
                    continue
                else:
                    remove_confirmation = input("\nWould you like to remove the selected CPU? (Y/n)")
                    if remove_confirmation.lower() == "Y":
                        self.selected_cpu = None
                        print('CPU removed.')
                        time.sleep(1)
                        break
                    else:
                        continue
            elif select_cpu == "10":
                print("Cancelling operation...")
                time.sleep(1)
                break
            else:
                print("Wrong selection, please try again.")
                time.sleep(1)
                clear_screen()


class CPUCoolerSel:
    def __init__(self):
        self.selected_cooler = None
        self.cooler_options = {
            "1": {'name': "NZXT", 'price': 1000},
            "2": {'name': "Deepcooler", 'price': 500},
            "3": {'name': "Corsair", 'price': 500},
            "4": {'name': "Noctua", 'price': 500}
        }
        while True:
            clear_screen()
            print("\nSelect your CPU Coolers")
            select_cooler = input(f'''
    [1] NZXT - P1000
    [2] Deepcooler - P500
    [3] Corsair - P500
    [4] Noctua - P500

    [9] Remove component
    [10] Cancel

    Choice: ''')

            if select_cooler in self.cooler_options:
                self.selected_cooler = self.cooler_options[select_cooler]
                print(f'You have selected {self.selected_cooler["name"]} for P{self.selected_cooler["price"]}')
                confirmation = input("Would you like to confirm this CPU Cooler? (Y/n) ")
                if confirmation.lower() == "n":
                    self.selected_cooler = None
                    print('Confirmation cancelled.')
                elif confirmation.lower() != 'y':
                    print('\nInvalid input! Please type y or n to confirm!')
                    time.sleep(1)
                else:
                    print(f'\nYou have confirmed {self.selected_cooler['name']} for P{self.selected_cooler['price']}.')
                    print('Returning to components list....')
                    time.sleep(1)
                    break
            elif select_cooler == "9":
                if self.selected_cooler is None:
                    print("\nYou have not selected a CPU Cooler!")
                    time.sleep(1)
                    continue
                else:
                    remove_confirmation = input("\nWould you like to remove the selected CPU Cooler? (Y/n)")
                    if remove_confirmation.lower() == "n":
                        self.selected_cooler = None
                        print('CPU removed.')
                        time.sleep(1)
                        break
            elif select_cooler == "10":
                print("Cancelling operation...")
                time.sleep(1)
                break
            else:
                print("Wrong selection, please try again.")
                time.sleep(1)
                clear_screen()


class MoboSel:
    def __init__(self):
        self.selected_mobo = None
        self.mobo_options = {
            "1": {'name': "NZXT", 'price': 1000},
            "2": {'name': "Deepcooler", 'price': 500},
            "3": {'name': "Corsair", 'price': 500},
            "4": {'name': "Noctua", 'price': 500}
        }
        while True:
            clear_screen()
            print("\nSelect your Motherboards")
            select_cooler = input(f'''
    [1] NZXT - P1000
    [2] Deepcooler - P500
    [3] Corsair - P500
    [4] Noctua - P500

    [9] Remove component
    [10] Cancel

    Choice: ''')

            if select_cooler in self.mobo_options:
                self.selected_mobo = self.mobo_options[select_cooler]
                print(f'You have selected {self.selected_mobo["name"]} for P{self.selected_mobo["price"]}')
                confirmation = input("Would you like to confirm this CPU Cooler? (Y/n) ")
                if confirmation.lower() == "n":
                    self.selected_mobo = None
                    print('Confirmation cancelled.')
                elif confirmation.lower() != 'y':
                    print('\nInvalid input! Please type y or n to confirm!')
                    time.sleep(1)
                else:
                    print(f'\nYou have confirmed {self.selected_mobo['name']} for P{self.selected_mobo['price']}.')
                    print('Returning to components list....')
                    time.sleep(1)
                    break
            elif select_cooler == "9":
                if self.selected_mobo is None:
                    print("\nYou have not selected a CPU Cooler!")
                    time.sleep(1)
                    continue
                else:
                    remove_confirmation = input("\nWould you like to remove the selected CPU Cooler? (Y/n)")
                    if remove_confirmation.lower() == "n":
                        self.selected_mobo = None
                        print('CPU removed.')
                        time.sleep(1)
                        break
            elif select_cooler == "10":
                print("Cancelling operation...")
                time.sleep(1)
                break
            else:
                print("Wrong selection, please try again.")
                time.sleep(1)
                clear_screen()


class RAMSel:
    def __init__(self):
        self.selected_ram = None
        self.ram_options = {
            "1": {'name': "NZXT", 'price': 1000},
            "2": {'name': "Deepcooler", 'price': 500},
            "3": {'name': "Corsair", 'price': 500},
            "4": {'name': "Noctua", 'price': 500}
        }
        while True:
            clear_screen()
            print("\nSelect your CPU Coolers")
            select_cooler = input(f'''
    [1] NZXT - P1000
    [2] Deepcooler - P500
    [3] Corsair - P500
    [4] Noctua - P500

    [9] Remove component
    [10] Cancel

    Choice: ''')

            if select_cooler in self.ram_options:
                self.selected_ram = self.ram_options[select_cooler]
                print(f'You have selected {self.selected_ram["name"]} for P{self.selected_ram["price"]}')
                confirmation = input("Would you like to confirm this CPU Cooler? (Y/n) ")
                if confirmation.lower() == "n":
                    self.selected_ram = None
                    print('Confirmation cancelled.')
                elif confirmation.lower() != 'y':
                    print('\nInvalid input! Please type y or n to confirm!')
                    time.sleep(1)
                else:
                    print(f'\nYou have confirmed {self.selected_ram['name']} for P{self.selected_ram['price']}.')
                    print('Returning to components list....')
                    time.sleep(1)
                    break
            elif select_cooler == "9":
                if self.selected_ram is None:
                    print("\nYou have not selected a CPU Cooler!")
                    time.sleep(1)
                    continue
                else:
                    remove_confirmation = input("\nWould you like to remove the selected CPU Cooler? (Y/n)")
                    if remove_confirmation.lower() == "n":
                        self.selected_ram = None
                        print('CPU removed.')
                        time.sleep(1)
                        break
            elif select_cooler == "10":
                print("Cancelling operation...")
                time.sleep(1)
                break
            else:
                print("Wrong selection, please try again.")
                time.sleep(1)
                clear_screen()


class ROMSel:
    def __init__(self):
        self.selected_rom = None
        self.rom_options = {
            "1": {'name': "NZXT", 'price': 1000},
            "2": {'name': "Deepcooler", 'price': 500},
            "3": {'name': "Corsair", 'price': 500},
            "4": {'name': "Noctua", 'price': 500}
        }
        while True:
            clear_screen()
            print("\nSelect your CPU Coolers")
            select_cooler = input(f'''
    [1] NZXT - P1000
    [2] Deepcooler - P500
    [3] Corsair - P500
    [4] Noctua - P500

    [9] Remove component
    [10] Cancel

    Choice: ''')

            if select_cooler in self.rom_options:
                self.selected_rom = self.rom_options[select_cooler]
                print(f'You have selected {self.selected_rom["name"]} for P{self.selected_rom["price"]}')
                confirmation = input("Would you like to confirm this CPU Cooler? (Y/n) ")
                if confirmation.lower() == "n":
                    self.selected_rom = None
                    print('Confirmation cancelled.')
                elif confirmation.lower() != 'y':
                    print('\nInvalid input! Please type y or n to confirm!')
                    time.sleep(1)
                else:
                    print(f'\nYou have confirmed {self.selected_rom['name']} for P{self.selected_rom['price']}.')
                    print('Returning to components list....')
                    time.sleep(1)
                    break
            elif select_cooler == "9":
                if self.selected_rom is None:
                    print("\nYou have not selected a CPU Cooler!")
                    time.sleep(1)
                    continue
                else:
                    remove_confirmation = input("\nWould you like to remove the selected CPU Cooler? (Y/n)")
                    if remove_confirmation.lower() == "n":
                        self.selected_rom = None
                        print('CPU removed.')
                        time.sleep(1)
                        break
            elif select_cooler == "10":
                print("Cancelling operation...")
                time.sleep(1)
                break
            else:
                print("Wrong selection, please try again.")
                time.sleep(1)
                clear_screen()


class GPUSel:
    def __init__(self):
        self.selected_gpu = None
        self.gpu_options = {
            "1": {'name': "NZXT", 'price': 1000},
            "2": {'name': "Deepcooler", 'price': 500},
            "3": {'name': "Corsair", 'price': 500},
            "4": {'name': "Noctua", 'price': 500}
        }
        while True:
            clear_screen()
            print("\nSelect your CPU Coolers")
            select_cooler = input(f'''
    [1] NZXT - P1000
    [2] Deepcooler - P500
    [3] Corsair - P500
    [4] Noctua - P500

    [9] Remove component
    [10] Cancel

    Choice: ''')

            if select_cooler in self.gpu_options:
                self.selected_gpu = self.gpu_options[select_cooler]
                print(f'You have selected {self.selected_gpu["name"]} for P{self.selected_gpu["price"]}')
                confirmation = input("Would you like to confirm this CPU Cooler? (Y/n) ")
                if confirmation.lower() == "n":
                    self.selected_gpu = None
                    print('Confirmation cancelled.')
                elif confirmation.lower() != 'y':
                    print('\nInvalid input! Please type y or n to confirm!')
                    time.sleep(1)
                else:
                    print(f'\nYou have confirmed {self.selected_gpu['name']} for P{self.selected_gpu['price']}.')
                    print('Returning to components list....')
                    time.sleep(1)
                    break
            elif select_cooler == "9":
                if self.selected_gpu is None:
                    print("\nYou have not selected a CPU Cooler!")
                    time.sleep(1)
                    continue
                else:
                    remove_confirmation = input("\nWould you like to remove the selected CPU Cooler? (Y/n)")
                    if remove_confirmation.lower() == "n":
                        self.selected_gpu = None
                        print('CPU removed.')
                        time.sleep(1)
                        break
            elif select_cooler == "10":
                print("Cancelling operation...")
                time.sleep(1)
                break
            else:
                print("Wrong selection, please try again.")
                time.sleep(1)
                clear_screen()


class CaseSel:
    def __init__(self):
        self.selected_case = None
        self.case_options = {
            "1": {'name': "NZXT", 'price': 1000},
            "2": {'name': "Deepcooler", 'price': 500},
            "3": {'name': "Corsair", 'price': 500},
            "4": {'name': "Noctua", 'price': 500}
        }
        while True:
            clear_screen()
            print("\nSelect your CPU Coolers")
            select_cooler = input(f'''
        [1] NZXT - P1000
        [2] Deepcooler - P500
        [3] Corsair - P500
        [4] Noctua - P500

        [9] Remove component
        [10] Cancel

    Choice: ''')

            if select_cooler in self.case_options:
                self.selected_case = self.case_options[select_cooler]
                print(f'You have selected {self.selected_case["name"]} for P{self.selected_case["price"]}')
                confirmation = input("Would you like to confirm this CPU Cooler? (Y/n) ")
                if confirmation.lower() == "n":
                    self.selected_case = None
                    print('Confirmation cancelled.')
                elif confirmation.lower() != 'y':
                    print('\nInvalid input! Please type y or n to confirm!')
                    time.sleep(1)
                else:
                    print(f'\nYou have confirmed {self.selected_case['name']} for P{self.selected_case['price']}.')
                    print('Returning to components list....')
                    time.sleep(1)
                    break
            elif select_cooler == "9":
                if self.selected_case is None:
                    print("\nYou have not selected a CPU Cooler!")
                    time.sleep(1)
                    continue
                else:
                    remove_confirmation = input("\nWould you like to remove the selected CPU Cooler? (Y/n)")
                    if remove_confirmation.lower() == "n":
                        self.selected_case = None
                        print('CPU removed.')
                        time.sleep(1)
                        break
            elif select_cooler == "10":
                print("Cancelling operation...")
                time.sleep(1)
                break
            else:
                print("Wrong selection, please try again.")
                time.sleep(1)
                clear_screen()


class PSUSel:
    def __init__(self):
        self.selected_psu = None
        self.psu_options = {
            "1": {'name': "NZXT", 'price': 1000},
            "2": {'name': "Deepcooler", 'price': 500},
            "3": {'name': "Corsair", 'price': 500},
            "4": {'name': "Noctua", 'price': 500}
        }
        while True:
            clear_screen()
            print("\nSelect your CPU Coolers")
            select_cooler = input(f'''
    [1] NZXT - P1000
    [2] Deepcooler - P500
    [3] Corsair - P500
    [4] Noctua - P500

    [9] Remove component
    [10] Cancel

    Choice: ''')

            if select_cooler in self.psu_options:
                self.selected_psu = self.psu_options[select_cooler]
                print(f'You have selected {self.selected_psu["name"]} for P{self.selected_psu["price"]}')
                confirmation = input("Would you like to confirm this CPU Cooler? (Y/n) ")
                if confirmation.lower() == "n":
                    self.selected_psu = None
                    print('Confirmation cancelled.')
                elif confirmation.lower() != 'y':
                    print('\nInvalid input! Please type y or n to confirm!')
                    time.sleep(1)
                else:
                    print(f'\nYou have confirmed {self.selected_psu['name']} for P{self.selected_psu['price']}.')
                    print('Returning to components list....')
                    time.sleep(1)
                    break
            elif select_cooler == "9":
                if self.selected_psu is None:
                    print("\nYou have not selected a CPU Cooler!")
                    time.sleep(1)
                    continue
                else:
                    remove_confirmation = input("\nWould you like to remove the selected CPU Cooler? (Y/n)")
                    if remove_confirmation.lower() == "n":
                        self.selected_psu = None
                        print('CPU removed.')
                        time.sleep(1)
                        break
            elif select_cooler == "10":
                print("Cancelling operation...")
                time.sleep(1)
                break
            else:
                print("Wrong selection, please try again.")
                time.sleep(1)
                clear_screen()


# Code initialization for running/testing
def main():
    while True:
        clear_screen()
        print("\nDIAGNOSTICS\nSelect a menu to test:")
        choice = input('''
        [1] CPU
        [2] CPU Cooler
        [3] Mobo
        [4] RAM
        [5] ROM
        [6] GPU
        [7] Case
        [8] PSU
        
        [9] Stop program
        
        Choice: ''')
        if choice == "1":
            CPUSel()
        elif choice == '2':
            CPUCoolerSel()
        elif choice == '3':
            MoboSel()
        elif choice == "4":
            RAMSel()
        elif choice == '5':
            ROMSel()
        elif choice == '6':
            GPUSel()
        elif choice == '7':
            CaseSel()
        elif choice == '8':
            PSUSel()
        elif choice == '9':
            print("\nStopping")
            break
        else:
            print("\nWrong value")
            time.sleep(1)


if __name__ == "__main__":
    main()
