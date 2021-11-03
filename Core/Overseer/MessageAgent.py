from Core.GameElements.simpleClasses import Roster

animals = [
    "Nop",  # No action
    "Ant", "Beaver", "Beetle", "Bluebird", "Cricket", "Duck", "Fish", "Horse", "Ladybug", "Mosquito", "Otter",
    "Pig",  # Tier 1
    "Bat", "Crab", "Dodo", "Dog", "Dromedary", "Elephant", "Flamingo", "Hedgehog", "Peacock", "Rat", "Shrimp",
    "Spider", "Swan", "Tabby Cat",  # Tier 2
    "Badger", "Blowfish", "Camel", "Caterpillar", "Giraffe", "Hatching Chick", "Kangaroo", "Owl", "Ox", "Puppy",
    "Rabbit", "Sheep", "Snail", "Tropical Fish", "Turtle", "Whale",  # Tier 3
    "Bison", "Buffalo", "Deer", "Dolphin", "Hippo", "Llama", "Lobster", "Monkey", "Penguin", "Poodle", "Rooster",
    "Skunk", "Squirrel", "Worm",  # Tier 4
    "Chicken", "Cow", "Crocodile", "Eagle", "Goat", "Microbe", "Parrot", "Rhino", "Scorpion", "Seal", "Shark",
    "Turkey",  # Tier 5
    "Cat", "Dragon", "Fly", "Gorilla", "Leopard", "Mammoth", "Octopus", "Sauropod", "Snake", "Tiger",
    "Tyrannosaurus"  # Tier 6
]

equipment = [
    "Apple", "Honey",  # Tier 1
    "Cupcake", "Meat Bone", "Sleeping Pill",  # Tier 2
    "Garlic", "Salad Bowl",  # Tier 3
    "Canned Food", "Pear",  # Tier 4
    "Chili", "Chocolate", "Sushi",  # Tier 5
    "Melon", "Mushroom", "Pizza", "Steak"  # Tier 6
]

roster = Roster(5)


class MessageHandler:
    inShop = True

    def __init__(self):
        pass


if __name__ == '__main__':
    while True:
        print(animals[int(input("\nAnimal number: "))])
