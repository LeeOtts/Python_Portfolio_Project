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

    def add_health(self, health_added):
        self.hp += health_added

    def attack(self, Enemy):
        self.damage -= Enemy.hp

# Calling player as Player Class
player = Player()

### Enemy Class ###

class Enemy:
    def __init__(self, name):
        self.name = name
        self.hp = 5
        self.attack = 1

black_knight = Enemy("Black Knight")

### Title Screen and Section ###

def title_screen_selections():
    option = input(">")
    if option.lower() == ("play"):
        start_game()  # START GAME PLACEHOLDER
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        print("Run Away... Run Awaaay... run away")
        quit()
    while option.lower() not in ["play", "help", "quit"]:
        print("Please enter a valid command")
        option = input(">")
        if option.lower() == ("play"):
            start_game()  # START GAME PLACEHOLDER
        elif option.lower() == ("help"):
            help_menu()  # HELP MENU PLACEHOLDER
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
ZONENAME: ""
DESCRIPTION: "description"
EXAMINATION: "examine"
PREVIOUS_VISIT: False
UP: "up", "north"
DOWN: "down", "south"
LEFT: "left", "west"
RIGHT: "right", "east"

previous_visit_places = {
    'a1': False, 'a2': False, 'a3': False, 'a4': False,
    'b1': False, 'b2': False, 'b3': False, 'b4': False,
    'c1': False, 'c2': False, 'c3': False, 'c4': False,
    'd1': False, 'd2': False, 'd3': False, 'd4': False,
}

zonemap = {
    'a1': {
        ZONENAME: "",
        DESCRIPTION: "description",
        EXAMINATION: "examine",
        PREVIOUS_VISIT: False,
        UP: "",
        DOWN: "b1",
        LEFT: "",
        RIGHT: "a2",
    },
    'a2': {
        ZONENAME: "",
        DESCRIPTION: "description",
        EXAMINATION: "examine",
        PREVIOUS_VISIT: False,
        UP: "",
        DOWN: "b2",
        LEFT: "a1",
        RIGHT: "a3"
    },
    'a3': {
        ZONENAME: "",
        DESCRIPTION: "description",
        EXAMINATION: "examine",
        PREVIOUS_VISIT: False,
        UP: "",
        DOWN: "b3",
        LEFT: "a2",
        RIGHT: "a4",
    },
    'a4': {
        ZONENAME: "",
        DESCRIPTION: "description",
        EXAMINATION: "examine",
        PREVIOUS_VISIT: False,
        UP: "",
        DOWN: "b4",
        LEFT: "a3",
        RIGHT: "",
    },
    'b1': {
        ZONENAME: "",
        DESCRIPTION: "description",
        EXAMINATION: "examine",
        PREVIOUS_VISIT: False,
        UP: "a1",
        DOWN: "c1",
        LEFT: "",
        RIGHT: "b2",
    },
    'b2': {
        ZONENAME: "",
        DESCRIPTION: "description",
        EXAMINATION: "examine",
        PREVIOUS_VISIT: False,
        UP: "a2",
        DOWN: "c2",
        LEFT: "b1",
        RIGHT: "b3",
    },
    'b3': {
        ZONENAME: "Starting Point",
        DESCRIPTION: "You started here",
        EXAMINATION: "examine",
        PREVIOUS_VISIT: False,
        UP: "a3",
        DOWN: "c3",
        LEFT: "b2",
        RIGHT: "b4",
    },
    'b4': {
        ZONENAME: "",
        DESCRIPTION: "description",
        EXAMINATION: "examine",
        PREVIOUS_VISIT: False,
        UP: "a4",
        DOWN: "c4",
        LEFT: "b3",
        RIGHT: "",
    },
    'c1': {
        ZONENAME: "Camelot",
        DESCRIPTION: "Tis a silly place",
        EXAMINATION: "examine",
        PREVIOUS_VISIT: False,
        UP: "b1",
        DOWN: "d1",
        LEFT: "",
        RIGHT: "c2",
    },
    'c2': {
        ZONENAME: "",
        DESCRIPTION: "description",
        EXAMINATION: "examine",
        PREVIOUS_VISIT: False,
        UP: "b2",
        DOWN: "d2",
        LEFT: "c1",
        RIGHT: "c3",
    },
    'c3': {
        ZONENAME: "",
        DESCRIPTION: "description",
        EXAMINATION: "examine",
        PREVIOUS_VISIT: False,
        UP: "b3",
        DOWN: "d3",
        LEFT: "c2",
        RIGHT: "c4",
    },
    'c4': {
        ZONENAME: "",
        DESCRIPTION: "description",
        EXAMINATION: "examine",
        PREVIOUS_VISIT: False,
        UP: "b4",
        DOWN: "d4",
        LEFT: "c3",
        RIGHT: "",
    },
    'd1': {
        ZONENAME: "",
        DESCRIPTION: "description",
        EXAMINATION: "examine",
        PREVIOUS_VISIT: False,
        UP: "c1",
        DOWN: "",
        LEFT: "",
        RIGHT: "d2",
    },
    'd2': {
        ZONENAME: "",
        DESCRIPTION: "description",
        EXAMINATION: "examine",
        PREVIOUS_VISIT: False,
        UP: "c2",
        DOWN: "",
        LEFT: "d1",
        RIGHT: "d3",
    },
    'd3': {
        ZONENAME: "",
        DESCRIPTION: "description",
        EXAMINATION: "examine",
        PREVIOUS_VISIT: False,
        UP: "c3",
        DOWN: "",
        LEFT: "d2",
        RIGHT: "d4",
    },
    'd4': {
        ZONENAME: "",
        DESCRIPTION: "description",
        EXAMINATION: "examine",
        PREVIOUS_VISIT: False,
        UP: "c4",
        DOWN: "",
        LEFT: "d3",
        RIGHT: "",
    },
}

### Game Interaction ###
### Game Function ###

def start_game():
    print("\nHello good Knight.")
    print("I am Arther, King of the Brittons.")
    print("Thank you joining my Quest for the Holy Grail?\n")
    player.name = input("What shall I call you brave knight? ")
    print(f"\nI dub thee, Sir {player.name}, Knight of the Round Table")