products = {
    "IT Products": [
        ("Laptop", 1000),
        ("Smartphone", 600),
        ("Headphones", 150),
        ("Keyboard", 50),
        ("Monitor", 300),
        ("Mouse", 25),
        ("Printer", 120),
        ("USB Drive", 15)
    ],
    "Electronics": [
        ("Smart TV", 800),
        ("Bluetooth Speaker", 120),
        ("Camera", 500),
        ("Smartwatch", 200),
        ("Home Theater", 700),
        ("Gaming Console", 450)
    ],
    "Groceries": [
        ("Milk", 2),
        ("Bread", 1.5),
        ("Eggs", 3),
        ("Rice", 10),
        ("Chicken", 12),
        ("Fruits", 6),
        ("Vegetables", 5),
        ("Snacks", 8)
    ]
}

def display_categories():
    categories = list(products.keys())
    for idx, category in enumerate(categories, 1):
        print(f"{idx}. {category}")
    try:
        category_choice = int(input("Please select a category by entering the corresponding number: "))
        if 1 <= category_choice <= len(categories):
            return category_choice - 1
        else:
            return None
    except ValueError:
        return None


def display_products(products_list):
    for idx, (product, price) in enumerate(products_list, 1):
        print(f"{idx}. {product} - ${price}")

def display_sorted_products(products_list, sort_order):
    reverse = True if sort_order == "desc" else False
    sorted_list = sorted(products_list, key=lambda x: x[1], reverse=reverse)
    return sorted_list

def add_to_cart(cart, product, quantity):
    cart.append((product[0], product[1], quantity))


def display_cart(cart):
    total_cost = 0
    output = []
    for (product_name, price, quantity) in cart:
        total_price = price * quantity
        total_cost += total_price
        output.append(f"{product_name} - ${price} x {quantity} = ${total_price}")
    print("\n".join(output))
    print(f"Total cost: ${total_cost}")


def generate_receipt(name, email, cart, total_cost, address):
    print("\n----- Receipt -----")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print("\nItems Purchased:")
    for item in cart:
        product_name, price, quantity = item
        total_price = price * quantity
        print(f"{product_name} - ${price} x {quantity} = ${total_price}")
    print(f"\nTotal Cost: ${total_cost}")
    print(f"Delivery Address: {address}")
    print("\nYour items will be delivered in 3 days.")
    print("Payment will be accepted after successful delivery.")
    print("--------------------")

def validate_name(name):
    parts = name.strip().split()
    if len(parts) != 2:
        return False
    first_name, last_name = parts
    if not (first_name.isalpha() and last_name.isalpha()):
        return False
    return True

def validate_email(email):
    return "@" in email


def main():
    while True:
        name = input("Please enter your full name (First and Last Name): ")
        if validate_name(name):
            break
        else:
            print("Invalid name. Please enter a valid name with only alphabets and a first and last name.")

    while True:
        email = input("Please enter your email address: ")
        if validate_email(email):
            break
        else:
            print("Invalid email address. Please include an '@' symbol in your email.")

    cart = []
    total_cost = 0

    while True:
        print("\nAvailable Categories:")
        category_index = display_categories()
        if category_index is None:
            print("Invalid category selection. Please try again.")
            continue

        categories = list(products.keys())
        selected_category = categories[category_index]

        current_products = products[selected_category]
        while True:
            print(f"\nProducts in {selected_category}:")
            display_products(current_products)

            # 展示选项
            print("\nOptions:")
            print("1. Select a product to buy")
            print("2. Sort the products according to the price")
            print("3. Go back to the category selection")
            print("4. Finish shopping")

            try:
                option = int(input("Please select an option: "))
                if option == 1:
                    # 选择购买的产品
                    while True:
                        try:
                            product_choice = int(input("Enter the product number you want to buy: "))
                            if 1 <= product_choice <= len(current_products):
                                selected_product = current_products[product_choice - 1]
                                break
                            else:
                                print(f"Invalid choice. Please enter a number between 1 and {len(current_products)}.")
                        except ValueError:
                            print("Invalid input. Please enter a number.")
                    while True:
                        try:
                            quantity = int(input("Enter the quantity you want to buy: "))
                            if quantity > 0:
                                break
                            else:
                                print("Quantity must be greater than 0.")
                        except ValueError:
                            print("Invalid input. Please enter a number.")
                    add_to_cart(cart, selected_product, quantity)
                    total_cost += selected_product[1] * quantity
                    print(f"{quantity} x {selected_product[0]} added to cart.")
                elif option == 2:
                    # 根据产品价格排序
                    while True:
                        try:
                            sort_choice = input("Sort by price: 'asc' for ascending, 'desc' for descending: ")
                            if sort_choice in ['asc', 'desc']:
                                current_products = display_sorted_products(current_products, sort_choice)
                                print("\nSorted Products:")
                                display_products(current_products)
                                break
                            else:
                                print("Invalid choice. Please enter 'asc' or 'desc'.")
                        except ValueError:
                            print("Invalid input. Please enter 'asc' or 'desc'.")
                elif option == 3:
                    # 回到类别选择
                    break
                elif option == 4:
                    # 完成购物
                    if cart:
                        print("\nYour Shopping Cart:")
                        display_cart(cart)
                        print(f"\nTotal Cost: ${total_cost}")
                        address = input("Please enter your delivery address: ")
                        generate_receipt(name, email, cart, total_cost, address)
                    else:
                        print("Thank you for using our portal. Hope you buy something from us next time. Have a nice day.")
                    return
                else:
                    print("Invalid option. Please select 1, 2, 3, or 4.")
            except ValueError:
                print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    main()