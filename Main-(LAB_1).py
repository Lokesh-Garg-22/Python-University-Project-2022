Items = [["Item-1",10],["Item-2",10],["Item-3",10],["Item-4",10],["Item-5",10]] #[item_name,price]
Users = [["admin","admin",True],["user-1","pass",False],["user-2","pass",False]] #[user_name,user_password,is_admin]
Orders = [[1, 0, 5], [1, 2, 1]] #[user_id,item_id,quantity]
Coupons = [["Coupon-1","IFJT928R",5]] #[Coupon Name,Coupon ID,Times it can be used]
Locations = ["Chandigarh","New Delhi","Mumbai","Jaipur"]
welcome_text_1 = '''Welcome to the Elite Cafe'''
welcome_text_2 = '''Type "Menu" OR "Help" to Start'''
help_text = '''
Exit / Quit -> To exit the Program.
Menu -> Prints the Menu.
Location -> Prints all the Locations our Cafe is Located.
Order item_id user_id quantity(default=1) -> Place an Order by User.
Get Orders user_id -> Get all The Orders Placed by The User.
Cancel Order user_id order_id -> Cancel a Particular Order Placed by The User.
Checkout user_id -> Get the total price to be Paid.
Add Item user_id -> Add a New Item in the Menu. CAN ONLY BE DONE BY THE ADMIN.
Add User user_id -> Add a New User in the Database. CAN ONLY BE DONE BY THE ADMIN.
Get Users user_id -> Print All the Users in the Database. CAN ONLY BE DONE BY THE ADMIN.'''


def print_menu():
    for i in range(len(Items)):
        print("{}: {}".format(i+1, Items[i][0]).rjust(1).ljust(20),"\t",Items[i][1])

def print_locations():
    for i in range(len(Locations)):
        print("{}: {}".format(i+1, Locations[i]).ljust(20))

def check_password(user_id):
    password = input("Password: ").strip()
    if Users[user_id][1] == password:
        return True
    else:
        print("Incorrect Password".upper())
        return False

def check_admin(user_id):
    if Users[user_id][2]:
        return True
    else:
        print("You are not an Admin".upper())
        return False

def order_item(item_id,user_id,quantity=1):
    if item_id >= len(Items):
        print("An Item of ID {} does not exists.".format(item_id))
        return
    if user_id >= len(Users):
        print("A User of ID {} does not exists.".format(user_id))
        return
    if not check_password(user_id):
        return
    Orders.append([user_id,item_id,quantity])
    print("Your Order of {}*{} has been Submitted".format(Items[item_id][0],quantity))

def checkout(user_id):
    if user_id >= len(Users):
        print("A User of ID {} does not exists.".format(user_id))
        return
    if not check_password(user_id):
        return
    user_orders = []
    for i in Orders:
        if i[0] == user_id:
            user_orders.append(i)
    print("Your Orders are:")
    print("   Items ".ljust(20),"Price")
    total = 0
    for i in range(len(user_orders)):
        times = user_orders[i][2]
        if times > 1:
            times_text = "* {}".format(user_orders[i][2])
        else:
            times_text = ""
        price = Items[user_orders[i][1]][1] * user_orders[i][2]
        total += price
        print("{}. {} {}".format(i+1,Items[user_orders[i][1]][0],times_text).ljust(20),"\t ${}".format(price))
    print("Total Price".ljust(20),"\t ${}".format(total))
    answer = input("Whould You like to Checkout? ").lower().strip()
    answer = answer == "y" or answer == "yes"
    if answer:
        t = []
        for i in range(len(Orders)):
            if Orders[i][0] == user_id:
                t.append(i)
        for i in t[::-1]:
            del Orders[i]
        print("Your Orders have been Paid.")
    else:
        print("Checkout has been canceled.")

def add_user(user_id):
    if not check_admin(user_id):
        return
    if not check_password(user_id):
        return
    username=input("Please enter the Name of the User >").lower().strip()
    password=input("Please enter the Password of the User >").strip()
    is_admin=input("Is the new User an Admin? >").lower().strip()
    is_admin= is_admin == "y" or is_admin == "yes"
    Users.append([username,password,is_admin])
    print("User {} has been added.".format(username))

