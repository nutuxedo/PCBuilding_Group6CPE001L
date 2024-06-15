# Not yet integrated
# imports
import os
import time
from ComponentsSelection import *


# global functions
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


class CheckoutSys:
    def __init__(self):
        print("Hello World!")

# Code initialization
def main():
    clear_screen()
    CheckoutSys()


if __name__ == "__main__":
    main()
