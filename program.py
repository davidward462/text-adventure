
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
        def __init__(self, name, description):
                self.name = name
                self.description = description
                # here an ancestor's __init__ function is called directly, without using the super() method, for simplicity.
                Node.__init__(self)

class Item(WorldObject):
        def __init__(self, name, description, weight):
                self.weight = weight
                WorldObject.__init__(self, name, description)

class Location(WorldObject):
        pass

# The passage is a doorway or path which leads from its location to the specified destination.
class Passage(WorldObject):
        def __init__(self, destination):
                self.destination = destination
                WorldObject.__init__(self, name, description)

class Entity(WorldObject):
        def __init__(self, name, description, health):
                self.health = health
                WorldObject.__init__(self, name, description)


class Player(Entity):
        def __init__(self, name, description, health, location):
                self.location = location
                Entity.__init__(self, name, description, health)



# return the object specified by the name, in the node. Return None if it is not found.
def getObject(name, node):
        children = node.children
        obj = None
        for child in children:
                if child.name == name:
                        obj = child
        return obj

def executeGo(noun, player):

        # TODO: use getObject() here
        children = player.location.children
        found = False
        destination = None
        for child in children:
                if child.name == noun:
                        found = True
                        destination = child
        if not found:
                print(f"That place doesn't exist here.")

        # TODO: don't move to a location that's not a place
        player.location = destination

def executeExamine(noun, player):
        # TODO: use getObject()
        children = player.location.children
        found = False
        for child in children:
                if child.name == noun:
                        found = True
                        print(f"You see {child.description}.")

        if not found:
                print(f"You don't see {noun} here.")

        pass

def executeLook(noun, player):
        #print(f"execute {noun}")
        match noun:
                case "around":
                        # TODO: use getObject()
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

hill = Location("hill", "a grassy hill")
coin = Item("coin", "a gold coin", 0)
cow = Entity("cow", "a brown cow", 100)
house = Location("house", "a red house")
player = Player("player", "main character", 100, hill)

hill.addChild(cow)
hill.addChild(house)

# should the player actually be in the world tree?
hill.addChild(player)
house.addChild(coin)


root.addChild(hill)


# main loop
running = True
while running:
        text = input()
        running = parseInput(text, player)