def print_user(user_id):
    if not check_admin(user_id):
        return
    if not check_password(user_id):
        return
    print("The Users are:")
    n = 0
    for i in Users:
        n += 1
        if i[2]:
            t = "Admin"
        else:
            t = "Not Admin"
        print("{}. {} ".format(n,i[0]).ljust(20),"{}".format(t))

def add_item(user_id):
    if not check_admin(user_id):
        return
    if not check_password(user_id):
        return
    item_name=input("Please enter the Name of the Item >").lower().strip()
    item_price=int(input("Please enter the Price of the Item >").strip())
    Items.append([item_name,item_price])
    print("Item {} has been added.".format(item_name))

def print_order(user_id):
    if not check_password(user_id):
        return
    print("Your Orders are:")
    print("   Items ".ljust(20),"Price")
    t = True
    n = 0
    for i in Orders:
        if i[0] == user_id:
            t = False
            n += 1
            print("{}. {}*{} ".format(n,Items[i[1]][0],i[2]).ljust(20),"{}".format(i[2]*Items[i[1]][1]))
    if t:
        print("None")

def cancel_order(user_id, order_id):
    if not check_password(user_id):
        return
    user_order = [i for i in Orders if i[0] == user_id]
    print("Your Order is {}*{}".format(Items[user_order[order_id][1]][0],user_order[order_id][2]))
    c = input("Do you want to Cancel This Order? >").lower().strip()
    c = c == "y" or c == "yes"
    if c:
        Orders.remove(user_order[order_id])
        print("Your order has been cancelled")
    else:
        print("Your Order Cancelation Command has been Revoked")

print()
print(welcome_text_1)
print(welcome_text_2)
while True:
    user_input = input(">").lower().split()
    if user_input[0] == "exit" or user_input[0] == "quit" : # Exit the Program
        break
    elif user_input[0] == "menu": # Menu
        print_menu()
    elif user_input[0] == "help": # Help
        print(help_text)
    elif user_input[0] == "location": # Locations
        print_locations()
    elif user_input[0] == "order": # Order an Item
        if len(user_input) >= 4:
            order_item(int(user_input[1])-1, int(user_input[2]), int(user_input[3]))
        elif len(user_input) >= 3:
            order_item(int(user_input[1])-1, int(user_input[2]))
        elif len(user_input) >= 2:
            print("Invalid Command: Please input Your User ID.")
        else:
            print("Invalid Command: Please input The Item ID and Your User ID.")
    elif len(user_input) >= 2 and user_input[0] == "get" and user_input[1] == "orders": # Print Orders
        if len(user_input) >= 3:
            print_order(int(user_input[2]))
        else:
            print("Invalid Command: Please input Your User ID.")
    elif len(user_input) >= 2 and user_input[0] == "cancel" and user_input[1] == "order": # Cancel Order
        if len(user_input) >= 4:
            cancel_order(int(user_input[2]),int(user_input[3])-1)
        elif len(user_input) >= 3:
            print("Invalid Command: Please input Your Order ID.")
        else:
            print("Invalid Command: Please input Your User ID and Your Order ID.")
    elif user_input[0] == "checkout": # Checkout
        if len(user_input) >= 2:
            checkout(int(user_input[1]))
        else:
            print("Invalid Command: Please input Your User ID.")
    elif len(user_input) >= 2 and user_input[0] == "add" and user_input[1] == "item": #Add New Item
        if len(user_input) >= 3:
            add_item(int(user_input[2]))
        else:
            print("Invalid Command: Please input Your User ID.")
    elif len(user_input) >= 2 and user_input[0] == "add" and user_input[1] == "user": #Add New User
        if len(user_input) >= 3:
            add_user(int(user_input[2]))
        else:
            print("Invalid Command: Please input Your User ID.")
    elif len(user_input) >= 2 and user_input[0] == "get" and user_input[1] == "users": # Print Users
        if len(user_input) >= 3:
            print_user(int(user_input[2]))
        else:
            print("Invalid Command: Please input Your User ID.")
    else:
        print("Invalid Command".upper())
