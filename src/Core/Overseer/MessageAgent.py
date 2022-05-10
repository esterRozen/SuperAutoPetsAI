from typing import TypeAlias, List, Callable
from .BaseAgent import BaseAgent
from .Handlers.Items import Tier1, Tier2, Tier3, Tier4, Tier5, Tier6, Equipment
from .Handlers.eventprocessor import EventProcessor


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

Animal: TypeAlias = Callable[['MessageAgent'], None]


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
        self.__EP = EventProcessor()

        # THIS DICTATES UNIT IDS. DO NOT MESS WITH ORDER
        self.func: List[Animal] = [t1.nop,
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

                                   # zombie_cricket, dirty_rat, butterfly, ram, honey, mushroom
                                   ]

    @property
    def sorted_team(self):
        # for unit in roster sorted by descending attack, then increasing index
        units_sorted = sorted(
                self.team.animals,
                key=lambda animal: (-1*animal.atk, self.team.animals.index(animal)),
                reverse=False)
        return units_sorted

    @property
    def sorted_without_raiser(self):
        sorted_team = self.sorted_team
        if self.event_raiser[0] == "team":
            sorted_team.remove(self.team.animals[self.event_raiser[1]])
        return sorted_team

    @property
    def sorted_without_target(self):
        sorted_team = self.sorted_team
        if self.target[0] == "team":
            sorted_team.remove(self.team.animals[self.target[1]])
        return sorted_team

    def handle_event(self, message, event_raiser, target=None):
        # set variables
        self.event_raiser = event_raiser
        if target is not None:
            self.target = target

        # route to trigger processor, it will figure out which units to have
        # handle messages.
        if message == "buy":
            self.__EP.buy(self)
        elif message == "buy food":
            self.__EP.buy_food(self)
        elif message == "buy t1 pet":
            self.__EP.buy_T1_pet(self)
        elif message == "eat food":
            self.__EP.eat_food(self)
        elif message == "start turn":
            self.__EP.start_turn(self)
        elif message == "sell":
            self.__EP.sell(self)
        elif message == "end turn":
            self.__EP.end_turn(self)
        elif message == "friend bought":
            self.__EP.friend_bought(self)
        elif message == "friend eats food":
            self.__EP.friend_eats_food(self)
        elif message == "friend sold":
            self.__EP.friend_sold(self)
        elif message == "friend summoned (shop)":
            self.__EP.friend_summoned_shop(self)
        elif message == "friend faints":
            self.__EP.friend_faints(self)
        elif message == "on level":
            self.__EP.on_level(self)
        elif message == "friend ahead faints":
            self.__EP.friend_ahead_faints(self)
        elif message == "hurt":
            self.__EP.hurt(self)
        elif message == "start battle":
            self.__EP.start_battle(self)
        elif message == "before attack":
            self.__EP.before_attack(self)
        elif message == "friend summoned (battle)":
            self.__EP.friend_summoned_battle(self)
        elif message == "knock out":
            self.__EP.knock_out(self)

            # sending messages like buy, sell, move, combine, start turn, end turn,
        # start turn, reroll, freeze/unfreeze, hurt, faint, knock out, attacks,
        # before attack, unit ahead attacks, unit ahead faints, friend summoned
        return

    # message contains unit_id which sent it
    def trigger_ability(self, message):
        # trigger function that manipulates roster
        # does not return anything
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
