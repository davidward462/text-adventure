from node import Node
import lib

root = Node(["root"], "")
brassKey = Node(["key"], "a brass key", weight=0)
house = Node(["house"], "a small wooden house", goText="You enter the house.", key=brassKey, closed=True, light=True)
house.makeEnterable()
field = Node(["field"], "a grassy field", light=True)
player = Node(["player"], "a hero", location=field, health=100)
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

root.addChildren([field, basement, flowerField])
field.addChildren([house, cobblestoneRoadToFlowers, brassKey, player])
flowerField.addChildren([cobblestoneRoadToField])
house.addChildren([player, door, staircaseDown, copperCoin])
basement.addChildren([staircaseUp, oldBook])


lib.executeLook("around", player)

# main loop
running = True
while running:
        text = input("\n-> ")
        running = lib.parseInput(text, player)
