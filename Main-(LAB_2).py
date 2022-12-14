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
    item_name = input("->").strip()
    #### Check if the item is in the list
    print("How much Quantity do you Require?")
    while True:
        quantity = input("->").strip()
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
    user_name = input("Username->").strip()
    user_password = input("Password->").strip()
    #### Add New User.
    print("New User {} has been made.".format(user_name))

def remove_user_sequence():
    if not logged_in_user.admin:
        print("You are not an Admin.")
        return
    print(cafe.print_users())
    user_name = input("User Name ->").strip()
    print("chech for user")
    confirmation = input("Do you want to remove {} ->".format(user_name)).lower().strip()
    confirmation = (confirmation == "y") or (confirmation == "yes")
    if confirmation:
        print("remove user")
        print("{} User has been Removed.".format(user_name))
    else:
        print("User Removal has been Canceled")

def add_item_sequence():
    if not logged_in_user.admin:
        print("You are not an Admin.")
        return
    print(cafe.menu.print_groups())
    item_group = input("Item Group->").strip()
    item_name = input("Item Name->").strip()
    item_price = input("Item Price->").strip()
    #### Add New Item to Menu.
    print("New Item {} has been Added.".format(item_name))

def remove_item_sequence():
    if not logged_in_user.admin:
        print("You are not an Admin.")
        return
    print(cafe.menu)
    item_name = input("Item Name ->").strip()
    print("check for item")
    item_group = ""
    confirmation = input("Do you want to remove {} from {}'s Group ->".format(item_name,item_group)).lower().strip()
    confirmation = (confirmation == "y") or (confirmation == "yes")
    if confirmation:
        print("remove item")
        print("{} Item from {} Group has been Removed.".format(item_name,item_group))
    else:
        print("Item Removal has been Canceled")

def set_item_discription_sequence():
    if not logged_in_user.admin:
        print("You are not an Admin.")
        return
    print(cafe.menu)
    item_name = input("Item Name ->").strip()
    print("check for item")
    item_discription = input("New Item Discription ->")
    print("change item discription")

def chechout_sequence():
    use_coupon = input("Do you want to use a Coupon? ->").lower().strip()
    use_coupon = (use_coupon == "y") or (use_coupon == "yes")
    while use_coupon:
        found = False
        coupon_id = input("Coupon ID ->").strip()
        for i in cafe.coupons:
            if i == coupon_id:
                found = True
        if found:
            print("Coupon ID {} found".format(coupon_id))
            break
        else:
            print("Coupon ID {} not found".format(coupon_id))
            use_coupon = False
    data = ["Text to print", "total_amount"] ### print Chechout
    if use_coupon:
        print() ###print coupon discount
    chechout = input("Do you want to Chechout? ->").lower().strip()
    chechout = (chechout == "y") or (chechout == "yes")
    if chechout:
        #### do chechout for the user
        print("Chechout Complete")
    else:
        print("Chechout has been Canceled")

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
        username = input("Username -> ").strip()
        for i in cafe.users:
            if i.name == username:
                user = i
                break
        else:
            print(username, "does not exist.")
            continue
        password = input("Password -> ").strip()
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
        elif user_input[0] == "set":
            if user_input[1] == "item":
                if user_input[2] == "discription":
                    set_item_discription_sequence()
        elif user_input[0] == "print":
            if user_input[1] == "users":
                if not logged_in_user.admin:
                    print("You are not an Admin.")
                    continue
                print(cafe.print_users())
            elif user_input[1] == "orders":
                print(cafe.print_user_orders(logged_in_user))
        else:
            print("Invalid Command".upper())