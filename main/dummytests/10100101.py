# Define a list of products and their respective prices per unit
import os
components = [
    ('CPU', 'Intel', 300),
    ('CPU Cooler', 'Intel Cooler', 50),
    ('Motherboard', 'MSI Board', 150),
    ('Memory', 'Kingston', 100),
    ('Storage', 'Seagate', 200),
    ('Graphics Card', 'RTX', 500),
    ('Case', 'ATX', 100),
    ('Power Supply', 'Corsair', 120)
]

# Open file
with open('gfg.txt', 'w+') as f:
    # Write the header
    f.write('========================================\n')
    f.write('World of Tomorrow Service Official Receipt\n========================================\n')

    total_price = 0

    # Write the product details and calculate total price
    for product, brand, price in components:
        f.write(f'{product}: {brand}\nP{price}\n')
        total_price += price

    f.write('========================================\n')
    f.write(f'Total Price: P{total_price}\n')
    f.close()

    print("File written successfully")
    confirm = input("Open? (Y/n) ")
    if confirm.lower() == 'y':
        f = open('gfg.txt', 'r')
        read_file = f.read()
        print(read_file)
        print("Work")
        input()
        f.close()
    else:
        print("Test")