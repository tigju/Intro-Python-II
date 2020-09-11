# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item
class Room:
    def __init__(self, name, description, items, n_to=None, s_to=None, w_to=None, e_to=None):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.s_to = s_to
        self.w_to = w_to
        self.e_to = e_to
        self.items = items
    
    def __str__(self):
        ret = f"{self.name}, {self.description}\n"
        if len(self.items) > 0:
            ret += "Look you have something here:\n\n"
            for i, c in enumerate(self.items):
                ret += f"    {i + 1}. {c.name[0]}, {c.description}\n"
        else:
            ret += "Nothing you can find here...\n\n"
        return ret

    def add_item(self, item):
        self.items.append(item)
    
    def remove_item(self, item):
        self.items.remove(item)
    
    def show_items(self):
        ret = ''
        if len(self.items) > 0:
            for i, c in enumerate(self.items):
                ret += f"    {i + 1}. {c.name[0]}, {c.description}\n"
        else:
            ret += "Nothing here...\n"
        return ret

