from item import Item


class Weapon(Item):
    def __init__(self, name, description, damage_points=10):
        super().__init__(name, description)
        self.damage_points = damage_points
    
    def __str__(self):
        return f"{self.name}, {self.description}, damage points: {self. damage_points}"