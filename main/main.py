# Start
# imports
from PCPartsCreator import PCPartsCreator
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

# Main menu class

class MainMenu():
    def __init__(self): # Main menu
        while True:
            operation = input('''
Welcome to Build-Your-PC!
Please, select your choice:
    
    [1] Create your PC
    [2] Track your order
    [3] Saved builds
    [4] Exit program

Choice: ''')
            if operation == '1':
                print("You have selected choice 1")
                time.sleep(2)
                print('Launching PC Parts Creator system....')
                time.sleep(3)
                PCPartsCreator()

            elif operation == '2':
                print("You have selected choice 2")

            elif operation == '3':
                print("You have selected choice 3")

            elif operation == '4':
                print("Thank you for using our service! Hope to see you again!")
                print('Exiting service...')
                time.sleep(1)
                break

            else:
                print("Invalid choice. Please try again.")

# Code initialization
def main():
    print("Launching service...")
    time.sleep(3)
    menu = MainMenu()

if __name__ == "__main__":
    main()

