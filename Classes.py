import random

class Item:
    discription = ""

    def __init__(self, name, price, discount = 0):
        self.name = name
        self.price = price
        self.discount = discount

    def __repr__(self):
        return self.name

    def set_discount(self, discount):
        if type(discount) != float:
            raise Exception(discount, "is not a Float.")
            return
        self.discount = discount

    def get_cost(self, quantity = 1):
        if self.discount != 0:
            return (self.price - (self.price / 100 * self.discount)) * quantity
        else:
            return self.price * quantity

    def print_item_discription(self):
        return self.discription


class Menu:
    groups = {}

    def __init__(self):
        pass

    def __repr__(self):
        result = ""
        for i in self.groups:
            result += (" {} ".format(i).center(45,"-") + "\n")
            for j in self.groups[i]["items"]:
                result += ("{}".format(j).ljust(40) + "{}\n".format(j.get_cost()))
        return result

    def add_item(self, item, group):
        if type(item) != Item:
            raise Exception(item, "is not an Item.")
            return
        if group in self.groups:
            self.groups[group]["items"].append(item)
        else:
            self.create_group(group)
            self.groups[group]["items"].append(item)

    def create_group(self, name):
        self.groups[name] = {"items": []}

    def print_group(self, group):
        if group not in self.groups:
            raise Exception(group, "is not present in the List of Groups")
            return
        result = (" {} ".format(group).center(45,"-") + "\n")
        for j in self.groups[group]["items"]:
            result += ("{}".format(j).ljust(40) + "{}\n".format(j.get_cost()))
        return result


class Cafe:
    data_file = "data.json"
    menu = None
    users = []
    coupons = {}

    def __init__(self, name):
        self.name = name

    def set_menu(self, menu):
        if type(menu) != Menu:
            raise Exception(menu, "is not an Menu.")
            return
        self.menu = menu

    def print_menu(self, group = None):
        if group == None:
            return self.menu
        else:
            return self.menu.print_group(group)
    
    def add_user(self, user):
        if type(user) != User:
            raise Exception(user, "is not a User.")
            return
        self.users.append(user)

    def generate_coupon_id(self, length = 10):
        result = ""
        for i in range(length):
            t = random.randint(1,2)
            if t == 1:
                result += str(random.randint(1,9))
            else:
                result += chr(random.randint(65,90))
        return result

    def generate_coupon(self, discount, times_used = 1):
        t = 0
        while True:
            t += 1
            if t >= 100:
                raise Exception("Coupon Not Generated.")
                return
            id = self.generate_coupon_id()
            if id not in self.coupons:
                break
        self.coupons[id] = {"discount": discount, "times_used": times_used}

    def load_data(self):
        pass

    def save_data(self):
        pass


class User:
    orders = []

    def __init__(self, name, password, admin = False, location = "offline"):
        self.name = name
        self.password = password
        self.admin = admin
        self.location = location
    
    def __repr__(self):
        return self.name

    def check_password(self, password):
        if password == self.password:
            return True
        else:
            return False
