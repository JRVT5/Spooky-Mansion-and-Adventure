import json, os, sys, time, random

def main():
    x=os.listdir()
    n=0
    lst=[]
    print("Which file would you like to play?")
    for file in x: 
        if '.json' in file:
            print("  {}. {}".format(n+1, file))
            n+=1
            lst.append(file)
        else:
            pass
    choice= input("> ").lower().strip()
    num = int(choice)-1
    selected = lst[num]
    with open(str(selected)) as fp:
        game = json.load(fp)
    if selected=="spooky_mansion.json":
        print_instructions()
        print("You are about to play '{}'! Good luck!".format(game['__metadata__']['title']))
        print("")
        play1(game)
    elif selected=="adventure.json":
        print_instructions()
        print("You are about to play '{}'! Good luck!".format(game['__metadata__']['title']))
        print("")
        play2(game)
    

def play1(rooms):
    start=time.time()
    # Where are we? Look in __metadata__ for the room we should start in first.
    current_place = rooms['__metadata__']['start']
    # The things the player has collected.
    stuff = ['Cell Phone; no signal or battery...']

    while True:
        # Figure out what room we're in -- current_place is a name.
        here = rooms[current_place]
        # Print the description.
        print(here["description"])
        
        print("Items in room:", here["items"])
        
        for i in rooms:
            for exit in here['exits']:
                x=exit.get('destination')
                if x in rooms:
                    pass
                else:
                    print("Error: Some destinations don't exist.")
                    return
            continue
            
        
        # Is this a game-over?
        if here.get("ends_game", False):
            break

        # Allow the user to choose an exit:
        usable_exits = find_usable_exits(here, stuff)
        # Print out numbers for them to choose:
        for i, exit in enumerate(usable_exits):
            print("  {}. {}".format(i+1, exit['description']))

        # See what they typed:
        action = input("> ").lower().strip()
        
        if action=='help':
            print_instructions()
            continue
        
        elif action=='stuff':
            if len(stuff)>0:
                print (stuff)
                continue
            else:
                print("You have nothing.")
                continue
            
        elif action=='take':
            if len(here["items"])>0:
                x=here['items'].pop()
                stuff.append(x)
                print("Your current stuff:", stuff)
                continue
            else:
                print("There are no items to take here.")
                continue
            
        elif action=='drop':
            n=0
            print("What item would you like to drop?")
            for i in range(len(stuff)):
                print("  {}. {}".format(i+1, stuff[n]))
                n+=1
            choice= input("> ").lower().strip()
            num = int(choice) - 1
            selected = stuff[num]
            print("Dropped Item:",selected)
            stuff.pop(num)
            print("Current Items:",stuff)
            continue
        
        elif action in ["search","find"]:
            for exit in here['exits']:
                exit["hidden"]=False
            continue
        
        # If they type any variant of quit; exit the game.    
        elif action in ["quit", "escape", "exit", "q"]:
            print("You quit.")
            break
        
        # TODO: if they type "stuff", print any items they have (check the stuff list!)
        # TODO: if they type "take", grab any items in the room.
        # TODO: if they type "search", or "find", look through any exits in the room that might be hidden, and make them not hidden anymore!
        
        # Try to turn their action into an exit, by number.
        try:
            num = int(action) - 1
            selected = usable_exits[num]
            current_place = selected['destination']
            print("...")
        except:
            print("I don't understand '{}'...".format(action))
        
    print("")
    print("")
    end=time.time()
    finish=end-start
    print("=== GAME OVER ===")
    print("Time elapsed:", time.strftime("%H:%M:%S", time.gmtime(finish)))

def play2(rooms):
    print("Find the transcript and exit the building to win the game!")
    start=time.time()
    # Where are we? Look in __metadata__ for the room we should start in first.
    current_place = rooms['__metadata__']['start']
    # The things the player has collected.
    stuff = ['Pencil']

    while True:
        # Figure out what room we're in -- current_place is a name.
        here = rooms[current_place]
        # Print the description.
        print(here["description"])
        
        print("Items in room:", here["items"])
    
        for i in rooms:
            for exit in here['exits']:
                x=exit.get('destination')
                if x in rooms:
                    pass
                else:
                    print("Error: Some destinations don't exist.")
                    return
            continue
        
        if current_place=="janitors_closet":
            code="1234"
            guess=input("Enter the 4 digit code to leave the room:")    
            if guess==code:
                pass
            else:
                print("Inncorrect Password. Try again.")
                aid=input("Would you like a hint? Yes or No: ")
                if aid in ["yes", "Yes"]:
                    print("Hint: 1_3_")
                    continue
                else:
                    continue
                
        # Is this a game-over?
        if here.get("ends_game", False):
            break

        # Allow the user to choose an exit:
        usable_exits = find_usable_exits(here, stuff)
        # Print out numbers for them to choose:
        for i, exit in enumerate(usable_exits):
            print("  {}. {}".format(i+1, exit['description']))

        # See what they typed:
        action = input("> ").lower().strip()
        
        if action=='help':
            print_instructions()
            continue
        
        elif action=='stuff':
            if len(stuff)>0:
                print (stuff)
                continue
            else:
                print("You have nothing.")
                continue
            
        elif action=='take':
            if len(here["items"])>0:
                x=here['items'].pop()
                stuff.append(x)
                print("Your current stuff:", stuff)
                continue
            else:
                print("There are no items to take here.")
                continue
            
        elif action=='drop':
            n=0
            print("What item would you like to drop?")
            for i in range(len(stuff)):
                print("  {}. {}".format(i+1, stuff[n]))
                n+=1
            choice= input("> ").lower().strip()
            num = int(choice) - 1
            selected = stuff[num]
            print("Dropped Item:",selected)
            stuff.pop(num)
            print("Current Items:",stuff)
            continue
        
        elif action in ["search","find"]:
            for exit in here['exits']:
                exit["hidden"]=False
            continue
        
        # If they type any variant of quit; exit the game.    
        elif action in ["quit", "escape", "exit", "q"]:
            print("You quit.")
            break
        
        # TODO: if they type "stuff", print any items they have (check the stuff list!)
        # TODO: if they type "take", grab any items in the room.
        # TODO: if they type "search", or "find", look through any exits in the room that might be hidden, and make them not hidden anymore!
        
        # Try to turn their action into an exit, by number.
        try:
            num = int(action) - 1
            selected = usable_exits[num]
            current_place = selected['destination']
            print("...")
        except:
            print("I don't understand '{}'...".format(action))
        
    print("")
    print("")
    end=time.time()
    finish=end-start
    print("=== GAME OVER ===")
    print("Time elapsed:", time.strftime("%H:%M:%S", time.gmtime(finish)))


def find_usable_exits(room, stuff):
    """
    Given a room, and the player's stuff, find a list of exits that they can use right now.
    That means the exits must not be hidden, and if they require a key, the player has it.

    RETURNS
     - a list of exits that are visible (not hidden) and don't require a key!
    """
    usable = []
    for exit in room['exits']:
        if exit.get("hidden", False):
            continue
        if "required_key" in exit:
            if exit["required_key"] in stuff:
                usable.append(exit)
            continue
        usable.append(exit)
    return usable

def print_instructions():
    print("=== Instructions ===")
    print(" - Type a number to select an exit.")
    print(" - Type 'stuff' to see what you're carrying.")
    print(" - Type 'take' to pick up an item.")
    print(" - Type 'quit' to exit the game.")
    print(" - Type 'search' or 'find' to take a deeper look at a room.")
    print(" - Type 'help' to reprint the instructions.")
    print("=== Instructions ===")
    print("")
    

if __name__ == '__main__':
    main()
