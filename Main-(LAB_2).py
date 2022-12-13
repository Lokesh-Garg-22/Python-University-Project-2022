from Classes import *

cafe = Cafe("Elite Cafe")
menu = Menu()
menu.add_item(Item("Item-1",20),"Group-1")
menu.add_item(Item("Item-2",20),"Group-1")
menu.add_item(Item("Item-3",20,10),"Group-1")
menu.add_item(Item("Item-4",20),"Group-2")
menu.add_item(Item("Item-5",20),"Group-2")
cafe.set_menu(menu)

print(cafe.print_menu())
print(cafe.print_menu("Group-1"))
cafe.generate_coupon(10)
print(cafe.coupons)
