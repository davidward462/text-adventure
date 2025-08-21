from node import Node, Player
import lib

root = Node(["root"], "")
house = Node(["house"], "a small wooden house")
player = Player(["player"], "a hero", location=house)
field = Node(["field"], "a grassy field")
door = Node(["door"], "a wooden door", destination=field)

root.addChild(field)
field.addChild(house)
house.addChildren([player, door])

# main loop
running = True
while running:
        text = input("\n-> ")
        running = lib.parseInput(text, player)
