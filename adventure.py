import json

# This global dictionary stores the name of the room as the key and the dictionary describing the room as the value.
GAME = {
    '__metadata__': {
        'title': 'Adventure',
        'start': 'classroom'
    }
}

def create_room(name, description, ends_game=False):
    """
    Create a dictionary that represents a room in our game.

    INPUTS:
     name: string used to identify the room; think of this as a variable name.
     description: string used to describe the room to the user.
     ends_game: boolean, True if arriving in this room ends the game.
    
    RETURNS:
     the dictionary describing the room; also adds it to GAME!
    """
    assert (name not in GAME)
    room = {
        'name': name,
        'description': description,
        'exits': [],
        'items': [],
    }
    # Does this end the game?
    if ends_game:
        room['ends_game'] = ends_game

    # Stick it into our big dictionary of all the rooms.
    GAME[name] = room
    return room

def create_exit(source, destination, description, required_key=False, hidden=False):
    """
    Rooms are useless if you can't get to them! This function connects source to destination (in one direction only.)

    INPUTS:
     source: which room to put this exit into (or its name)
     destination: where this exit goes (or its name)
     description: how to show this exit to the user (ex: "There is a red door.")
     required_key (optional): string of an item that is needed to open/reveal this door.
     hidden (optional): set this to True if you want this exit to be hidden initially; until the user types 'search' in the source room.
    """
    # Make sure source is our room!
    if isinstance(source, str):
        source = GAME[source]
    # Make sure destination is a room-name!
    if isinstance(destination, dict):
        destination = destination['name']
    # Create the "exit":
    exit = {
        'destination': destination,
        'description': description
    }
    if required_key:
        exit['required_key'] = required_key
    # Do we need to search for this?
    if hidden:
        exit['hidden'] = hidden
    source['exits'].append(exit)
    return exit

key="Office Box Key"
transcript="Transcript"
apple="Apple"
broom="Broom"

classroom = create_room("classroom", "You're in a lecture hall, for some reason.")
create_exit(classroom, 'hallway', "A door leads into the hall.")
create_exit(classroom, 'teachers_lounge', "An open door in the classroom leads to the lounge.")

hallway = create_room("hallway", "This is a hallway with many locked doors.")
create_exit(hallway, 'classroom', "Go back into the classroom.")
create_exit(hallway, 'staircase', "A door with the words STAIRS is stuck open.")
create_exit(hallway, 'office', "Go into the Principal's office.")

janitors_closet = create_room("janitors_closet", "A strange, musty smelling closet. The door locks behhind you but there is a key pad.")
janitors_closet["items"].append(broom)
create_exit(janitors_closet, 'teachers_lounge', "Return to the teacher's lounge. That was a close one.")

staircase = create_room("staircase", "The staircase leads downward.")
create_exit(staircase, 'hallway', "Nevermind; go back to the hallway.")
create_exit(staircase, 'outside', "A door at the bottom of the stairs has a red, glowing, EXIT sign. But do you have the transcript?", required_key=transcript)

staircase2 = create_room("staircase2", "A long dark staircase decends down.")
create_exit(staircase2, 'office', "Climb back up the big stone steps.")
create_exit(staircase2, 'bomb_shelter', "There's a strange looking room below.")

bomb_shelter = create_room("bomb_shelter", "The old, musty bomb shelter from WWII. It seems like there might be something here.")
create_exit(bomb_shelter, 'staircase2', "Go back up the staircase.")
create_exit(bomb_shelter, 'key_holder', "Grab the key.", hidden=True)

key_holder = create_room("key_holder", "A big office key hangs down.")
key_holder["items"].append(key)
create_exit(key_holder, 'bomb_shelter', "Return to the bomb shelter with the key.")

teachers_lounge = create_room("teachers_lounge", "This lounge is filled with books and smells like old coffee.")
teachers_lounge["items"].append(apple)
create_exit(teachers_lounge, 'classroom', "Return back to the classroom.")
create_exit(teachers_lounge, 'janitors_closet', "There is a janitors closet with the door slightly open.")

locked_box = create_room("locked_box","Your grades are inside. Exit now!")
locked_box["items"].append(transcript)
create_exit(locked_box, 'office', "Return to the office.")

office = create_room("office", "The office is dark and cold. There is a locked box. Find the key to open it.")
create_exit(office, 'hallway', "Go back into the hallway.")
create_exit(office, 'locked_box', "Open the locked box.", required_key=key)
create_exit(office, 'staircase2', "Descend down the eery stairs.")

outside = create_room("outside", "You've escaped! It's cold out.", ends_game=True)

# Save our text-adventure to a file:
##
with open('adventure.json', 'w') as out:
    json.dump(GAME, out, indent=2)
    
