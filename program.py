from node import Node
import lib

root = Node(["root"], "")
brassKey = Node(["key"], "a brass key", weight=0)
house = Node(["house, east"], "a small wooden house", goText="You enter the house.", key=brassKey, closed=True, light=True)
house.makeEnterable()
field = Node(["field"], "a grassy field", light=True)
player = Node(["player"], "", health=100)
door = Node(["door"], "a wooden door", destination=field, goText="You go through the door.")
basement = Node(["basement"], "a dusty basement")
staircaseDown = Node(["stairs", "staircase", "down", "basement"], "a staircase leading down to the basement", destination=basement, goText="You descend the stairs.")
staircaseUp = Node(["stairs", "staircase", "up"], "a staircase leading up", destination=house, goText="You ascend the stairs.")
oldBook = Node(["book"], "an old book", weight=1)
flowerField = Node(["flowers", "field"], "a field of flowers", light=True)
flowerField.makeEnterable()
cobblestoneRoadToFlowers = Node(["road"], "a cobblestone road", destination=flowerField, goText="You walk down the road.")
cobblestoneRoadToField = Node(["road"], "a cobblestone road", destination=field, goText="You walk down the road.")
copperCoin = Node(["coin", "copper"], "a copper coin", weight=1)
goldCoin = Node(["coin", "gold"], "a gold coin", weight=1)
gnomeResponses = {
        "coin":"Worth something, I think.",
        "house":"It's not me who lives there!",
        "field":"It's nice here.",
        "door":"Looks fine to me.",
        "default":"I'm not familiar with that."
}
gnome0 = Node(['gnome'], "a little gnome", weight=10, health=1, expression="Oh, hello.", responses=gnomeResponses)

ghostResponses = {
        "coin":"all is moth-eaten...",
        "book":"I can't remember...",
        "default":"..."
}
ghost = Node(['ghost'], "a sad ghost", weight=0, health=1000, expression="sigh...", responses=ghostResponses)

root.addChildren([field, basement, flowerField])
field.addChildren([house, cobblestoneRoadToFlowers, brassKey, player, gnome0])
flowerField.addChildren([cobblestoneRoadToField])
house.addChildren([door, staircaseDown, copperCoin, ghost, goldCoin])
basement.addChildren([staircaseUp, oldBook])

# main loop
running = True
userName = input("Enter your name: ")
player.description = userName

lib.lookAround(player)
while running:
        text = input("\n-> ")
        running = lib.parseInput(text, player)
