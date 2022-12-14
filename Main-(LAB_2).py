from Classes import *

def reset_cafe(cafe = Cafe("")):
    if type(cafe) != Cafe:
        raise Exception(cafe, "is not a Cafe")
        return
    cafe.set_menu(Menu())
    cafe.menu.add_item(Item("Item-1",20),"Group-1")
    cafe.menu.add_item(Item("Item-2",20),"Group-1")
    cafe.menu.add_item(Item("Item-3",20,10),"Group-1")
    cafe.menu.add_item(Item("Item-4",20),"Group-2")
    cafe.menu.add_item(Item("Item-5",20),"Group-2")
    cafe.generate_coupon(10)
    cafe.add_user(User("Admin", "admin", True))
    cafe.save_data()

def order_sequence():
    print(cafe.menu)
    print("What would you like to order?")
    item_name = input("->")
    #### Check if the item is in the list
    print("How much Quantity do you Require?")
    while True:
        quantity = input("->")
        try:
            quantity = int(quantity)
        except:
            print("Please Type a Number")
            continue
        break
    #### Order Item for the user.
    print("{} items of {} has been ordered.".format(quantity,item_name))

def cancel_order_sequence():
    pass

def add_user_sequence():
    if not logged_in_user.admin:
        print("You are not an Admin.")
        return
    user_name = input("Username->")
    user_password = input("Password->")
    #### Add New User.
    print("New User {} has been made.".format(user_name))

def remove_user_sequence():
    pass

def add_item_sequence():
    if not logged_in_user.admin:
        print("You are not an Admin.")
        return
    print(cafe.menu.print_groups())
    item_group = input("Item Group->")
    item_name = input("Item Name->")
    item_price = input("Item Price->")
    #### Add New Item to Menu.
    print("New Item {} has been Added.".format(item_name))

def remove_item_sequence():
    pass

def chechout_sequence():
    pass

logged_in = False
logged_in_user = User("","")

cafe = Cafe("Elite Cafe")
cafe.load_data()

print("Welcome to the", cafe.name)
while True:
    user_input = input("->").lower()
    if user_input == "login":
        pass
    elif user_input == "exit":
        print("System Shuting Down".upper())
        break
    else:
        print("Please Login to continue.")
        continue
    while not logged_in:
        username = input("Username -> ")
        for i in cafe.users:
            if i.name == username:
                user = i
                break
        else:
            print(username, "does not exist.")
            continue
        password = input("Password -> ")
        if user.check_password(password):
            logged_in = True
            logged_in_user = user
        else:
            print("Wrong Password".upper())
            break
    if not logged_in:
        continue
    print("Wellcome", logged_in_user)
    print("What would you like to do.")
    while logged_in_user:
        user_input = input("->").lower().split()
        if user_input[0] == "exit":
            print("Logout first to exit.")
        elif user_input[0] == "logout":
            logged_in = False
            logged_in_user = User("","")
            print("User Logged Out")
            break
        elif user_input[0] == "menu":
            print(cafe.menu)
        elif user_input[0] == "locations":
            print(cafe.print_locations())
        elif user_input[0] == "order":
            order_sequence()
        elif user_input[0] == "cancel":
            if user_input[1] == "order":
                cancel_order_sequence()
        elif user_input[0] == "add":
            if user_input[1] == "user":
                add_user_sequence()
            elif user_input[1] == "item":
                add_item_sequence()
        else:
            print("Invalid Command".upper())