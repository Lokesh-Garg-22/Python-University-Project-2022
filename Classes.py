class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return self.name


class Menu:
    groups = {}

    def __init__(self):
        pass

    def __repr__(self):
        pass

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

class Cafe:
    def __init__(self, name, menu = None):
        self.name = name
        self.menu = menu

    def set_menu(self, menu):
        if type(menu) != Menu:
            raise Exception(menu, "is not an Menu.")
            return
        self.menu = menu

    def print_menu(self):
        return self.menu
