from Classes import *

def reset_cafe(cafe = Cafe("")):
    if type(cafe) != Cafe:
        raise Exception(cafe, "is not a Cafe")
        return
    cafe.locations = ["Chandigarh","New Delhi","Mumbai","Jaipur"]
    cafe.set_menu(Menu())
    cafe.menu.add_item(Item("Apni Chai",15),"Tea")
    cafe.menu.add_item(Item("Masale Wali",20),"Tea")
    cafe.menu.add_item(Item("Elaichi Wali",25),"Tea")
    cafe.menu.add_item(Item("Black Tea",15),"Tea")
    cafe.menu.add_item(Item("Lemon Tea",20),"Tea")
    cafe.menu.add_item(Item("Strawberry Tea",30),"Tea")
    cafe.menu.add_item(Item("Peach Tea",20),"Tea")
    cafe.menu.add_item(Item("Hot Coffee",30),"Coffee")
    cafe.menu.add_item(Item("Cold Coffee",80),"Coffee")
    cafe.menu.add_item(Item("Espresso",50),"Coffee")
    cafe.menu.add_item(Item("Americano",60),"Coffee")
    cafe.menu.add_item(Item("Cappuccino",80),"Coffee")
    cafe.menu.add_item(Item("Cafe Latte",30),"Coffee")
    cafe.menu.add_item(Item("Caramel Macchiato",40),"Coffee")
    cafe.menu.add_item(Item("Piccolo",40),"Coffee")
    cafe.menu.add_item(Item("Affogato",40),"Coffee")
    cafe.menu.add_item(Item("Poha",30),"Snacks")
    cafe.menu.add_item(Item("Samosa",15),"Snacks")
    cafe.menu.add_item(Item("Vada Pav",15),"Snacks")
    cafe.menu.add_item(Item("Veg Sandwich",30),"Snacks")
    cafe.menu.add_item(Item("Cheese Sandwich",35),"Snacks")
    cafe.menu.add_item(Item("Mix Pakoda",30),"Snacks")
    cafe.menu.add_item(Item("Bread Butter",15),"Snacks")
    cafe.menu.add_item(Item("Pasta",40),"Snacks")
    cafe.menu.add_item(Item("Green Salad",30),"Snacks")
    cafe.add_user(User("Admin", "admin", True))
    cafe.add_user(User("Lokesh", "pass"))
    cafe.add_user(User("Mehak", "pass"))
    cafe.add_user(User("Manya", "pass"))
    cafe.save_data()

def order_sequence():
    print(cafe.menu)
    print("What would you like to order?")
    item_name = input("->").strip()
    item = cafe.menu.get_item(item_name)
    if item == False:
        print(item_name, "Does not exist")
        return
    print("How much Quantity do you Require?")
    while True:
        quantity = input("->").strip()
        try:
            quantity = int(quantity)
        except:
            print("Please Type a Number")
            continue
        break
    cafe.add_user_order(logged_in_user, item, quantity)
    print("{} items of {} has been ordered".format(quantity,item_name))
    cafe.save_data()

def cancel_order_sequence():
    cafe.print_user_orders(logged_in_user)
    item_name = input("Item Name->").strip()
    item = cafe.menu.get_item(item_name)
    if item == False:
        print("Item {} does not exist".format(item_name))
        return
    confirmation = input("Do you want to Cancel Order of Item {} ->".format(item)).lower().strip()
    confirmation = (confirmation == "y") or (confirmation == "yes")
    if confirmation:
        cafe.cancel_user_order(logged_in_user, item)
        print("Order of Item {} has been Canceled".format(item))
        cafe.save_data()
    else:
        print("Order of Item {} has Not been Canceled")

def add_user_sequence():
    if not logged_in_user.admin:
        print("You are not an Admin")
        return
    user_name = input("Username->").strip()
    user_password = input("Password->").strip()
    user_admin = input("Is the New User an Admin ->").lower().strip()
    user_admin = (user_admin == "y") or (user_admin == "yes")
    user = User(user_name, user_password, admin=user_admin)
    if user_admin:
        confirmation = input("Do you want to Add a New User {} as Admin ->".format(user_name)).lower().strip()
    else:
        confirmation = input("Do you want to Add a New User {} ->".format(user_name)).lower().strip()
    confirmation = (confirmation == "y") or (confirmation == "yes")
    if confirmation:
        cafe.add_user(user)
        print("New User {} has been made".format(user))
        cafe.save_data()
    else:
        print("New User has been Canceled")

