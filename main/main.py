# v0.2.0dev
# imports
import os
from PCSelectionMenu import PCPartsCreatorMenu
import time

# Ideas here:
# Check document for components and prices for reference
'''
Main menu here
 - add most popular pc builds
 - create-your-pc picker
 - credentials
 - track your order (from receipt)
 - exit program
'''


# Global functions

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# Main menu class

class MainMenu:
    def __init__(self):  # Main menu
        while True:
            clear_screen()
            operation = input('''
Welcome to Build-Your-PC!
Please, select your choice:
    
    [1] Create your PC
    [2] Track your order
    [3] Saved builds
    [4] Exit program
    [5] About

Choice: ''')
            if operation == '1':
                print("You have selected choice 1")
                time.sleep(1)
                clear_screen()
                print('Launching PC Selection menu....')
                time.sleep(3)
                PCPartsCreatorMenu()

            elif operation == '2':
                print("You have selected choice 2")
                time.sleep(1)
                clear_screen()

            elif operation == '3':
                print("You have selected choice 3")
                time.sleep(1)
                clear_screen()

            elif operation == '4':
                exit_program = input('Are you sure you want to exit the program? (y/n) ')
                if exit_program == "y":
                    print("\nThank you for using our service! Hope to see you again!")
                    print('Exiting service...')
                    time.sleep(1)
                    break

            elif operation == '5':
                clear_screen()
                print('\nBuild-Your-PC')
                print('v0.2.0dev')
                input('''\nProgram created by these authors:

Vizconde, Rafael Jose G.
Perias, Anthony
Braga, Rovic Jay

Thank you for using this service!

Press Enter to go back to the main menu...''')

            elif operation == '':
                print('Please enter a value.')
                time.sleep(1)

            else:
                print("Invalid choice. Please try again.")
                time.sleep(1)
                continue


# Code initialization
def main():
    clear_screen()
    print("Launching service...")
    time.sleep(3)
    MainMenu()


if __name__ == "__main__":
    main()
