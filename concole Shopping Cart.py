menu = {"apple": 2.99,
        "orange": 1.50,
        "pineapple": 1.99,
        "banana": 1.00,
        "watermelon": 1.25,
        "corn": 2.50,
        "dragon fruit": 3.00,
        "grapes": 2.25
}  # Dictionary storing all items and their prices

cart = {}  # Dictionary to store items that the user selects
quantity = {}  # Dictionary to store quantity of each item selected by the user

def show_menu():
    for key, value in menu.items():  # Loop through each item in the menu
        print(f"{key} - ${value:.2f}")  # Print item name and price formatted to 2 decimal places

def show_cart():
        for key, value in cart.items():  # Loop through items in the cart
            print(f"{key} - ${value} - {quantity[key]}")  # Print item, price, and quantity

while True:  # Infinite loop to keep the program running until user exits
    user_input = input("Buy items/show my cart/remove item from my cart/print bill: ").lower().strip()
    # Ask user what they want to do, convert input to lowercase and remove spaces

    if user_input == "buy items":  # If user wants to buy items
        show_menu()  # Show the available items and prices

        while True:  # Loop to allow the user to add multiple items
            add_cart = input("What would you like to buy(q to quit): ")  # Ask which item to buy

            if add_cart == "q":  # If user types 'q', break out of buying loop
                break

            elif add_cart in menu:  # If the item exists in the menu
                cart[add_cart] = menu[add_cart]  # Add item and its price to the cart
            quantities = int(input(f"How many {add_cart}: "))  # Ask how many of this item the user wants
            quantity[add_cart] = quantities  # Store the quantity in the quantity dictionary

    elif user_input == "show my cart":  # If user wants to view cart
         show_cart()  # Call function to display cart contents

    elif user_input == "remove item from my cart":  # If user wants to remove an item
        show_cart()  # Show current cart
        remove_item = input("Which item would you like to remove: ")  # Ask which item to remove

        if remove_item in cart:  # If the item exists in the cart
            cart.pop(remove_item, None)  # Remove it from cart
            quantity.pop(remove_item, None)  # Remove its quantity as well
            show_cart()  # Show updated cart

    elif user_input == "print bill":  # If user wants to finalize and see the bill
        total = 0  # Initialize total to 0
        for items in cart:  # Loop through each item in the cart
            total += cart[items] * quantity[items]  # Multiply price by quantity and add to total

        print("---------Your-Bill---------------")
        print()
        show_cart()  # Show cart items with their quantities
        print("_____________________________")
        print()
        print(f"Your total is ${total:.2f}")  # Print total amount formatted to 2 decimal places
        print()
        print("---------Thank-You---------------") 
        break  # Exit the program after printing the bill
