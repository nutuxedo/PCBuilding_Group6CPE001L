# experimentation grounds
# for colored text
from colorama import Fore, Back, Style

print(Fore.BLACK + 'some black text')
print(Back.YELLOW + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')

