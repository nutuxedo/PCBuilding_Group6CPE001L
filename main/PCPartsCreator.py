# imports
import os
import time

# Components here
class CPUs:
    # This is temporary, going to find a way on how to optimize this code
    # planning this to turn this into a list/dictionary on a different python file
    # For now, this would do
    def __init__(self):
        while True:
            os.system('clear')
            selected_cpu = ''
            print("\nSelect your CPUs")
            select_cpu = input('''
    [1] Intel Core i9
    [2] Intel Core i7
    [3] AMD Ryzen 9
    [4] AMD Ryzen 5
    
    [5] Cancel

Choice: ''')

            if select_cpu == "1":
                selected_cpu = 'Intel Core i9'
                print(f'You have selected {selected_cpu}')
                confirmation = input("Would you like to confirm this CPU? (Y/n) ")
                if confirmation == "n":
                    selected_cpu = ""
                    print('Confirmation cancelled.')
                else:
                    break
            elif select_cpu == "2":
                selected_cpu = 'Intel Core i7'
                print(f'You have selected {selected_cpu}')
                confirmation = input("Would you like to confirm this CPU? (Y/n) ")
                if confirmation == "n":
                    selected_cpu = ""
                    print('Confirmation cancelled.')
                else:
                    break
            elif select_cpu == "3":
                selected_cpu = 'AMD Ryzen 9'
                print(f'You have selected {selected_cpu}')
                confirmation = input("Would you like to confirm this CPU? (Y/n) ")
                if confirmation == "n":
                    selected_cpu = ""
                    print('Confirmation cancelled.')
                else:
                    break
            elif select_cpu == "4":
                selected_cpu = 'AMD Ryzen 5'
                print(f'You have selected {selected_cpu}')
                confirmation = input("Would you like to confirm this CPU? (Y/n) ")
                if confirmation == "n":
                    selected_cpu = ""
                    print('Confirmation cancelled.')
                else:
                    break
            elif select_cpu == "5":
                print("Cancelling operation...")
                print(f'You have selected {selected_cpu}')
                confirmation = input("Would you like to confirm this CPU? (Y/n) ")
                if confirmation == "n":
                    selected_cpu = ""
                    print('Confirmation cancelled.')
                else:
                    break
            else:
                print("Wrong selection, please try again.")
                time.sleep(1)
                os.system('clear')

# the PC Parts creator system
class PCPartsCreator:
    def __init__(self):
        while True:
            os.system('clear')
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
            
    [10] Checkout
    [0] Back to main menu
    
    Choice: ''')

            if components == '1':
                CPUs()

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

            elif components == '10':
                print('\nCheckout')
                print(CPUs)

            elif components == '0':
                print('\nAre you sure that you want to go back to the main menu?')
                confirmation = input("Doing this will lose all of your pending items! (Y/n) ")
                if confirmation == "n":
                    continue
                else:
                    os.system('clear')
                    break

            elif components == '':
                print('\nPlease enter a value.')
                time.sleep(1)

            else:
                print("Invalid choice. Please try again.")


# Code initialization

def main():
    PCPartsCreator()


if __name__ == "__main__":
    main()
