from IPython.display import clear_output


def show_instructions():
    print("""
Type "ADD" to add item to your cart.
Type "DELETE" to remove item from your cart.
Type "SHOW" to see cart.
Type "QUIT" to finish shopping.""")
    print("=~"*25)


def shopping():
    input("Welcome to Jon's Market! Press any key to continue.")
    print("=~"*25)

    cart = []
    done = False

    while not done:
        clear_output()

        show_instructions()

        choice = input(
            "What is your choice? ADD | DELETE | SHOW | QUIT ").lower()
        if choice == 'add':
            item = input('Type in item. ').title()
            item_price = float(input('Type in item price. '))

            shopping_cart = {
                "item": item,
                "item_price": item_price,
            }

            cart.append(shopping_cart)

        elif choice == 'delete':
            item = input('Type item you wish to delete. ').title()
            cart.remove(shopping_cart)

        elif choice == "show":
            for item in cart:
                print(item)
            input("Press any key to continue. ")

        elif choice == "quit":
            confirm = input("Are you sure you want to quit? Y/N ").lower()
            if confirm == "y":
                print(
                    'Thank you for shopping, have a nice day! Please take your reciept.', shopping_cart)
                done = True
            elif confirm == "n":
                continue


shopping()
