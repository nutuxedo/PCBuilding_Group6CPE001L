class PCPartsCreator():
    def __init__(self):
        while True:
            print('Welcome to PC Parts Creator!')
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
            ''')

            if components == '1':
                print("Select your CPUs")
                # CPU Class here

            elif components == '2':
                print("Select your Cooler:")
                # Cooler Class here

            elif components == '3':
                print("Select your Motherboard")
                # MBoard Class here

            elif components == '4':
                print("Select your Memory")
                # RAM Class here

            elif components == '5':
                print("Select your Storage")
                # ROM Class here

            elif components == '6':
                print("Select your Video Card")
                # GPU Class here

            elif components == '7':
                print("Select your Case")
                # Case Class here

            elif components == '8':
                print("Select your Power Supply")
                # PSU Class here

            elif components == '10':
                print('Checkout')
                # Checkout Class here

            elif components == '0':
                break

            else:
                print("Invalid choice. Please try again.")