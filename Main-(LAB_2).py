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


cafe = Cafe("Elite Cafe")
cafe.load_data()

print(cafe.menu)
print(cafe.coupons)
print(cafe.users)
print(cafe.users[0].id)
print(cafe.users[0].orders)
