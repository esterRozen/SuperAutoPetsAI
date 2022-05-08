from .BaseAgent import BaseAgent
from .Handlers.Items import Tier1, Tier2, Tier3, Tier4, Tier5, Tier6, Equipment


animals = [
    "Nop",  # No action

    "Ant", "Beaver", "Beetle", "Bluebird", "Cricket", "Duck", "Fish", "Horse", "Ladybug", "Mosquito", "Otter",
    "Pig",  # Tier 1

    "Bat", "Crab", "Dodo", "Dromedary", "Elephant", "Flamingo", "Hedgehog", "Peacock", "Rat", "Shrimp",
    "Spider", "Swan", "Tabby Cat",  # Tier 2

    "Badger", "Blowfish", "Camel", "Caterpillar", "Dog", "Giraffe", "Hatching Chick", "Kangaroo", "Owl", "Ox", "Puppy",
    "Rabbit", "Sheep", "Snail", "Tropical Fish", "Turtle",  # Tier 3

    "Bison", "Buffalo", "Deer", "Dolphin", "Hippo", "Llama", "Lobster", "Microbe", "Parrot", "Penguin",
    "Rooster", "Skunk", "Squirrel", "Whale", "Worm",  # Tier 4

    "Chicken", "Cow", "Crocodile", "Eagle", "Goat", "Monkey", "Poodle", "Rhino", "Scorpion", "Seal", "Shark",
    "Turkey",  # Tier 5

    "Boar", "Cat", "Dragon", "Fly", "Gorilla", "Leopard", "Mammoth", "Octopus", "Sauropod", "Snake", "Tiger",
    "Tyrannosaurus"  # Tier 6
    
    "Butterfly", "Bus", "DirtyRat", "FlyFriend", "Ram", "ZombieCricket"
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
class MessageAgent(BaseAgent):
    def __init__(self, mode):
        super(MessageAgent, self).__init__(mode)

        # event handling matrix
        t1 = Tier1()
        t2 = Tier2()
        t3 = Tier3()
        t4 = Tier4()
        t5 = Tier5()
        t6 = Tier6()
        eq = Equipment()

        self.func = [t1.nop,
                     t1.ant, t1.beaver, t1.beetle, t1.bluebird, t1.cricket, t1.duck, t1.fish,
                     t1.horse, t1.ladybug, t1.mosquito, t1.otter, t1.pig,

                     t2.bat, t2.crab, t2.dodo, t2.dromedary, t2.elephant, t2.flamingo,
                     t2.hedgehog, t2.peacock, t2.rat, t2.shrimp, t2.spider, t2.swan, t2.tabby_cat,

                     t3.badger, t3.blowfish, t3.camel, t3.caterpillar, t3.dog, t3.giraffe,
                     t3.hatching_chick, t3.kangaroo, t3.owl, t3.ox, t3.puppy, t3.rabbit,
                     t3.sheep, t3.snail, t3.tropical_fish, t3.turtle,

                     t4.bison, t4.buffalo, t4.deer, t4.dolphin, t4.hippo, t4.llama, t4.lobster,
                     t4.penguin, t4.poodle, t4.rooster, t4.skunk, t4.squirrel, t4.whale,
                     t4.worm,

                     t5.chicken, t5.cow, t5.crocodile, t5.eagle, t5.goat, t5.microbe, t5.monkey,
                     t5.parrot, t5.rhino, t5.scorpion, t5.seal, t5.shark, t5.turkey,

                     t6.boar, t6.cat, t6.dragon, t6.fly, t6.gorilla, t6.leopard, t6.mammoth,
                     t6.octopus, t6.sauropod, t6.snake, t6.tiger, t6.tyrannosaurus

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

    # message contains unit_id which sent it
    def handle_message(self, message):
        # trigger function that manipulates roster
        self.func[message](self)

    # assume event which triggered event handler has already resolved!!!
    # e.g. if animal sold, then it is no longer in the roster and gold
    # incremented already
    # also assume that self.lvl is the level of the unit whose ability triggered
    # done for convenience, otherwise it's a pain...


if __name__ == '__main__':
    while True:
        a = MessageAgent("base")
        print(animals[int(input("\nAnimal number: "))])
