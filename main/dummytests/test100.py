# assign list
list1 = ['Geeks', 'for', 'Geeks?']


# open file
with open('gfg.txt', 'w+') as f:
    # write elements of list
    f.write('========================================\n')
    f.write('Build-Your-PC Service Official Receipt\n========================================\n')
    f.write(f'CPU:\n')
    f.write(f'CPU Cooler:\n')
    f.write(f'Motherboard:\n')
    f.write(f'Memory:\n')
    f.write(f'Storage:\n')
    f.write(f'Graphics Card:\n')
    f.write(f'Case:\n')
    f.write(f'Power Supply:\n')

    for items in list1:
        f.write('%s\n' % items)

    print("File written successfully")

# close the file
f.close()