def remove_user_sequence():
    if not logged_in_user.admin:
        print("You are not an Admin")
        return
    print(cafe.print_users())
    user_name = input("User Name ->").strip()
    user = cafe.get_user(user_name)
    if user == False:
        print("User {} does not exist".format(user_name))
        return
    confirmation = input("Do you want to remove {} ->".format(user)).lower().strip()
    confirmation = (confirmation == "y") or (confirmation == "yes")
    if confirmation:
        cafe.remove_user(user)
        print("User {} has been Removed".format(user))
        cafe.save_data()
    else:
        print("User Removal has been Canceled")

def add_item_sequence():
    if not logged_in_user.admin:
        print("You are not an Admin")
        return
    print(cafe.menu.print_groups())
    item_group = input("Item Group->").strip()
    item_name = input("Item Name->").strip()
    item_price = input("Item Price->").strip()
    item = Item(item_name, item_price)
    confirmation = input("Do you want to Add The Item {} of Group {} ->".format(item, item_group)).lower().strip()
    confirmation = (confirmation == "y") or (confirmation == "yes")
    if confirmation:
        cafe.menu.add_item(item, item_group)
        print("New Item {} has been Added".format(item))
        cafe.save_data()
    else:
        print("New Item has been Canceled")

def remove_item_sequence():
    if not logged_in_user.admin:
        print("You are not an Admin")
        return
    print(cafe.menu)
    item_name = input("Item Name ->").strip()
    item = cafe.menu.get_item(item_name)
    if item == False:
        print("Item {} does not exist".format(item_name))
        return
    item_group = cafe.menu.get_item_group(item_name)
    confirmation = input("Do you want to remove {} from {}'s Group ->".format(item,item_group)).lower().strip()
    confirmation = (confirmation == "y") or (confirmation == "yes")
    if confirmation:
        cafe.menu().remove_item(item, item_group)
        print("{} Item from {} Group has been Removed".format(item,item_group))
        cafe.save_data()
    else:
        print("Item Removal has been Canceled")

def set_item_discription_sequence():
    if not logged_in_user.admin:
        print("You are not an Admin")
        return
    print(cafe.menu)
    item_name = input("Item Name ->").strip()
    item = cafe.menu.get_item(item_name)
    if item == False:
        print("Item {} does not exist".format(item_name))
        return
    item_discription = input("New Item Discription ->")
    cafe.menu().change_item_discription(item, item_discription)
    print("Item Discription has Been Changed")
    cafe.save_data()

def set_item_discount_sequence():
    if not logged_in_user.admin:
        print("You are not an Admin")
        return
    print(cafe.menu)
    item_name = input("Item Name ->").strip()
    item = cafe.menu.get_item(item_name)
    if item == False:
        print("Item {} does not exist".format(item_name))
        return
    while True:
        item_discount = input("New Item Discount ->").strip()
        try:
            item_discount = int(item_discount)
        except:
            print("Please Type a Number out of 100")
            continue
        break
    cafe.menu().change_item_discount(item, item_discount)
    print("Item Discount has Been Changed")
    cafe.save_data()

def add_coupon_sequence():
    if not logged_in_user.admin:
        print("You are not an Admin")
        return
    while True:
        coupon_discount = input("Coupon Discount->").strip()
        try:
            coupon_discount = int(coupon_discount)
        except:
            print("Please Type a Number out of 100")
            continue
        break
    while True:
        coupon_times_used = input("Coupon Times Used->").strip()
        try:
            coupon_times_used = int(coupon_times_used)
        except:
            print("Please Type a Number")
            continue
        break
    confirmation = input("Do you want to Add a Coupon of Discount {} which can be used {} times ->".format(coupon_discount, coupon_times_used)).lower().strip()
    confirmation = (confirmation == "y") or (confirmation == "yes")
    if confirmation:
        coupon_id = cafe.generate_coupon(coupon_discount, coupon_times_used)
        print("New Coupon of ID {} has been Generated".format(coupon_id))
        cafe.save_data()
    else:
        print("New Coupon has been Canceled")

