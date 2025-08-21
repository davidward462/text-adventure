
# Base node class
class Node():
        def __init__(self, name, description, weight=None, destination=None, health=None):
                self.children = []
                self.name = name
                self.description = description
                self.weight = weight                    # for items
                self.destination = destination          # for passages
                self.health = health                    # for entities

        def addChild(self, childNode):
                self.children.append(childNode)

        def addChildren(self, childrenList):
                for child in childrenList:
                        self.addChild(child)

        def makeEnterable(self):
                self.destination = self


class Player(Node):
        def __init__(self, name, description, location, weight=None, destination=None, health=100):
                self.inventory = []
                self.location = location
                Node.__init__(self, name, description, weight, destination, health)


# return the object specified by the name, in the node. Return None if it is not found.
def getObject(name, node):
        children = node.children
        obj = None
        for child in children:
                if child.name == name:
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
        namesList = [child.name for child in children]
        # if not empty
        if namesList:
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
                        print(f"I don't know how to do '{verb}'")
        return True

# Player <- (name="name", description="descr", location=loc)
# Location <- (name="name", description="descr")
# Passage <- (name="name", description="descr", destination=dest)

root = Node("world", "the game world")
field = Node("field", "a grassy field")
player = Player("player", "a hero", field)
cow = Node("cow", "a brown cow")
tree = Node("tree", "a birch tree")
cave = Node("cave", "a small cave")
cave.makeEnterable()
caveExit = Node("exit", "an exit from the cave", destination=field)
house = Node("house", "a blue house")
house.makeEnterable()
bed = Node("bed", "a ragged bed")
stove = Node("stove", "an old, cast-iron stove")
door = Node("door", "a wooden door", destination=field)

root.addChild(field)
field.addChildren([cow, tree, house, cave, player])
house.addChildren([bed, stove, door])
cave.addChild(caveExit)

# main loop
running = True
executeLook("around", player)
while running:
        text = input("-> ")
        running = parseInput(text, player)
