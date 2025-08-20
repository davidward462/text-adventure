
# Base node class
class Node():
        def __init__(self):
                self.children = []

        def addChild(self, childNode):
                self.children.append(childNode)

        def getChildren(self):
                return self.children

class EmptyNode(Node):
        pass

class WorldObject(Node):
        def __init__(self, name, description, weight=None, destination=None, health=None):
                self.name = name
                self.description = description
                self.weight = weight                    # for items
                self.destination = destination          # for passages
                self.health = health                    # for entities

                # here an ancestor's __init__ function is called directly, without using the super() method, for simplicity.
                Node.__init__(self)

class Player(WorldObject):
        def __init__(self, name, description, location, weight=None, destination=None, health=100):
                self.inventory = []
                self.location = location
                WorldObject.__init__(self, name, description, weight, destination, health)


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
                # TODO: don't move to a location that's not a place. Also move through a passage correctly.
                player.location = obj
        else:
                print(f"That place doesn't exist here.")


def executeExamine(noun, player):
        obj = getObject(noun, player.location)
        if obj:
                print(f"There is a {obj.description} here.")
        else:
                print(f"You don't see {noun} here.")


def executeLook(noun, player):
        match noun:
                case "around":
                        output = player.location.description
                        print(f"You are in {output}.")
                        children = player.location.children
                        namesList = [child.name for child in children]
                        print(f"Around you, you see {namesList}")
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


root = EmptyNode()

hill = WorldObject("hill", "a grassy hill")
coin = WorldObject("coin", "a gold coin", 0)
cow = WorldObject("cow", "a brown cow", 100)
house = WorldObject("house", "a red house")
player = Player("player", "main character", hill)
door = WorldObject("door", "a wooden door", hill)

hill.addChild(cow)
hill.addChild(house)

# should the player actually be in the world tree?
hill.addChild(player)
house.addChild(coin)
house.addChild(door)


root.addChild(hill)


# main loop
running = True
while running:
        text = input()
        running = parseInput(text, player)
