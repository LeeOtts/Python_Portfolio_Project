# Monty.py: A Text Based RPG
# Python Fundamentals Portfolio Project
# By: Lee Otts

### Imports ###
import random
import sys
import os
import textwrap
import time
import cmd


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


class Enemy:
    def __init__(self):
        self.name = ""
        self.hp = 5
        self.attack = 1

        def enemy_attack(self, player):
            player.hp -= self.attack


# Calling player as Player Class
player = Player()

# Calling enemies


ZONENAME = ""
DESCRIPTION = "description"
EXAMINATION = "examine"
PREVIOUS_VISIT = False
UP = "up", "north"
DOWN = "down", "south"
LEFT = "left", "west"
RIGHT = "right", "east"

previous_visit_places = {
    'a1': False, 'a2': False, 'a3': False, 'a4': False,
    'b1': False, 'b2': False, 'b3': False, 'b4': False,
    'c1': False, 'c2': False, 'c3': False, 'c4': False,
    'd1': False, 'd2': False, 'd3': False, 'd4': False,
}

### Maps ###

### Map is 4x4 Grid ###
"""
    a1   a2   a3    a4
   ---------------------
a1 |    |    |    |    | a4
   ---------------------
b1 |    |    |    |    | b4
   ---------------------
c1 |    |    |    |    | c4
   ---------------------
d1 |    |    |    |    | d4
   ---------------------
     d1   d2   d3   d4
"""


def map_a1():
    print('\n')
    print("    a1   a2   a3    a4")
    print("   ---------------------")
    print("a1 | X  |    |    |    | a4")
    print("   ---------------------")
    print("b1 |    |    |    |    | b4")
    print("   ---------------------")
    print("c1 |    |    |    |    | c4")
    print("   ---------------------")
    print("d1 |    |    |    |    | d4")
    print("   ---------------------")
    print("     d1   d2   d3   d4")
    print('\n')


def map_a2():
    print('\n')
    print("    a1   a2   a3    a4")
    print("   ---------------------")
    print("a1 |    | X  |    |    | a4")
    print("   ---------------------")
    print("b1 |    |    |    |    | b4")
    print("   ---------------------")
    print("c1 |    |    |    |    | c4")
    print("   ---------------------")
    print("d1 |    |    |    |    | d4")
    print("   ---------------------")
    print("     d1   d2   d3   d4")
    print('\n')


def map_a3():
    print('\n')
    print("    a1   a2   a3    a4")
    print("   ---------------------")
    print("a1 |    |    | X  |    | a4")
    print("   ---------------------")
    print("b1 |    |    |    |    | b4")
    print("   ---------------------")
    print("c1 |    |    |    |    | c4")
    print("   ---------------------")
    print("d1 |    |    |    |    | d4")
    print("   ---------------------")
    print("     d1   d2   d3   d4")
    print('\n')


def map_a4():
    print('\n')
    print("    a1   a2   a3    a4")
    print("   ---------------------")
    print("a1 |    |    |    | X  | a4")
    print("   ---------------------")
    print("b1 |    |    |    |    | b4")
    print("   ---------------------")
    print("c1 |    |    |    |    | c4")
    print("   ---------------------")
    print("d1 |    |    |    |    | d4")
    print("   ---------------------")
    print("     d1   d2   d3   d4")
    print('\n')


def map_b1():
    print('\n')
    print("    a1   a2   a3    a4")
    print("   ---------------------")
    print("a1 |    |    |    |    | a4")
    print("   ---------------------")
    print("b1 | X  |    |    |    | b4")
    print("   ---------------------")
    print("c1 |    |    |    |    | c4")
    print("   ---------------------")
    print("d1 |    |    |    |    | d4")
    print("   ---------------------")
    print("     d1   d2   d3   d4")
    print('\n')


def map_b2():
    print('\n')
    print("    a1   a2   a3    a4")
    print("   ---------------------")
    print("a1 |    |    |    |    | a4")
    print("   ---------------------")
    print("b1 |    | X  |    |    | b4")
    print("   ---------------------")
    print("c1 |    |    |    |    | c4")
    print("   ---------------------")
    print("d1 |    |    |    |    | d4")
    print("   ---------------------")
    print("     d1   d2   d3   d4")
    print('\n')


def map_b3():
    print('\n')
    print("    a1   a2   a3    a4")
    print("   ---------------------")
    print("a1 |    |    |    |    | a4")
    print("   ---------------------")
    print("b1 |    |    | X  |    | b4")
    print("   ---------------------")
    print("c1 |    |    |    |    | c4")
    print("   ---------------------")
    print("d1 |    |    |    |    | d4")
    print("   ---------------------")
    print("     d1   d2   d3   d4")
    print('\n')


