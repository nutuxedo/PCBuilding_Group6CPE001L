# lol CHATGPT code here for reference
class PCBuilder:
    def __init__(self):
        self.components = {
            'CPU': {'i5': 200, 'i7': 300, 'Ryzen 5': 250, 'Ryzen 7': 350},
            'GPU': {'GTX 1650': 250, 'GTX 1660': 300, 'RTX 2060': 400, 'RTX 3070': 600},
            'RAM': {'8GB': 100, '16GB': 150, '32GB': 300},
            'Storage': {'256GB SSD': 80, '500GB SSD': 120, '1TB SSD': 200}
        }
        self.cart = {}

    def select_component(self, category):
        print(f"Available {category}s:")
        options = self.components[category]
        for option, price in options.items():
            print(f"{option}: ${price}")

        choice = input(f"Select a {category} from the options above: ")
        while choice not in options:
            print("Invalid choice. Please select from the options provided.")
            choice = input(f"Select a {category} from the options above: ")

        self.cart[category] = {'component': choice, 'price': options[choice]}

    def checkout(self):
        print("Selected Components:")
        total_cost = 0
        for category, details in self.cart.items():
            print(f"{category}: {details['component']} - ${details['price']}")
            total_cost += details['price']

        print(f"Total: ${total_cost}")


def main():
    builder = PCBuilder()

    print("Welcome to our PC Building Service!")
    builder.select_component('CPU')
    builder.select_component('GPU')
    builder.select_component('RAM')
    builder.select_component('Storage')

    print("\nYour PC Configuration:")
    builder.checkout()


if __name__ == "__main__":
    main()
