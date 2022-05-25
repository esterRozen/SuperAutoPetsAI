import itertools
from typing import List, Callable

from .state import State
from .baseagent import BaseAgent
from .handlers.object_effects import Tier1, Tier2, Tier3, Tier4, Tier5, Tier6, Equipment
from .handlers.eventprocessor import EventProcessor
from ..eventnames import *

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
        self.__EP = EventProcessor()

        # THIS DICTATES UNIT IDS. DO NOT MESS WITH ORDER
        self.func: List[
            Callable[['MessageAgent'], None]] \
            = [t1.nop,

               t1.ant, t1.beaver, t1.beetle, t1.bluebird, t1.cricket,
               t1.duck, t1.fish,
               t1.horse, t1.ladybug, t1.mosquito, t1.otter, t1.pig,

               t2.bat, t2.crab, t2.dodo, t2.dromedary, t2.elephant,
               t2.flamingo,
               t2.hedgehog, t2.peacock, t2.rat, t2.shrimp, t2.spider,
               t2.swan, t2.tabby_cat,

               t3.badger, t3.blowfish, t3.camel, t3.caterpillar, t3.dog,
               t3.giraffe,
               t3.hatching_chick, t3.kangaroo, t3.owl, t3.ox, t3.puppy,
               t3.rabbit,
               t3.sheep, t3.snail, t3.tropical_fish, t3.turtle,

               t4.bison, t4.buffalo, t4.deer, t4.dolphin, t4.hippo,
               t4.llama, t4.lobster,
               t4.penguin, t4.poodle, t4.rooster, t4.skunk, t4.squirrel,
               t4.whale,
               t4.worm,

               t5.chicken, t5.cow, t5.crocodile, t5.eagle, t5.goat,
               t5.microbe, t5.monkey,
               t5.parrot, t5.rhino, t5.scorpion, t5.seal, t5.shark,
               t5.turkey,

               t6.boar, t6.cat, t6.dragon, t6.fly, t6.gorilla, t6.leopard,
               t6.mammoth,
               t6.octopus, t6.sauropod, t6.snake, t6.tiger,
               t6.tyrannosaurus

               # zombie_cricket, dirty_rat, butterfly, ram, honey,
               # mushroom
               ]

    @property
    def sorted_team(self, team=None):
        # for unit in roster sorted by descending attack, then increasing index
        if team == "team" or self.event_raiser[0] == "team":
            roster = self.team.animals
        elif team == "enemy" or self.event_raiser[0] == "enemy":
            roster = self.enemy.animals
        elif team == "both":
            # interleaved units to maintain left/right ordering for enemies and friendlies
            roster = list(itertools.chain(*zip(self.team.animals, self.enemy.animals)))
        else:
            raise ValueError(f"self.event_raiser should not contain {self.event_raiser[0]}")
        units_sorted = sorted(
                roster,
                key=lambda animal: (-1 * animal.atk, roster.index(animal)),
                reverse=False)
        return units_sorted

    @property
    def sorted_without_raiser(self):
        sorted_team = self.sorted_team
        if self.event_raiser[0] == "team":
            sorted_team.remove(self.team.animals[self.event_raiser[1]])
            return sorted_team
        elif self.event_raiser[0] == "enemy":
            sorted_team.remove(self.enemy.animals[self.event_raiser[1]])
            return sorted_team
        raise ValueError(f"self.event_raiser should not contain {self.event_raiser[0]}")

    @property
    def sorted_without_target(self):
        sorted_team = self.sorted_team
        if self.target[0] == "team":
            sorted_team.remove(self.team.animals[self.target[1]])
            return sorted_team
        elif self.target[0] == "enemy":
            sorted_team.remove(self.enemy.animals[self.target[1]])
            return sorted_team
        raise ValueError(f"self.target should not contain {self.target[0]}")

    @property
    def sorted_units_behind_raiser(self):
        sorted_team = self.sorted_team
        if self.event_raiser[0] == "team":
            out = []
            for animal in range(sorted_team):
                if self.team.animals.index(animal) < self.event_raiser[1]:
                    out += [animal]
            return out
        elif self.event_raiser[0] == "enemy":
            out = []
            for animal in range(sorted_team):
                if self.enemy.animals.index(animal) < self.event_raiser[1]:
                    out += [animal]
            return out
        raise ValueError(f"self.event_raiser should not contain {self.event_raiser[0]}")

    @staticmethod
    def load(state: State) -> 'BaseAgent':
        agent = MessageAgent(state.mode)
        agent.team = state.team
        agent.turn = state.turn
        agent.gold = state.gold
        agent.life = state.life
        agent.battle_lost = state.battle_lost
        if state.shop is not None:
            agent.shop = state.shop
        return agent

    def handle_event(self, message, event_raiser=None, target=None):
        # set variables
        if self.event_raiser is not None:
            self.event_raiser = event_raiser
        if target is not None:
            self.target = target

        # handle event
        if message == BEFORE_ATTACK:
            self.__EP.before_attack(self)
        elif message == BUY:
            self.__EP.buy(self)
        elif message == BUY_FOOD:
            self.__EP.buy_food(self)
        elif message == BUY_T1_PET:
            self.__EP.buy_t1_pet(self)
        elif message == EAT_FOOD:
            self.__EP.eat_food(self)
        elif message == ENEMY_ATTACKS:
            self.__EP.enemy_attacks(self)
        elif message == END_TURN:
            self.__EP.end_turn(self)
        elif message == FRIEND_AHEAD_ATTACKS:
            self.__EP.friend_ahead_attacks(self)
        elif message == FRIEND_AHEAD_FAINTS:
            self.__EP.friend_ahead_faints(self)
        elif message == FRIEND_BOUGHT:
            self.__EP.friend_bought(self)
        elif message == FRIEND_EATS_FOOD:
            self.__EP.friend_eats_food(self)
        elif message == FRIEND_FAINTS:
            self.__EP.friend_faints(self)
        elif message == FRIEND_SOLD:
            self.__EP.friend_sold(self)
        elif message == FRIEND_SUMMONED_BATTLE:
            self.__EP.friend_summoned_battle(self)
        elif message == FRIEND_SUMMONED_SHOP:
            self.__EP.friend_summoned_shop(self)
        elif message == HURT:
            self.__EP.hurt(self)
        elif message == IS_SUMMONED:
            self.__EP.is_summoned(self)
        elif message == KNOCK_OUT:
            self.__EP.knock_out(self)
        elif message == ON_FAINT:
            self.__EP.on_faint(self)
        elif message == ON_LEVEL:
            self.__EP.on_level(self)
        elif message == SELL:
            self.__EP.sell(self)
        elif message == START_BATTLE:
            self.__EP.start_battle(self)
        elif message == START_TURN:
            self.__EP.start_turn(self)

            # sending messages like buy, sell, move, combine, start turn, end turn,

        # route to trigger processor, it will figure out which units to have
        # handle messages.
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
