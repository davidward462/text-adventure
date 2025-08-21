
# 'children' is a list of objects that are either representationally inside this node, or can be reached from it, or are a subsection of it.
# 'tags' is a list of strings that are used to identify the object.
# 'description' is a short description of the object the player can see.
# 'details' is text that the player sees if they examine the object closely.
# 'weight' relates to how easy an item is to pick up.
# 'destination' is only for passages, and is the place to where it leads.
# 'prospect' is the place to which the passage appears to go.
# 'health' is the number of hit points for entities
# 'goText' is text the player sees when passing through this passage.
class Node():
        def __init__(self, tags, description, details="You see nothing special.", weight=None, destination=None, prospect=None, health=None, goText=None):
                self.children = []
                self.tags = tags
                self.description = description
                self.details = details
                self.weight = weight
                self.destination = destination
                self.prospect = prospect
                self.health = health
                self.goText = goText

        def addChild(self, childNode):
                self.children.append(childNode)

        def addChildren(self, childrenList):
                for child in childrenList:
                        self.addChild(child)

        def makeEnterable(self):
                self.destination = self

class Player(Node):
        def __init__(self, tags, description, location, weight=None, destination=None, health=100):
                self.inventory = []
                self.location = location
                Node.__init__(self, tags, description, weight, destination, health)


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

# main loop
running = False
while running:
        text = input("\n-> ")
        running = parseInput(text, player)
