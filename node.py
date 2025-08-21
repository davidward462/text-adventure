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
