from Core.Overseer.Handlers import *


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


# noinspection DuplicatedCode
class MessageAgent(Equipment, Tier1, Tier2, Tier3, Tier4, Tier5, Tier6):
    def __init__(self, mode):
        super(MessageAgent, self).__init__(mode)

        # event handling matrix
        self.func = [self._nop,
                     self._ant, self._beaver, self._beetle, self._bluebird, self._cricket, self._duck, self._fish,
                     self._fish, self._horse, self._ladybug, self._mosquito, self._otter, self._pig,
                     self._bat, self._crab, self._dodo, self._dog, self._dromedary, self._elephant, self._flamingo,
                     self._hedgehog, self._peacock, self._rat, self._shrimp, self._spider, self._swan, self._tabby_cat,
                     self._badger, self._blowfish, self._camel, self._caterpillar, self._giraffe, self._hatching_chick,
                     self._kangaroo, self._owl, self._ox, self._puppy, self._rabbit, self._sheep, self._snail,
                     self._tropical_fish, self._turtle, self._whale,
                     self._bison, self._buffalo, self._deer, self._dolphin, self._hippo, self._llama, self._lobster,
                     self._monkey, self._penguin, self._poodle, self._rooster, self._skunk, self._squirrel, self._worm,
                     self._chicken, self._cow, self._crocodile, self._eagle, self._goat, self._microbe, self._parrot,
                     self._rhino, self._scorpion, self._seal, self._shark, self._turkey,
                     self._cat, self._dragon, self._fly, self._gorilla, self._leopard, self._mammoth, self._octopus,
                     self._sauropod, self._snake, self._tiger, self._tyrannosaurus
                     # self._zombie_cricket, self.dirty_rat, self.butterfly, self.honey, self
                     ]

    def load(self, team, turn, gold=10, shop=None, hearts=4, battle_lost=False):
        # re-enter the shop from a given game state
        # used for simulation/replay
        pass

    def trigger_message(self, message):
        # for unit in roster sorted by descending attack, then descending
        # hp, send message, handle response
        # sending messages like buy, sell, move, combine, start turn, end turn,
        # start turn, reroll, freeze/unfreeze, hurt, faint, knock out, attacks,
        # before attack, unit ahead attacks, unit ahead faints, friend summoned
        pass

    # make a new layer of handlers that deals with battle???

    def handle_message(self, message):
        # trigger function that manipulates roster
        self.lvl = self.team.level()
        self.func[message]()

    # assume event which triggered event handler has already resolved!!!
    # e.g. if animal sold, then it is no longer in the roster and gold
    # incremented already
    # also assume that self.lvl is the level of the unit whose ability triggered
    # done for convenience, otherwise it's a pain...


if __name__ == '__main__':
    while True:
        a = MessageAgent("base")
        print(animals[int(input("\nAnimal number: "))])