def map_b4():
    print('\n')
    print("    a1   a2   a3    a4")
    print("   ---------------------")
    print("a1 |    |    |    |    | a4")
    print("   ---------------------")
    print("b1 |    |    |    | X  | b4")
    print("   ---------------------")
    print("c1 |    |    |    |    | c4")
    print("   ---------------------")
    print("d1 |    |    |    |    | d4")
    print("   ---------------------")
    print("     d1   d2   d3   d4")
    print('\n')


def map_c1():
    print('\n')
    print("    a1   a2   a3    a4")
    print("   ---------------------")
    print("a1 |    |    |    |    | a4")
    print("   ---------------------")
    print("b1 |    |    |    |    | b4")
    print("   ---------------------")
    print("c1 | X  |    |    |    | c4")
    print("   ---------------------")
    print("d1 |    |    |    |    | d4")
    print("   ---------------------")
    print("     d1   d2   d3   d4")
    print('\n')


def map_c2():
    print('\n')
    print("    a1   a2   a3    a4")
    print("   ---------------------")
    print("a1 |    |    |    |    | a4")
    print("   ---------------------")
    print("b1 |    |    |    |    | b4")
    print("   ---------------------")
    print("c1 |    | X  |    |    | c4")
    print("   ---------------------")
    print("d1 |    |    |    |    | d4")
    print("   ---------------------")
    print("     d1   d2   d3   d4")
    print('\n')


def map_c3():
    print('\n')
    print("    a1   a2   a3    a4")
    print("   ---------------------")
    print("a1 |    |    |    |    | a4")
    print("   ---------------------")
    print("b1 |    |    |    |    | b4")
    print("   ---------------------")
    print("c1 |    |    | X  |    | c4")
    print("   ---------------------")
    print("d1 |    |    |    |    | d4")
    print("   ---------------------")
    print("     d1   d2   d3   d4")
    print('\n')


def map_c4():
    print('\n')
    print("    a1   a2   a3    a4")
    print("   ---------------------")
    print("a1 |    |    |    |    | a4")
    print("   ---------------------")
    print("b1 |    |    |    |    | b4")
    print("   ---------------------")
    print("c1 |    |    |    | X  | c4")
    print("   ---------------------")
    print("d1 |    |    |    |    | d4")
    print("   ---------------------")
    print("     d1   d2   d3   d4")
    print('\n')


def map_d1():
    print('\n')
    print("    a1   a2   a3    a4")
    print("   ---------------------")
    print("a1 |    |    |    |    | a4")
    print("   ---------------------")
    print("b1 |    |    |    |    | b4")
    print("   ---------------------")
    print("c1 |    |    |    |    | c4")
    print("   ---------------------")
    print("d1 | X  |    |    |    | d4")
    print("   ---------------------")
    print("     d1   d2   d3   d4")
    print('\n')


def map_d2():
    print('\n')
    print("    a1   a2   a3    a4")
    print("   ---------------------")
    print("a1 |    |    |    |    | a4")
    print("   ---------------------")
    print("b1 |    |    |    |    | b4")
    print("   ---------------------")
    print("c1 |    |    |    |    | c4")
    print("   ---------------------")
    print("d1 |    | X  |    |    | d4")
    print("   ---------------------")
    print("     d1   d2   d3   d4")
    print('\n')


def map_d3():
    print('\n')
    print("    a1   a2   a3    a4")
    print("   ---------------------")
    print("a1 |    |    |    |    | a4")
    print("   ---------------------")
    print("b1 |    |    |    |    | b4")
    print("   ---------------------")
    print("c1 |    |    |    |    | c4")
    print("   ---------------------")
    print("d1 |    |    | X  |    | d4")
    print("   ---------------------")
    print("     d1   d2   d3   d4")
    print('\n')


def map_d4():
    print('\n')
    print("    a1   a2   a3    a4")
    print("   ---------------------")
    print("a1 |    |    |    |    | a4")
    print("   ---------------------")
    print("b1 |    |    |    |    | b4")
    print("   ---------------------")
    print("c1 |    |    |    |    | c4")
    print("   ---------------------")
    print("d1 |    |    |    | X  | d4")
    print("   ---------------------")
    print("     d1   d2   d3   d4")
    print('\n')