def checkout_sequence():
    use_coupon = input("Do you want to use a Coupon? ->").lower().strip()
    use_coupon = (use_coupon == "y") or (use_coupon == "yes")
    while use_coupon:
        found = False
        coupon_id = input("Coupon ID ->").strip()
        for i in cafe.coupons:
            if i == coupon_id:
                coupon = cafe.coupons[i]
                found = True
        if found:
            print("Coupon ID {} found".format(coupon_id))
            break
        else:
            print("Coupon ID {} not found".format(coupon_id))
            use_coupon = False
    orders, total_amount = cafe.get_user_checkout_data(logged_in_user)
    print(orders,end="")
    if use_coupon:
        print("{}% Discount from The Coupon".format(coupon["discount"])) ###print coupon discount
        total_amount = (total_amount - (total_amount / 100 * coupon["discount"]))
    print("Total".ljust(30,"-") + "{}".format(total_amount))
    chechout = input("Do you want to Chechout? ->").lower().strip()
    chechout = (chechout == "y") or (chechout == "yes")
    if chechout:
        if use_coupon:
            cafe.user_checkout(logged_in_user)
            cafe.use_coupon(coupon_id)
            print("Chechout Complete")
            cafe.save_data()
        else:
            cafe.user_checkout(logged_in_user)
            print("Chechout Complete")
            cafe.save_data()
    else:
        print("Chechout has been Canceled")

logged_in = False
logged_in_user = User("","")

help_text = '''
Exit / Quit -> To exit the Program.
Login -> To Login of the System
Logout -> To Logout of the System
Menu -> Prints the Menu.
Locations -> Prints all the Locations our Cafe is Located.
Order -> Place an Order by User.
Print Orders -> Get all The Orders Placed by The User.
Cancel Order -> Cancel a Particular Order Placed by The User.
Checkout -> Get the total price to be Paid.
Add Item -> Add a New Item in the Menu. CAN ONLY BE DONE BY THE ADMIN.
Add User -> Add a New User in the Database. CAN ONLY BE DONE BY THE ADMIN.
Add Coupon -> Add a New Coupon in the Database. CAN ONLY BE DONE BY THE ADMIN.
Print Users -> Print All the Users in the Database. CAN ONLY BE DONE BY THE ADMIN.
Print Coupons -> Print All the Coupons in the Database. CAN ONLY BE DONE BY THE ADMIN.
Set Item Discription -> Set Discription of an Item. CAN ONLY BE DONE BY THE ADMIN.
Set Item Discount -> Set Discount for an Item. CAN ONLY BE DONE BY THE ADMIN.'''

cafe = Cafe("Elite Cafe")
cafe.load_data()
# reset_cafe(cafe)

print("Welcome to the", cafe.name)
while True:
    user_input = input("->").lower()
    if user_input == "login":
        pass
    elif user_input == "exit" or user_input == "quit":
        print("System Shuting Down".upper())
        break
    elif user_input == "help":
        print(help_text)
    else:
        print("Please Login to continue.")
        continue
    while not logged_in:
        username = input("Username -> ").strip()
        if username.lower() == "exit":
            break
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
        if user_input[0] == "exit" or user_input[0] == "quit":
            print("Logout first to exit.")
        elif user_input[0] == "logout":
            logged_in = False
            logged_in_user = User("","")
            print("User Logged Out")
            break
        elif user_input[0] == "help":
            print(help_text)
        elif user_input[0] == "menu":
            print(cafe.menu)
        elif user_input[0] == "locations":
            print(cafe.print_locations())
        elif user_input[0] == "order":
            order_sequence()
        elif user_input[0] == "checkout":
            checkout_sequence()
        elif user_input[0] == "cancel":
            if user_input[1] == "order":
                cancel_order_sequence()
        elif user_input[0] == "add":
            if user_input[1] == "user":
                add_user_sequence()
            elif user_input[1] == "item":
                add_item_sequence()
            elif user_input[1] == "coupon":
                add_coupon_sequence()
        elif user_input[0] == "set":
            if user_input[1] == "item":
                if user_input[2] == "discription":
                    set_item_discription_sequence()
                elif user_input[2] == "discount":
                    set_item_discount_sequence()
        elif user_input[0] == "print":
            if user_input[1] == "users":
                if not logged_in_user.admin:
                    print("You are not an Admin")
                    continue
                print(cafe.print_users())
            if user_input[1] == "coupons":
                if not logged_in_user.admin:
                    print("You are not an Admin")
                    continue
                print(cafe.print_coupons())
            elif user_input[1] == "orders":
                print(cafe.print_user_orders(logged_in_user))
        else:
            print("Invalid Command".upper())