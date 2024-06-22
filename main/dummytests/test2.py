def main():
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

main()