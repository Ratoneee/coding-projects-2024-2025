# I added so when the user wants to see the items in the cart it will also display the total price of all items instead of having to go to another menu to see the total price and I also added Item Quantities so the user can add more then one of the same item and I added in the cart it formats the cart by "ITEMS", "QUANTITY", and "PRICE".
shopping_cart = []
item_price = []
item_quantity = []

def main_menu():
    print("\nPlease choose a menu option")
    print("1. Add new item to cart")
    print("2. Show current items in cart")
    print("3. Remove an item from cart")
    print("4. Calculate total amount in cart")
    print("5. Quit")
    print("-----------------------------------")

def adding_cart():
    item = input("What item would you like to add to your cart? ")
    print("-----------------------------------")
    try:
        quantity = int(input(f"How many of '{item}' would you like to add? "))
        print("-----------------------------------")
        price_of_item = float(input(f'What is the price of "{item}"? '))
        print("-----------------------------------")
        shopping_cart.append(item)
        item_price.append(price_of_item * quantity)
        item_quantity.append(quantity)
        print("-----------------------------------")
        print(f'"{item}" has been added to your cart.')
        print(f"Quantity: {quantity}")
        print("-----------------------------------")
    except ValueError:
        print("Invalid input. Please enter a valid number for price and quantity.")
        print("-----------------------------------")

def show_cart():
    if shopping_cart:
        print("You currently have these items in your shopping cart:")
        total = 0
        for idx, item in enumerate(shopping_cart, 1):
            print("-----------------------------------")
            print(f"{idx}. ITEM {item}   QUANTITY {item_quantity[idx-1]}   PRICE ${item_price[idx-1] / item_quantity[idx-1]:.2f}")
            total += item_price[idx-1]
        print("-----------------------------------")
        print(f"Total price: ${total:.2f}")
        print("-----------------------------------")
    else:
        print("Your shopping cart is empty.")
        print("-----------------------------------")

def remove_item():
    if not shopping_cart:
        print("Your shopping cart is empty. Nothing to remove.")
        print("-----------------------------------")
        return
    
    show_cart()
    try:
        choice = int(input("Which item would you like to remove? Enter the number: "))
        print("-----------------------------------")
        if 1 <= choice <= len(shopping_cart):
            removed_item = shopping_cart.pop(choice - 1)
            removed_price = item_price.pop(choice - 1)
            removed_quantity = item_quantity.pop(choice - 1)
            
            print(f'"{removed_item}" has been removed from your cart.')
            print("-----------------------------------")
        else:
            print("Invalid choice. Please enter a number from the list.")
            print("-----------------------------------")
    
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        print("-----------------------------------")

def compute_total():
    if not item_price:
        print("Your shopping cart is empty. Total is $0.00")
    else:
        total = sum(item_price)
        print(f"Your total price is: ${total:.2f}")
    print("-----------------------------------")

while True:
    main_menu()
    choice = input("Enter your choice (1, 2, 3, 4, or 5): ")
    print("-----------------------------------")
    if choice == "1":
        adding_cart()
    elif choice == "2":
        show_cart()
    elif choice == "3":
        remove_item()
    elif choice == "4":
        compute_total()
    elif choice == "5":
        print("-----------------------------------")
        print("Thank you for shopping with us!")
        print("-----------------------------------")
        break
    else:
        print("Invalid choice. Please enter a valid option (1, 2, 3, 4, or 5).")
        print("-----------------------------------")
