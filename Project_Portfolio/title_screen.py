import os
from monty import title_screen_selections, prompt


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
