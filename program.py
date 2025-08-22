from node import Node, Player
import lib

root = Node(["root"], "")
house = Node(["house"], "a small wooden house", goText="You enter the house.")
house.makeEnterable()
player = Player(["player"], "a hero", location=house)
field = Node(["field"], "a grassy field")
door = Node(["door"], "a wooden door", destination=field, goText="You go through the door.")
basement = Node(["basement"], "a dimly-lit basement")
staircaseDown = Node(["stairs", "staircase", "down", "basement"], "a staircase leading down to the basement", destination=basement, goText="You descend the stairs.")
staircaseUp = Node(["stairs", "staircase", "up"], "a staircase leading up", destination=house, goText="You ascend the stairs.")
oldBook = Node(["book"], "an old book", weight=1)

root.addChildren([field, basement])
field.addChild(house)
house.addChildren([player, door, staircaseDown])
basement.addChildren([staircaseUp, oldBook])


lib.executeLook("around", player)

# main loop
running = True
while running:
        text = input("\n-> ")
        running = lib.parseInput(text, player)
