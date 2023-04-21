def restaurant_menu():
    print("*****************************************")
    print("**     Welcome to the Snakes Cafe! **")
    print("**     Please see our menu below.  **")
    print("**")
    print('** To quit at any time, type "quit" **')
    print("*******************************************")

    menu = {
        "Appetizers": ["Wings", "Cookies", "Spring Rolls"],
        "Entrees": ["Salmon", "Steak", "Meat Tornado", "A Literal Garden"],
        "Desserts": ["Ice Cream", "Cake", "Pie"],
        "Drinks": ["Coffee", "Tea", "Unicorn Tears"]
    }

    for category, items in menu.items():
        print(f"\n{category.capitalize()}:")
        for item in items:
            print(f"- {item}")

    print("\nWhat would you like to order?")
    order = input("> ")
    order_counts = {}
    while order.lower() != "quit":

        found_item = False
        for sublist in menu.values():
            for item in sublist:
                if order.lower() == item.lower():
                    found_item = True
                    if item.lower() in order_counts:
                        order_counts[item.lower()] += 1
                    else:
                        order_counts[item.lower()] = 1
                    print(f"{order_counts[item.lower()]} order of {item} has been added to your meal")
                    break

            if found_item:
                break

        if not found_item:
            print(f"\nPlease choose from the menu")
        print("\nWhat would you like to order?")
        order = input("> ")

restaurant_menu()

