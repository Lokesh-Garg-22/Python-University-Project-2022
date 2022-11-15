Items = [["Item-1",10],["Item-2",10],["Item-3",10],["Item-4",10],["Item-5",10]]
Users = [["admin","admin",True],["user-1","pass"],["user-2","pass"]]
Orders = [[1, 0, 5], [1, 2, 1]] #[user_id,item_id,quantity]
welcome_text_1 = '''Welcome to the Elite Cafe.'''
welcome_text_2 = '''What whould you like to order?'''
help_text = '''
exit / quit -> To exit the Program.
menu -> Prints the Menu.
order item_id user_id quantity(default=1) -> Place an Order by User.
checkout -> Get the total price to be Paid.'''

def print_menu():
    for i in range(len(Items)):
        print("{}: {}".format(i+1, Items[i][0]).rjust(1).ljust(20),"\t",Items[i][1])
def check_password(user_id):
    password = input("Password: ").strip()
    if Users[user_id][1] == password:
        return True
    else:
        print("Incorrect Password".upper())
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
    print(Orders)
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
    answer = input("Whould You like to Checkout? ").lower().strip() == "y"
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

print()
print(welcome_text_1)
while True:
    print(welcome_text_2)
    user_input = input(">").lower().split()
    if user_input[0] == "exit" or user_input[0] == "quit" :
        break
    elif user_input[0] == "menu":
        print_menu()
    elif user_input[0] == "help":
        print(help_text)
    elif user_input[0] == "order":
        if len(user_input) >= 4:
            order_item(int(user_input[1])-1, int(user_input[2]), int(user_input[3]))
        elif len(user_input) >= 3:
            order_item(int(user_input[1])-1, int(user_input[2]))
        elif len(user_input) >= 2:
            print("Invalid Command: Please input Your User ID.")
        else:
            print("Invalid Command: Please input The Item ID and Your User ID.")
    elif user_input[0] == "checkout":
        if len(user_input) >= 2:
            checkout(int(user_input[1]))
        else:
            print("Invalid Command: Please input Your User ID.")
    else:
        print("Invalid Command".upper())
