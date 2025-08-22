
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

def executeGo(noun, player):

        obj = getObject(noun, player.location)
        if obj:
                # if object has a destination, go there
                if obj.destination:
                        player.location.children.remove(player)
                        player.location = obj.destination
                        obj.destination.addChild(player)
                        # go message
                        print(f"{obj.goText}")
                        executeLook("around", player)
                else:
                        print("You can't go there.")

        else:
                print(f"That place doesn't exist here.")


def executeExamine(noun, player):
        obj = getObject(noun, player.location)
        if obj:
                print(f"There is {obj.description} here.")
        else:
                print(f"You don't see {noun} here.")


# Given a location, list the objects that are there.
def listObjectsAtLocation(location):
        children = location.children
        # if not empty
        if children:
                print(f"Around you, you see:")
                for child in children:
                        print(f"{child.description}")


def executeLook(noun, player):
        match noun:
                case "around":
                        output = player.location.description
                        print(f"You are in {output}.")
                        listObjectsAtLocation(player.location)
                case _:
                        print(f"You can't do that.")


def parseInput(text, player):
        words = text.split()
        verb = words[0]
        # TODO: handle player entering only one word
        noun = None
        if len(words) > 1:
                noun = words[1]

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
                        executeExamine(noun, player)
                case _:
                        print(f"You don't know how to do '{verb}'")
        return True
