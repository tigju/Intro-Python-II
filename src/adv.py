from room import Room
from player import Player
from item import Item

# Declare Items
item_dict = {
    'coins': Item("Coins", "Pile of coins - old gold"),
    'sword': Item("Sword", "Very sharp made out of steel"),
    'skull': Item("Skull", "As dry as a bone"),
    'apple': Item("Apple", "Eat this fresh apple to increase life points"),
    'hammer': Item("Hammer", "You can crush stones with it"),
    "diamond": Item("Diamond", "Very shiny"),
    "emerald": Item("Emerald", "The emerald has been known as a symbol of truth and love")
}

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", []),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [item_dict['apple']]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [item_dict['hammer']]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [item_dict['diamond'], item_dict['skull']]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [item_dict['coins'], item_dict['sword'], item_dict['emerald']]),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
my_player = Player('Caesar', room['outside'], [])
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

q = False
directions = {
    'n': 'North',
    'e': 'East',
    's': 'South',
    'w': 'West'
}
while q != True: 
    print(f'\n{my_player.name} is in {my_player.current_room}')
    print('-------------------------------------------------------------')
    print(f"{my_player.show_inventory()}")
    inp = input("Enter 'n', 'e', 's' or 'w' to move North, East, South or West otherwise enter 'q' to quit the game: ")
    
    if inp == 'q':
        q = True

    if len(inp.split(" ")) > 1:
        if inp.split(" ")[0] == 'get':
            for i in my_player.current_room.items:
                if i.name[0].lower() == inp.split(" ")[1].lower():
                    print(f"\nYou just picked {i.name[0]}")
                    my_player.get_item(i)
                    my_player.current_room.remove_item(i)

        if inp.split(" ")[0] == 'drop':
            for i in my_player.inventory:
                if i.name[0].lower() == inp.split(" ")[1].lower():
                    print(f"\nYou just picked {i.name[0]}")
                    my_player.current_room.add_item(i)
                    my_player.drop_item(i)

    # elif len(inp.split(" ")) == 1 and inp.split(" ")[0] == 'get':
    #     next_inp = input(f"what do you want to pick? you can choose: \n{my_player.current_room.show_items()}")
    #     if i.name[0].lower() == inp_next.split(" ")[0].lower():


    elif my_player.current_room.name == room['outside'].name:
        if inp == 'n':
            my_player.current_room = room['outside'].n_to
            print(f"{my_player.name} is moving {directions[inp]}...\n")
        else:    
            print("Try North!\n")

    elif my_player.current_room.name == room['foyer'].name:
        if inp == 'n':
            my_player.current_room = room['foyer'].n_to
            print(f"{my_player.name} is moving {directions[inp]}...\n")
        elif inp == 's':
            my_player.current_room = room['foyer'].s_to
            print(f"{my_player.name} is moving {directions[inp]}...\n")
        elif inp == 'e':
            my_player.current_room = room['foyer'].e_to
            print(f"{my_player.name} is moving {directions[inp]}...\n")
        elif inp == 'w':
            print("Try East or South!\n")
        else:
            print("Error! Could not undersand you! Try again")

    elif my_player.current_room.name == room['overlook'].name:
        if inp == 's':
            my_player.current_room = room['overlook'].s_to
            print(f"{my_player.name} is moving {directions[inp]}...\n")
        else:
            print("Nowhere to go except South!\n")
    
    elif my_player.current_room.name == room['narrow'].name:
        if inp == 'n':
            my_player.current_room = room['narrow'].n_to
            print(f"{my_player.name} is moving {directions[inp]}...\n")
        elif inp == 'w':
            my_player.current_room = room['narrow'].w_to
            print(f"{my_player.name} is moving {directions[inp]}...\n")
        else:
            print("Try North or West!\n")
    elif my_player.current_room.name == room['treasure'].name:
        if inp == 's':
            my_player.current_room = room['treasure'].s_to
            print(f"{my_player.name} is moving {directions[inp]}...\n")
        else:
            print("Go South!")
    else:
        print("Try 'n' for North, 'e' for East, 's' for South or 'w' for West\n")
        
    
