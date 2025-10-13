import lib

def go(passage, player):
        player.location.children.remove(player)
        player.location = passage.destination
        passage.destination.addChild(player)
        print(f"{passage.goText}")
        lookAround(player)
        # executeLook("around", player)

def executeGo(noun, player):

        obj = lib.getObject(noun, player.location)
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

# Give a description of the area and things around the player
def lookAround(player):
        location = player.location
        if lib.isLit(location):
                descr = location.description
                print(f"You are in {descr}.")
        else:
                print("It is very dark.")

        lib.listObjectsAtPlayer(player)

# Given a list of tags of 1 or more, look at some item.
# If there are more than 1 matching items, or none, tell this to the player.
def executeLook(tags, player):
        #obj = getObject(tags, player.location)
        objects = lib.getChildren(tags, player.location)

        if not objects:
                # TODO: make this print better
                print(f"You don't see '{tags}' here.")
        elif len(objects) > 1:
                print("Please be more specific about what you want to look at.")
        else:
                obj = objects[0]
                print(f"There is {obj.description} here.")


# Examine the given noun at the location provided
def executeExamine(noun, location):
        obj = lib.getObject(noun, location)
        if obj:
                print(f"{obj.details}")
        else:
                print(f"You don't see '{noun}' here.")

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
        if lib.isLit(player.location):
                obj = lib.getObject(noun, player.location)
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
        entity = lib.getObject(noun, player.location)
        entity.talk()


def executeTalkAbout(player, noun, topic):
        entity = lib.getObject(noun, player.location)
        entity.talkAbout(topic)

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

"""
rest: The part of the command after the first keyword.
player: The player object.
"""
def look(rest, player):
        # []
        # ['around']
        # ['noun']
        if not rest:
                # []
                lookAround(player)
        else:
                # there are some other words
                if rest[0] == "around":
                        lookAround(player)
                else:
                        # look at an object given some tags
                        executeLook(rest, player)
