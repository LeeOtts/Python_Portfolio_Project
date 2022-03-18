### Player Class ###

class Player:
    def __init__(self):
        self.name = ''
        self.hp = 10
        self.shield = 2
        self.damage = 1
        self.location = 'b3'
        self.status_effect = 'no_quest'
        self.finished = False

    def add_health(self, health_added):
        self.hp += health_added

    def player_attack(self, Enemy):
        Enemy.hp -= self.damage

### Enemies Class ###

class Enemy:
    def __init__(self):
        self.name = ""
        self.hp = 5
        self.attack = 1

        def enemy_attack(self, player):
            player.hp -= self.attack