# 'children' is a list of objects that are either representationally inside this node, or can be reached from it, or are a subsection of it.
# 'inventory' is a list of objects contained by this object.
# 'tags' is a list of strings that are used to identify the object.
# 'description' is a short description of the object the player can see.
# 'location' is a pointer to the parent of this object.
# 'details' is text that the player sees if they examine the object closely.
# 'weight' relates to how easy an item is to pick up.
# 'destination' is only for passages, and is the place to where it leads.
# 'prospect' is the place to which the passage appears to go.
# 'health' is the number of hit points for entities
# 'goText' for a location that you enter directly, describes entering the location. For a passage it describes moving through the passage.
# 'closed' means a passage is locked, blocked, or otherwise not passable at this time.
# 'key' is a pointer to the specific object that the player needs in order to open a passage (it does not need to be called a key)
# 'light' indicates if an object is glowing or is otherwise lit by it's own nature (like natural light). By default things are not lit.
# 'response is data for entities when the player talks to them. None means the player cannot talk to this node (like a rock). An entity may have a single string as a generic response to all conversation (like a cat who always says "meow"), or a separate data structure may be used (TODO: set this up. Maybe a dict) to hold answers about certain words.
class Node():
        def __init__(self, tags, description, location=None, details="You see nothing special.", weight=None, destination=None, prospect=None, health=None, goText=None, closed=False, key=None, light=False, response=None):
                self.children = []
                self.inventory = []
                self.tags = tags
                self.description = description
                self.location = location
                self.details = details
                self.weight = weight
                self.destination = destination
                self.prospect = prospect
                self.health = health
                self.goText = goText
                self.closed = closed
                self.key = key
                self.light = light
                self.response = response

        def addChild(self, childNode):
                childNode.location = self
                self.children.append(childNode)

        def addChildren(self, childrenList):
                for child in childrenList:
                        child.location = self
                        self.addChild(child)

        def makeEnterable(self):
                self.destination = self

        # Returns true of the key opens the passage (and does open the passage), false otherwise.
        def tryOpen(self, keyProvided):
                if keyProvided == self.key:
                        self.closed = False
                        return True
                else:
                        return False

        def destinatinIsLit(self):
                # if the object has a destination (it is a passage)
                if self.destination:
                        if self.destination.light:
                                return True
                return False
