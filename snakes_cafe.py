def snakes_cafe():
    print("*****************************************")
    print("**     Welcome to the Snakes Cafe! **")
    print("**     Please see our menu below.  **")
    print("**")
    print("** To quit at any time, type " + "quit **")
    print("*******************************************")

    # menu = {
    #     "Appetizers": ["Wings", "Cookies", "Spring Rolls"],
    #     "Entrees": ["Salmon", "Steak", "Meat Tornado", "A Literal Garden"],
    #     "Desserts": ["Ice Cream", "Cake", "Pie"],
    #     "Drinks": ["Coffee", "Tea", "Unicorn Tears"]
    # }

    Appetizers= ["Wings", "Cookies", "Spring Rolls"]
    Entrees= ["Salmon", "Steak", "Meat Tornado", "A Literal Garden"]
    Desserts= ["Ice Cream", "Cake", "Pie"]
    Drinks= ["Coffee", "Tea", "Unicorn Tears"]

    print(" ")
    print("Appetizers")
    print("----------")
    for x in Appetizers:
        print(x)

    print(" ")
    print("Entrees")
    print("----------")
    for x in Entrees:
        print(x)

    print(" ")
    print("Desserts")
    print("----------")
    for x in Desserts:
        print(x)

    print(" ")
    print("Drinks")
    print("----------")
    for x in Drinks:
        print(x)

    All_menu = ["Wings", "Cookies", "Spring Rolls", "Salmon", "Steak", "Meat Tornado",
                "A Literal Garden", "Ice Cream", "Cake", "Pie", "Coffee", "Tea", "Unicorn Tears"]
    
    order = input("What would you like to order?")
    count = 0

    while order!= "quit":
    
      for i in range(len(All_menu)):
         if order == All_menu[i]:
            count = count + 1
            print("${count} order of ${order} has been added to your meal")
    else:
        order = input("What would you like to order?")

    


snakes_cafe()
