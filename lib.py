
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

def executeTalk(player, noun):
        obj = getObject(noun, player.location)
        if obj:
                if obj.response:
                        # if there is a response
                        print(f"{obj.description} says: \"{obj.response}\"")
                else:
                        print("It doesn't say anything.")
        else:
                print(f"You don't see {noun} here.")
                

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

def executeHelp():
        print("Commands:\nquit\nquit game\nlook\nlook around\nlook A\nlook at A\nlook inventory\nget A\nget A from B\nexamine A\ngo A\ngo to A\ngive A\ngive A to B\ndrop A\nask A\nask A from B\nopen A\nclose A\nlock A\nunlock A\ninventory\nhit A\nwield A\nunwield A\neat A\ntalk A\ntalk A about B\nwear A\ntake off A\nattack A\nattack A with B\nwait\n")

def parseInput(text, player):

        # Split input into a list, and match the different cases for the commands.
        # TODO: Patterns are only matched exactly. A command like "help me" would cause the default case to execute.
        words = text.split()
        match words:
                case ["quit"]:
                        return False
                case ["quit", "game"]:
                        return False
                case ["help"]:
                        executeHelp()
                case ["look"]:
                        executeLook("around", player)
                case ["look", "around"]:
                        executeLook("around", player)
                case ["look", A]:
                        executeLook(A, player)
                case ["look", "at", A]:
                        executeLook(A, player)
                case ["look", "inventory"]:
                        inventory(player)
                case ["get", A]:
                        executeGet(A, player)
                case ["get", A, "from", B]:
                        print(f"You can't get {A} from {B} right now.")
                case ["examine", A]:
                        executeExamine(A, player.location)
                case ["go", A]:
                        executeGo(A, player)
                case ["go", "to", A]:
                        executeGo(A, player)
                case ["give", A]:
                        print(f"You can't give {A} right now.")
                case ["give", A, "to", B]:
                        print(f"You can't give {A} to {B} right now.")
                case ["drop", A]:
                        executeDrop(A, player)
                case ["ask", A]:
                        print(f"You can't ask {A} right now.")
                case ["ask", A, "for", B]:
                        print(f"You can't ask {A} for {B} right now.")
                case ["open", A]:
                        print(f"You can't open {A} right now.")
                case ["close", A]:
                        print(f"You can't close {A} right now.")
                case ["lock", A]:
                        print(f"You can't lock {A} right now.")
                case ["unlock", A]:
                        print(f"You can't unlock {A} right now.")
                case ["inventory", A]:
                        inventory(player)
                case ["hit", A]:
                        print(f"You can't hit {A} right now.")
                case ["wield", A]:
                        print(f"You can't wield {A} right now.")
                case ["unwield", A]:
                        print(f"You can't unwield {A} right now.")
                case ["eat", A]:
                        print(f"You can't eat {A} right now.")
                case ["talk", A]:
                        executeTalk(player, A)
                        #print(f"You can't talk to {A} right now.")
                case ["talk", A, "about", B]:
                        print(f"You can't talk to {A} about {B} right now.")
                case ["wear", A]:
                        print(f"You can't wear {A} right now.")
                case ["remove", A]:
                        print(f"You can't remove {A} right now.")
                case ["attack", A]:
                        print(f"You can't attack {A} right now.")
                case ["attack", A, "with", B]:
                        print(f"You can't attack {A} with {B} right now.")
                case ["wait"]:
                        print("You wait.")
                case _:
                        print("I don't know how to do that.")
        return True