### ZoneMap ###
### Uses a nested dictionary ###
zonemap = {
    'a1': {
        ZONENAME: "Castle Anthrax",
        DESCRIPTION: "You are wounded. I will fetch the doctor",
        # Must use runaway method to escape. Use add_health method
        # + add_health(2),
        EXAMINATION: "You walk into a large room, full of woman in white gowns.",
        PREVIOUS_VISIT: False,
        UP: "",
        DOWN: "b1",
        LEFT: "",
        RIGHT: "a2",
    },
    'a2': {
        ZONENAME: "Lone Bridge",
        DESCRIPTION: "You come to a lone bridge.\n You see a furious battle between two knights.\nOne of them is wearing black armour.",
        # BlackKnight Fight Placeholder
        EXAMINATION: "trigger black knight fight",
        PREVIOUS_VISIT: False,
        UP: "",
        DOWN: "b2",
        LEFT: "a1",
        RIGHT: "a3"
    },
    'a3': {
        ZONENAME: "Small Town",
        DESCRIPTION: "You enter a small town",
        EXAMINATION: "You see priests walking around chanting.\n In the west part of the town you see a group of people gathering ",
        PREVIOUS_VISIT: False,
        UP: "",
        DOWN: "b3",
        LEFT: "a2",
        RIGHT: "a4",
    },
    'a4': {
        ZONENAME: "Western Part of Town",
        DESCRIPTION: "You hear the crowd yelling 'Witch' and 'Burn Her'.\n The crown brings the woman to a knight dressed in blue.",
        ##
        EXAMINATION: "a4 examine",
        PREVIOUS_VISIT: False,
        UP: "",
        DOWN: "b4",
        LEFT: "a3",
        RIGHT: "",
    },
    'b1': {
        ZONENAME: "Autonomous Collective",
        DESCRIPTION: "You see an old ma'am pulling a cart.\n I'm sorry you see an old MAN pulling a cart",
        EXAMINATION: "b1 examine",
        PREVIOUS_VISIT: False,
        UP: "a1",
        DOWN: "c1",
        LEFT: "",
        RIGHT: "b2",
    },
    'b2': {
        ZONENAME: "Small Town",
        DESCRIPTION: "A small town near the middle of the map.",
        EXAMINATION: "Bring 'Out your dead",
        PREVIOUS_VISIT: False,
        UP: "a2",
        DOWN: "c2",
        LEFT: "b1",
        RIGHT: "b3",
    },
    'b3': {
        ZONENAME: "Starting Point",
        DESCRIPTION: "This is where you started. You are on top of a foggy hill",
        EXAMINATION: "examine",
        PREVIOUS_VISIT: False,
        UP: "a3",
        DOWN: "c3",
        LEFT: "b2",
        RIGHT: "b4",
    },
    'b4': {
        ZONENAME: "b4 zonename",
        DESCRIPTION: "b4 description",
        EXAMINATION: "b4 examine",
        PREVIOUS_VISIT: False,
        UP: "a4",
        DOWN: "c4",
        LEFT: "b3",
        RIGHT: "",
    },
    'c1': {
        ZONENAME: "Camelot",
        DESCRIPTION: "Tis a silly place",
        EXAMINATION: "You see knights signing and dancing around the Round table",
        PREVIOUS_VISIT: False,
        UP: "b1",
        DOWN: "d1",
        LEFT: "",
        RIGHT: "c2",
    },
    'c2': {
        ZONENAME: "c2 zonename",
        DESCRIPTION: "c2 description",
        EXAMINATION: "c2 examine",
        PREVIOUS_VISIT: False,
        UP: "b2",
        DOWN: "d2",
        LEFT: "c1",
        RIGHT: "c3",
    },
    'c3': {
        ZONENAME: "c3 zonename",
        DESCRIPTION: "c3 description",
        EXAMINATION: "c3 examine",
        PREVIOUS_VISIT: False,
        UP: "b3",
        DOWN: "d3",
        LEFT: "c2",
        RIGHT: "c4",
    },
    'c4': {
        ZONENAME: "Foggy patch of forest",
        DESCRIPTION: "A little further down the pass you hear 'Ni'!",
        ### Add shrubbery pickup to player class ###
        EXAMINATION: "You see a group of knights. They demand you find a shrubbery to pass",
        PREVIOUS_VISIT: False,
        UP: "b4",
        DOWN: "d4",
        LEFT: "c3",
        RIGHT: "",
    },
    'd1': {
        ZONENAME: "d1 zone",
        DESCRIPTION: "d1 description",
        EXAMINATION: "d1 examine",
        PREVIOUS_VISIT: False,
        UP: "c1",
        DOWN: "",
        LEFT: "",
        RIGHT: "d2",
    },
    'd2': {
        ZONENAME: "d2 zone",
        DESCRIPTION: "d2 description",
        EXAMINATION: "d2 examine",
        PREVIOUS_VISIT: False,
        UP: "c2",
        DOWN: "",
        LEFT: "d1",
        RIGHT: "d3",
    },
    'd3': {
        ZONENAME: "d3 zone",
        DESCRIPTION: "d3 description",
        EXAMINATION: "d3 examine",
        PREVIOUS_VISIT: False,
        UP: "c3",
        DOWN: "",
        LEFT: "d2",
        RIGHT: "d4",
    },
    'd4': {
        ZONENAME: "d4 zone",
        DESCRIPTION: "d4 description",
        EXAMINATION: "d4 examine",
        PREVIOUS_VISIT: False,
        UP: "c4",
        DOWN: "",
        LEFT: "d3",
        RIGHT: "",
    },
}

