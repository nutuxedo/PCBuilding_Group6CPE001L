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
            "1": {'name': "Intel Core i7 13700k", 'price': 20000},
            "2": {'name': "Intel Core i5 13600k", 'price': 15000},
            "3": {'name': "AMD Ryzen 7 7700x", 'price': 18000},
            "4": {'name': "AMD Ryzen 5 7600x", 'price': 10000}
        }
        while True:
            clear_screen()
            print("\nSelect your CPU")
            select_cpu = input(f'''
    [1] Intel Core i7 13700k - P20,000
    [2] Intel Core i5 13600k - P15,000
    [3] AMD Ryzen 7 7700x    - P18,000
    [4] AMD Ryzen 5 7600x    - P10,000

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
            "1": {'name': "NZXT KRAKEN 240 AIO", 'price': 9000},
            "2": {'name': "Deepcool AK500", 'price': 3600},
            "3": {'name': "Corsair iCUE H100i", 'price': 9800},
            "4": {'name': "Noctua NH-D15 Chromax", 'price': 7300}
        }
        while True:
            clear_screen()
            print("\nSelect your CPU Cooler")
            select_cooler = input(f'''
    [1] NZXT KRAKEN 240 AIO     - P9,000
    [2] Deepcool AK500          - P3,600
    [3] Corsair iCUE H100i      - P9,800
    [4] Noctua NH-D15 Chromax   - P7,300

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
            "1": {'name': "MSI MAG B450M MORTAR MAX", 'price': 7000},
            "2": {'name': "ASUS TUF B660M-Plus WiFi D4", 'price': 9700},
            "3": {'name': "GIGABYTE H510M-H MATX", 'price': 3750},
            "4": {'name': "ASRock B550M Pro", 'price': 5650}
        }
        while True:
            clear_screen()
            print("\nSelect your Motherboard")
            select_cooler = input(f'''
    [1] MSI MAG B450M MORTAR MAX    - P7,000
    [2] ASUS TUF B660M-Plus WiFi D4 - P9,700
    [3] GIGABYTE H510M-H MATX       - P3,750
    [4] ASRock B550M Pro            - P5,650

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
            "1": {'name': "Corsair Dominator Platinum 32GB (2x16GB)", 'price': 9500},
            "2": {'name': "G.Skill Ripjaws S5 32GB (2x16GB)", 'price': 6950},
            "3": {'name': "TEAMGROUP T-Force Vulkan 16GB (2x8GB)", 'price': 2250},
            "4": {'name': "Kingston Fury Beast 16GB (2x8GB)", 'price': 3150}
        }
        while True:
            clear_screen()
            print("\nSelect your Memory")
            select_cooler = input(f'''
    [1] Corsair Dominator Platinum 32GB (2x16GB) - P9,500
    [2] G.Skill Ripjaws S5 32GB (2x16GB)         - P6,950
    [3] TEAMGROUP T-Force Vulkan 16GB (2x8GB)    - P2,250
    [4] Kingston Fury Beast 16GB (2x8GB)         - P3,150

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
            "1": {'name': "Samsung 980 1TB NVMe M.2", 'price': 5000},
            "2": {'name': "Kingston Fury Renegade 1TB NVMe M.2", 'price': 6300},
            "3": {'name': "Western Digital SN350 500GB NVMe M.2", 'price': 2250},
            "4": {'name': "Seagate SKYHAWK 1TB SATA", 'price': 3100}
        }
        while True:
            clear_screen()
            print("\nSelect your Storage")
            select_cooler = input(f'''
    [1] Samsung 980 1TB NVMe M.2                - P5,000
    [2] Kingston Fury Renegade 1TB NVMe M.2     - P6,300
    [3] Western Digital SN350 500GB NVMe M.2    - P2,250
    [4] Seagate SKYHAWK 1TB SATA                - P3,100

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
            "1": {'name': "Gigabyte GeForce RTX 4070Ti Aero OC V2 12GB GDDR6X", 'price': 50000},
            "2": {'name': "ZOTAC Gaming GeForce RTX 3060 Twin Edge 8GB GDDR6", 'price': 16000},
            "3": {'name': "Sapphire Pure AMD Radeon RX7700XT 12GB GDDR6", 'price': 28700},
            "4": {'name': "AORUS Radeon RX 5700 XT 8GB GDDR6", 'price': 23000}
        }
        while True:
            clear_screen()
            print("\nSelect your GPU")
            select_cooler = input(f'''
    [1] Gigabyte GeForce RTX 4070Ti Aero OC V2 12GB GDDR6X - P50,000
    [2] ZOTAC Gaming GeForce RTX 3060 Twin Edge 8GB GDDR6  - P16,000
    [3] Sapphire Pure AMD Radeon RX7700XT 12GB GDDR6       - P28,700
    [4] AORUS Radeon RX 5700 XT 8GB GDDR6                  - P23,000

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
            "1": {'name': "NZXT H510 ATX Gaming Case", 'price': 4800},
            "2": {'name': "Lian Li O11 Vision ATX Mid-Tower", 'price': 8400},
            "3": {'name': "Corsair 2500X Mid-Tower Dual Chamber", 'price': 8300},
            "4": {'name': "Cooler Master Qube 500 Flatpack Mid-Tower ATX", 'price': 4600}
        }
        while True:
            clear_screen()
            print("\nSelect your Case")
            select_cooler = input(f'''
    [1] NZXT H510 ATX Gaming Case                     - P4,800
    [2] Lian Li O11 Vision ATX Mid-Tower              - P8,400
    [3] Corsair 2500X Mid-Tower Dual Chamber          - P8,300
    [4] Cooler Master Qube 500 Flatpack Mid-Tower ATX - P4,600

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
            "1": {'name': "Corsair RM1200X 1200W Gold Fully-Modular ATX", 'price': 14000},
            "2": {'name': "MSI MAG A850GL Gold 850W ATX", 'price': 6300},
            "3": {'name': "Cooler Master MWE Gold 750W Full Modular", 'price': 5700},
            "4": {'name': "be quiet! Straight Power 11 Gold 850W Full Modular", 'price': 7800}
        }
        while True:
            clear_screen()
            print("\nSelect your Power Supply")
            select_cooler = input(f'''
    [1] Corsair RM1200X 1200W Gold Fully-Modular ATX       - P14,000
    [2] MSI MAG A850GL Gold 850W ATX                       - P6,300
    [3] Cooler Master MWE Gold 750W Full Modular           - P5,700
    [4] be quiet! Straight Power 11 Gold 850W Full Modular - P7,800

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
