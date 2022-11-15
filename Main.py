Items = [["Item-1",10],["Item-2",10],["Item-3",10],["Item-4",10],["Item-5",10]]
Users = [["admin","admin",True],["user-1","pass"],["user-2","pass"]]
Orders = [[1, 0, 5], [1, 2, 1]] #[user_id,item_id,quantity]
welcome_text = '''
Welcome to the Elite Cafe.
What whould you like to order?'''
help_text = '''
exit / quit -> To exit the Program.
menu -> Prints the Menu.'''

def print_menu():
    for i in range(len(Items)):
        print("{}: {}".format(i+1, Items[i][0]).rjust(1).ljust(20),"\t",Items[i][1])
def order_item(item_id,user_id,quantity=1):
    password = input("Password: ").strip()
    if Users[user_id][1] == password:
        Orders.append([user_id,item_id,quantity])
    print(Orders)
def checkout(user_id):
    password = input("Password: ").strip()
    if Users[user_id][1] == password:
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
        answer = input("Whould You like to Checkout? ").lower().strip()
        print("Answer: ",answer)

print(welcome_text)
while True:
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
        else:
            order_item(int(user_input[1])-1, int(user_input[2]))
    elif user_input[0] == "checkout":
        checkout(int(user_input[1]))
    else:
        print("Invalid Command".upper())