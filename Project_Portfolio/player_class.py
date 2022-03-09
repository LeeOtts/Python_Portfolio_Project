### Player Class ###
class Player:
    def __init__(self):
        self.name = ''
        self.hp = 10
        self.shield = 2
        self.damage = 1
        self.location = 'b3'

    def add_health(self, health_added):
        self.hp += health_added

    def attack(self, Enemy):
        self.damage -= Enemy.hp
