# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room, inventory):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory

    def __str__(self):
        ret = f"{self.name}, {self.current_room}\n"
        if len(self.inventory) > 0:
            ret += "You have collected these items:\n"
            for i, c in enumerate(self.inventory):
                ret += f"    {i + 1}. {c.name}, {c.description}\n"
        if self.inventory == 0:
            ret += "Your basket is empty"

        return ret

    def get_item(self, item):
        self.inventory.append(item)

    def drop_item(self, item):
        self.inventory.remove(item)
    
    def show_inventory(self):
        ret = ''
        if len(self.inventory) > 0:
            ret += "You have collected these items:\n"
            for i, c in enumerate(self.inventory):
                ret += f"    {i + 1}. {c.name[0]}, {c.description}\n"
        else:
            ret += "Your basket is empty\n"
        return ret