# Title and Help Screen


def title_screen_selections():
    option = input("> ")
    if option.lower() == ("play"):
        start_game()
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        print("Run Away... Run Awaaay... run away")
        quit()
    while option.lower() not in ["play", "help", "quit"]:
        print("Please enter a valid command")
        option = input("> ")
        if option.lower() == ("play"):
            start_game()
        elif option.lower() == ("help"):
            help_menu()
        elif option.lower() == ("quit"):
            print("Run Away... Run Awaaay... run away")
            quit()


def title_screen():
    os.system('Clear')
    print("##########################################")
    print("#          My Portfolio Project          #")
    print("#                                        #")
    print("#                Monty.Py                #")
    print("#                Text RPG                #")
    print("#                                        #")
    print("#                          By: Lee Otts  #")
    print("##########################################")
    print("#               - Play -                 #")
    print("#               - Help -                 #")
    print("#               - Quit -                 #")
    print("##########################################")
    title_screen_selections()


def help_menu():
    print("##########################################")
    print("#               Help Menu                #")
    print("#                                        #")
    print("#                Monty.Py                #")
    print("#                Text RPG                #")
    print("#                                        #")
    print("##########################################")
    print("#  - Use up, down, left, right to move - #")
    print("#   - Type your commands to do them -    #")
    print("#   - Use 'look' to inspect location -   #")
    print("#             - Good Luck -              #")
    print("##########################################")
    title_screen_selections()


def in_game_help_menu():
    print("##########################################")
    print("#               Help Menu                #")
    print("#                                        #")
    print("#                Monty.Py                #")
    print("#                Text RPG                #")
    print("#                                        #")
    print("##########################################")
    print("#     - Use up, down, left, right -      #")
    print("#   - Type your commands to do them -    #")
    print("#   - Use 'look' to inspect location -   #")
    print("#             - Good Luck -              #")
    print("##########################################")
    prompt()

### Game Interaction ###


def print_location():
    print('\n' + ('#' * (5 + len(player.location))))
    print('#' + player.location.upper() + '#')
    print('#' + zonemap[player.location][DESCRIPTION] + '#')
    print('\n' + ('#' * (5 + len(player.location))))


def prompt():
    print("\n")
    print("====================")
    print("What would you like to do?")
    action = input("> ")
    acceptable_actions = ['move', 'go', 'travel', 'walk',
                          'quit', 'look', 'examine', 'attack', 'hit', 'help', 'map']
    while action.lower() not in acceptable_actions:
        print("Not a accepted action, try again.\n")
        action = input("> ")
    
    if action.lower() == 'quit':
        print("Run Away... Run Awaaay... run away")
        sys.exit()
    elif action.lower() in ['move', 'go', 'travel', 'walk']:
        player_move(action.lower())
    elif action.lower() in ['look', 'examine']:
        player_examine(action.lower())

    elif action.lower() == 'help':
        in_game_help_menu()

    elif action.lower() in ['attack', 'hit']:
        print("Add attack action")


def player_move(myAction):
    ask = "Where would you like to move to?\n"
    dest = input(ask)
    if dest in ['up', 'north', 'n']:
        destination = zonemap[player.location][UP]
        movement_handler(destination)
    elif dest in ['down', 'south', 's']:
        destination = zonemap[player.location][DOWN]
        movement_handler(destination)
    elif dest in ['left', 'west', 'w']:
        destination = zonemap[player.location][LEFT]
        movement_handler(destination)
    elif dest in ['right', 'east', 'e']:
        destination = zonemap[player.location][RIGHT]
        movement_handler(destination)


def movement_handler(destination):
    print(f'\nYou have moved to the {destination}.')
    player.location = destination
    print_location()


def player_examine(action):
    if zonemap[player.location][PREVIOUS_VISIT] == True:
        print('You have been here before')
    else:
        # Trigger event / enemy
        print('Trigger enemy')


### Game Function ###

def main_game_loop():
    while player.finished is False:
        prompt()


def start_game():
    arthur_greeting = "Hello good Knight.\n I am Arthur, King of the Brittons.\nThank you joining me\n"
    for character in arthur_greeting:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    whats_your_name = "What shall I call you brave knight?\n "
    for character in whats_your_name:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_name = input('> ')
    player.name = player_name
    dub = f"I dub thee Sir {player.name}, Knight of Camelot.\n"
    for character in dub:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.02)
    time.sleep(2)
    os.system('Clear')
    print('####################')
    print('#      England     #')
    print('#      932 a.d.    #')
    print('####################')
    main_game_loop()


title_screen()
