from item import Item


class Treasure(Item):
    def __init__(self, name, description, value=100):
        super().__init__(name, description)
        self.value = value

    def __str__(self):
        return f"{self.name}, {self.description}, value: {self.value}"