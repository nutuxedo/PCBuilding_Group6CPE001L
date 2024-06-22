# Initialize an empty dictionary
my_dict = {}

print("Enter key-value pairs (key:value). Type 'exit' to finish.")

while True:
    # Prompt user for input
    user_input = input("Enter key:value pair: ")

    # Check if the user wants to exit
    if user_input.lower() == 'exit':
        break

    # Split the input to get the key and value
    try:
        key, value = user_input.split(":")
        # Add the key-value pair to the dictionary
        my_dict[key.strip()] = value.strip()
    except ValueError:
        print("Invalid format. Please enter in key:value format.")

# Display the final dictionary
print("Final dictionary:", my_dict)