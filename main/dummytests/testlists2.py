my_list = []

print("Enter strings to add to the list. Type 'exit' to finish.")

while True:
    # Prompt user for input
    user_input = input("Enter a string: ")

    # Check if the user wants to exit
    if user_input.lower() == 'exit':
        break

    # Add the entered string to the list
    my_list.append(user_input)

# Display the final list
print("Final list:", my_list)