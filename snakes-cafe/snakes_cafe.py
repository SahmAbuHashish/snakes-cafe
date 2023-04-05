def restaurant_menu():
    print("*****************************************")
    print("**     Welcome to the Snakes Cafe! **")
    print("**     Please see our menu below.  **")
    print("**")
    print("** To quit at any time, type " + "quit **")
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
    count = 0
    while order.lower() != "quit":
        
        if order.lower() in [item.lower() for sublist in menu.values() for item in sublist]:
            count = count +1
            print(f"{count} order of {order} has been added to your meal")
        else:
            print(f"\nplease chaos from the menu")
            print(f"\nWhat would you like to order?")
        order = input("> ")
    

restaurant_menu()
