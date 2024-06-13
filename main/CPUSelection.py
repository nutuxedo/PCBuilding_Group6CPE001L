# CPU Selection menu
# imports
import os
import time


# Global Functions
def clear_screen():
    os.system('clear')


# Main class
class CPUSel:
    # Convert this into a list or dictionary (dictionary done)
    # Add functionalities:
    # - When user already confirmed a CPU and wants to re-pick, user should see a selected CPU from the picker
    # - Make the variable accessible to PCPartsCreatorMenu.py and others
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

        [5] Cancel

    Choice: ''')

            if select_cpu in self.cpu_options:
                self.selected_cpu = self.cpu_options[select_cpu]
                print(f'You have selected {self.selected_cpu["name"]} for P{self.selected_cpu["price"]}')
                confirmation = input("Would you like to confirm this CPU? (Y/n) ")
                if confirmation.lower() == "n":
                    self.selected_cpu = None
                    print('Confirmation cancelled.')
                else:
                    print(f'You have confirmed {self.selected_cpu['name']} for P{self.selected_cpu['price']}.')
                    print('Returning to components list....')
                    time.sleep(1)
                    break
            elif select_cpu == "5":
                print("Cancelling operation...")
                time.sleep(1)
                break
            else:
                print("Wrong selection, please try again.")
                time.sleep(1)
                clear_screen()


# Code initialization for running
def main():
    CPUSel()


if __name__ == "__main__":
    main()
