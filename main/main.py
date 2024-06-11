# Start
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
Select operation:
[1] Create your PC
[2] Track your order
[3] Saved builds
[4] Exit program

Operation: ''')
            if operation == '1':
                print("You have selected choice 1")

            elif operation == '2':
                print("You have selected choice 2")

            elif operation == '3':
                print("You have selected choice 3")

            elif operation == '4':
                break

            else:
                print("Invalid choice. Please try again.")

# Code initialization
def main():
    menu = MainMenu()

if __name__ == "__main__":
    main()

