import commands

# return the object specified by the tags, in the node. Return None if it is not found.
# TODO: Handle the case where multiple children have matching tags.
def getObject(tag, node):
        children = node.children
        obj = None
        objList = []
        # check each child of the node
        for child in children:
                # if one of the tags in the list matches
                if tag in child.tags:
                        obj = child
                        objList.append(child)
        for o in objList:
                print(f"\t{o.description}")
        return obj

# TODO: Write the below functions.

def printObjectList(objectList):
        if objectList:
                for obj in objectList:
                        print(obj)
        else:
                print("List is empty")

# Return a list of children of the current node where 'tags' is a subset of the child's tags.
# Return None if nothing is found.
def getChildren(tags, node):
        #print(f"tags: {tags}")
        children = node.children
        objects = []
        obj = None

        # check each child
        for child in children:
                # the child is a match if the tags to search for are a subset of the child's tags.
                #print(f"tags: {tags} ? child tags: {child.tags}")
                tagsMatch = set(tags).issubset(set(child.tags))


                # if the given tags are a subset of the child's tags (or equal)
                if tagsMatch:
                        # append child to the list of objects that match
                        objects.append(child)

        if not objects:
                # if no objects were found with matching tags, return None
                return None
        else:
                # otherwise, return the list of found objects
                #printObjectList(objects)
                return objects

# Check all the descendants of the given node (traverse the tree). Return the first node where 'tag' matches at least one of
# its tags. Return None if nothing is found.
def getDescendant(tag, node):
        pass


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


# New parse function.
# TODO: Figure out a way to parse and execute multiword commands, empty commands, etc.
def parse(text,player):
        # Split the text into a list of strings.
        words = []
        words = text.split()
        #print(f"words: {words}")

        first = ""
        rest = ""

        first = words[0]
        rest = words[1::]
        #print(f"first: {first}\nrest: {rest}")

        match first:
                case "quit":
                        return False
                case "help":
                        commands.executeHelp()
                case "look":
                        #print("case: look")
                        commands.look(rest, player)
                case ["get"]:
                        pass
                case ["examine"]:
                        pass
                case ["wait"]:
                        pass
                case ["go"]:
                        pass
                case ["drop"]:
                        pass
                case ["talk"]:
                        pass
                case ["give"]:
                        pass
                case ["ask"]:
                        pass
                case ["eat"]:
                        pass
                case ["lock"]:
                        pass
                case ["unlock"]:
                        pass
                case ["inventory"]:
                        pass
                case ["hit"]:
                        pass
                case ["wield"]:
                        pass
                case ["unwield"]:
                        pass
                case ["open"]:
                        pass
                case ["close"]:
                        pass
                case ["wear"]:
                        pass
                case ["remove"]:
                        pass
                case ["attack"]:
                        pass
        return True

def parseInput(text, player):
        # Split input into a list, and match the different cases for the commands.
        # TODO: Patterns are only matched exactly. A command like "help me" would cause the default case to execute.
        words = text.split()
        #print(f"words: {words}")
        match words:
                case ["quit"]:
                        return False
                case ["quit", "game"]:
                        return False
                case ["help"]:
                        commands.executeHelp()
                case ["look"]:
                        # executeLook("around", player)
                        commands.lookAround(player)
                case ["look", "around"]:
                        # executeLook("around", player)
                        commands.lookAround(player)
                case ["look", A]:
                        commands.executeLook(A, player)
                case ["look", "at", A]:
                        commands.executeLook(A, player)
                case ["look", "inventory"]:
                        commands.inventory(player)
                case ["get", A]:
                        print(f"executeGet({A})")
                        commands.executeGet(A, player)
                case ["get", A, "from", B]:
                        print(f"You can't get {A} from {B} right now.")
                case ["examine", A]:
                        commands.executeExamine(A, player.location)
                case ["go", A]:
                        commands.executeGo(A, player)
                case ["go", "to", A]:
                        commands.executeGo(A, player)
                case ["give", A]:
                        print(f"You can't give {A} right now.")
                case ["give", A, "to", B]:
                        print(f"You can't give {A} to {B} right now.")
                case ["drop", A]:
                        commands.executeDrop(A, player)
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
                        commands.inventory(player)
                case ["hit", A]:
                        print(f"You can't hit {A} right now.")
                case ["wield", A]:
                        print(f"You can't wield {A} right now.")
                case ["unwield", A]:
                        print(f"You can't unwield {A} right now.")
                case ["eat", A]:
                        print(f"You can't eat {A} right now.")
                case ["talk", A]:
                        commands.executeTalk(player, A)
                case ["talk", A, "about", B]:
                        commands.executeTalkAbout(player, A, B)
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
                        print(f"{words}")
                        print("I don't know how to do that.")
        return True
