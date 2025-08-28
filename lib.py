
# return the object specified by the tags, in the node. Return None if it is not found.
def getObject(tag, node):
        children = node.children
        obj = None
        # check each child of the node
        for child in children:
                # if one of the tags in the list matches
                if tag in child.tags:
                        obj = child
        return obj

def go(passage, player):
        player.location.children.remove(player)
        player.location = passage.destination
        passage.destination.addChild(player)
        print(f"{passage.goText}")
        executeLook("around", player)


def executeGo(noun, player):

        obj = getObject(noun, player.location)
        # if the object is found
        if obj:
                # if object has a destination, go there
                if obj.destination:
                        # if the passage is closed
                        if obj.closed:
                                keyNeeded = obj.key
                                # check if player has the key
                                if keyNeeded in player.inventory:
                                        print(f"You unlock it using {keyNeeded.description}.")
                                        obj.closed = False
                                        go(obj, player)
                                else:
                                        print(f"It's locked.")
                        else:
                                # move player to location
                                go(obj, player)
                # object has no destination
                else:
                        print("You can't go there.")

        # object was not found
        else:
                print(f"That place doesn't exist here.")

# Examine the given noun at the location provided
def executeExamine(noun, location):
        obj = getObject(noun, location)
        if obj:
                print(f"There is {obj.description} here.")
        else:
                print(f"You don't see {noun} here.")


def isLit(obj):
        if obj.light or obj.destinatinIsLit() or obj.location.light:
                return True
        else:
                return False


# Returns true if an object can be noticed by the player, false otherwise.
# Something can be noticed if it is in a lit room, if it emits light, or if the player is actively carrying it.
def isNoticible(obj, player):
        if isLit(obj) or obj in player.inventory:
                return True
        else:
                return False

# Given a location, list the objects that are there.
def listObjectsAtLocation(location):
        children = location.children
        # if not empty
        if children:
                print(f"Around you, you see:")
                for child in children:
                        print(f"{child.description}")

# List the objects at the player's location, and exclude the player.
def listObjectsAtPlayer(player):
        children = player.location.children

        # if not empty
        if children:
                print(f"Around you, you see:")

                # if the only child is the player, there isn't anything to see.
                if len(children) == 1 and children[0] == player:
                        print("Nothing of interest.")

                for child in children:
                        if child != player:
                                if isNoticible(child, player):
                                        print(f"{child.description}")

def lookAround(noun, player):
        location = player.location
        if isLit(location):
                descr = location.description
                print(f"You are in {descr}.")
        else:
                print("It is very dark.")

        listObjectsAtPlayer(player)

def executeLook(noun, player):
        match noun:
                case "around":
                        lookAround(noun, player)
                case _:
                        print(f"You can't do that.")

# Get an item from the inventory with a matching tag
def getFromInventory(tag, player):
        inventory = player.inventory
        obj = None
        # check each item in the inventory
        for item in inventory:
                # if one of the tags in the list matches
                if tag in item.tags:
                        obj = item
        return obj


def executeGet(noun, player):
        # if the place we are trying to get from is lit
        if isLit(player.location):
                obj = getObject(noun, player.location)
                if obj:
                        if obj.weight != None:
                                if obj.weight < 100:
                                        print(f"You pick up {obj.description}")
                                        # add the object to the player's inventory
                                        player.inventory.append(obj)
                                        # remove the object from where it was before
                                        player.location.children.remove(obj)
                                        # set the object's location to be at the player
                                        obj.location = player
                        else:
                                print("That's not something you can get.")
                else:
                        print(f"You don't see {noun} here.")
        else:
                print("Its too dark to see.")

def inventory(player):
        for child in player.inventory:
                print(f"{child.description}")

def executeDrop(tag, player):
        obj = getFromInventory(tag, player)
        if obj:
                # remove object from player's inventory
                player.inventory.remove(obj)
                # att the object as a child of the current location
                player.location.children.append(obj)
                # set the object's location to be where it is dropped
                obj.location = player.location
                print(f"You drop {obj.description}")
        else:
                print("You aren't carrying that.")

def printHelp():
        print("Commands:\nquit\nlook <noun>\ngo <noun>\nexamine <noun>\nget <noun>\ndrop <noun>\ninventory")

def parseInput(text, player):
        words = text.split()
        verb = words[0]
        # TODO: handle player entering only one word
        noun = None
        if len(words) > 1:
                noun = words[1]

        '''
        Commands in the game:
        quit
        go
        look
        examine
        get
        drop
        inventory
        help

        talk (to A about B)
        put A in B
        eat
        wield
        unwield
        open?
        close?
        use?
        '''
        
        match verb:
                case "quit":
                        # quit the game
                        return False
                case "go":
                        # move in the specified direction
                        executeGo(noun, player)
                case "look":
                        # look at the noun, or in the direction of the noun
                        executeLook(noun, player)
                case "examine":
                        # examine something closely without interacting with it
                        executeExamine(noun, player.location)
                case "get":
                        # get a local item and put it in the player's inventory
                        executeGet(noun, player)
                case "drop":
                        # drop an item from the inventory at the current location
                        executeDrop(noun, player)
                case "inventory":
                        # show the player's inventory
                        inventory(player)
                case "help":
                        printHelp()
                case _:
                        print(f"You don't know how to '{verb}'")
        return True
