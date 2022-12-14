import random, json

class Item:
    def __init__(self, name, price, discount = 0, id=0, discription = ""):
        self.id = id
        self.name = name
        self.price = price
        self.discount = discount
        self.discription = discription

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

    def generate_item_id(self):
        max_id = 0
        for i in self.groups:
            for j in self.groups[i]["items"]:
                if j.id > max_id:
                    max_id = j.id
        id = max_id + 1
        return id

    def add_item(self, item, group):
        if type(item) != Item:
            raise Exception(item, "is not an Item.")
            return
        item.id = self.generate_item_id()
        if group in self.groups:
            self.groups[group]["items"].append(item)
        else:
            self.create_group(group)
            self.groups[group]["items"].append(item)

    def get_item(self, item_name):
        for i in self.groups:
            for j in self.groups[i]["items"]:
                if j.name == item_name:
                    return j
        else:
            return False

    def get_item_group(self, item_name):
        for i in self.groups:
            for j in self.groups[i]["items"]:
                if j.name == item_name:
                    return i
        else:
            return False

    def remove_item(self, item, item_group = False):
        if item_group == False:
            for i in self.groups:
                for j in self.groups[i]["items"]:
                    if j.id == item.id:
                        self.groups[i]["items"].remove(j)
        else:
            for j in self.groups[item_group]["items"]:
                if j.id == item.id:
                    self.groups[item_group]["items"].remove(j)

    def change_item_discription(self, item, discription):
        for i in self.groups:
            for j in self.groups[i]["items"]:
                if j.id == item.id:
                    j.discription = discription

    def change_item_discount(self, item, discount):
        for i in self.groups:
            for j in self.groups[i]["items"]:
                if j.id == item.id:
                    j.discount = discount

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

    def print_groups(self):
        result = ""
        for i in self.groups:
            result += "{}\n".format(i)
        return result



class Cafe:
    menu = None
    users = []
    coupons = {}
    locations = []

    def __init__(self, name):
        self.name = name
        self.data_file = "data" + "_" + self.name + "_" + ".json"
        self.data_back_up_file = "data_back_up" + "_" + self.name + "_" + ".json"

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

    def generate_user_id(self):
        max_id = 0
        for i in self.users:
            if i.id > max_id:
                max_id = i.id
        id = max_id + 1
        return id
    
    def add_user(self, user):
        if type(user) != User:
            raise Exception(user, "is not a User.")
            return
        user.id = self.generate_user_id()
        self.users.append(user)

    def get_user(self, user_name):
        for i in self.users:
            if i.name == user_name:
                return i
        else:
            return False

    def remove_user(self, user):
        if type(user) != User:
            raise Exception(user, "is not a User.")
            return
        for i in self.users:
            if i.id == user.id:
                self.users.remove(i)
                break

    def add_user_order(self, user, item, quantity):
        for i in self.users:
            if i.id == user.id:
                i.add_order(item, quantity)

    def get_user_checkout_data(self, user):
        for i in self.users:
            if i.id == user.id:
                data = i.get_checkout_data()
                return data

    def user_checkout(self, user):
        for i in self.users:
            if i.id == user.id:
                i.checkout()

    def print_users(self):
        result = ""
        result += ("ID".ljust(15) + "Name".ljust(15) + "Is Admin\n")
        for i in self.users:
            result += ("{}".format(i.id).ljust(15) + "{}".format(i.name).ljust(15) + "{}\n".format(i.admin))
        return result

    def print_user_orders(self, user):
        if type(user) != User:
            raise Exception(user, "is not a User.")
            return
        for i in self.users:
            if user.id == i.id:
                user = i
        return user.print_orders()

    def cancel_user_order(self, user, item):
        if type(user) != User:
            raise Exception(user, "is not a User.")
            return
        for i in self.users:
            if user.id == i.id:
                i.cancle_order(item)
                break

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

    def add_coupon(self, id, discount, times_used = 1):
        self.coupons[id] = {"discount": discount, "times_used": times_used}

    def use_coupon(self, coupon_id):
        for i in self.coupons:
            if i == coupon_id:
                t = self.coupons[i]["times_used"] - 1
                if t <= 0:
                    del self.coupons[i]
                else:
                    self.coupons[i]["times_used"] = t

    def add_locations(self, *location):
        for l in location:
            self.locations.append(l)

    def print_locations(self):
        result = ""
        for i in self.locations:
            result += "{}\n".format(i)
        return result

    def load_back_up_data(self):
        try:
            with open(self.data_back_up_file, 'r') as data_file:
                data = json.load(data_file)
            self.load_data(data)
        except:
            return "BackUp not Found"

    def load_data(self, data = None):
        if data == None:
            try:
                with open(self.data_file, 'r') as data_file:
                    data = json.load(data_file)
            except:
                data = {
                        "coupons": {},
                        "locations": [],
                        "users": [],
                        "menu": {}
                    }

        self.coupons = data.get("coupons", {})
        self.locations = data.get("locations", [])

        #Load Menu Data
        self.set_menu(Menu())
        for i in data.get("menu", {}):
            for j in data["menu"][i]["items"]:
                self.menu.add_item(Item(**j), i)
        
        #Load User Data
        self.users = []
        for i in data.get("users", []):
            o = []
            for j1 in i["orders"]:
                for j2 in self.menu.groups:
                    for j3 in self.menu.groups[j2]["items"]:
                        if j1["item"] == j3.id:
                            o.append({"item": j3, "quantity": j1["quantity"]})
            i["orders"] = o
            self.add_user(User(**i))

        return "Data Loaded Successfully"

    def save_back_up_data(self):
        data = self.save_data(return_data=True)
        with open(self.data_back_up_file, "w") as data_file:
            data_file.write(json.dumps(data, indent=4))
        return "BackUp Data Saved Successfully"

    def save_data(self, return_data = False):
        data = {
            "coupons": self.coupons,
            "locations": self.locations
        }

        #Save Menu Data
        t = {}
        for i in self.menu.groups:
            tt = {}
            tt["items"] = []
            for j in self.menu.groups[i]["items"]:
                ttt = {}
                ttt["id"] = j.id
                ttt["name"] = j.name
                ttt["price"] = j.price
                ttt["discount"] = j.discount
                ttt["discription"] = j.discription
                tt["items"].append(ttt)
            t[i] = (tt)
        data["menu"] = t

        #Save Users Data
        t = []
        for i in self.users:
            tt = {}
            tt["id"] = i.id
            tt["name"] = i.name
            tt["password"] = i.password
            tt["admin"] = i.admin
            tt["location"] = i.location
            tt["orders"] = [{"item": j["item"].id, "quantity": j["quantity"]} for j in i.orders]
            t.append(tt)
        data["users"] = t

        with open(self.data_file, "w") as data_file:
            data_file.write(json.dumps(data, indent=4))
        if return_data:
            return data
        else:
            return "Data Saved Successfully"


class User:
    def __init__(self, name, password, admin = False, location = "offline", id = 0, orders = []):
        self.id = id
        self.name = name
        self.password = password
        self.admin = admin
        self.location = location
        self.orders = orders
    
    def __repr__(self):
        return self.name

    def check_password(self, password):
        if password == self.password:
            return True
        else:
            return False

    def add_order(self, item, quantity = 1):
        if type(item) != Item:
            raise Exception(item, "is not an Item")
            return
        self.orders.append({"item": item, "quantity": quantity})

    def print_orders(self):
        result = ""
        result += ("Item".ljust(30,"-") + "Quantity\n")
        for i in self.orders:
            result += ("{}".format(i["item"]).ljust(30,"-") + "{}\n".format(i["quantity"]))
        return result

    def cancle_order(self, item):
        if type(item) != Item:
            raise Exception(item, "is not an Item")
            return
        for i in self.orders:
            if i["item"].id == item.id:
                self.orders.remove(i)
                break

    def get_checkout_data(self):
        print_text = ""
        total_amount = 0
        print_text += ("Item".ljust(30,"-") + "Price\n")
        for i in self.orders:
            print_text += ("{}".format(i["item"]).ljust(30,"-") + "{}\n".format(i["item"].price))
            total_amount += i["item"].price
        return (print_text, total_amount)

    def checkout(self):
        self.orders = []
