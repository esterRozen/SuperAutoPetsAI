from ..GameElements import *
from ..Shop import Shop
from ..Team import Team
from .BaseHandler import BaseHandler

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
class MessageHandler(BaseHandler):
    in_shop = True

    def __init__(self, mode):
        self.spawner = Spawner(mode)
        self.team = Team([Empty()] * 5, [Equipment()] * 5)
        self.enemy = Team([Empty()] * 5, [Equipment()] * 5)
        self.shop = Shop(mode, 3, 1)

        self.lvl = 0
        self.gold = 0
        self.turn = 1
        self.battle_lost = False

        # animal that triggered the event is the event_raiser
        # animal that responded to event is the acting animal
        self.event_raiser = 0

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
                     ]

    def load(self, team, turn, gold=10, shop=None, hearts=4, battle_lost=False):
        # re-enter the shop from a given game state
        # used for simulation/replay
        pass

    def send_engine_message(self, message):
        # for unit in roster sorted by descending attack, then descending
        # hp, send message, handle response
        # sending messages like buy, sell, move, combine, start turn, end turn,
        # start turn, reroll, freeze/unfreeze, hurt, faint, knock out, attacks,
        # before attack, unit ahead attacks, unit ahead faints, friend summoned
        pass

    def handle(self, message):
        # trigger function that manipulates roster
        self.lvl = self.team.level()
        self.func[message]()

    def buff(self, unit, atk, hp):
        if self.in_shop:
            if isinstance(unit, Animal):
                unit.permanent_buff(atk, hp)
            else:
                for animal in unit:
                    animal.permanent_buff(atk, hp)
        else:
            if isinstance(unit, Animal):
                unit.temp_buff(atk, hp)
            else:
                for animal in unit:
                    animal.temp_buff(atk, hp)
        return

    # assume event which triggered event handler has already resolved!!!
    # e.g. if animal sold, then it is no longer in the roster and gold
    # incremented already

    def _nop(self):
        pass

    def _ant(self):
        # permanently buff random animal on team.
        friend = self.team.random_friend()
        if friend == []:
            return
        if self.lvl == 1:
            self.buff(friend, 2, 1)
        elif self.lvl == 2:
            self.buff(friend, 4, 2)
        else:
            self.buff(friend, 6, 3)

    # on sell give 2 +1/2/3 hp
    def _beaver(self):
        friends = self.team.random_friends(2)
        if friends == []:
            return
        if self.lvl == 1:
            [friend.permanent_buff(1, 0) for friend in friends]
        elif self.lvl == 2:
            [friend.permanent_buff(2, 0) for friend in friends]
        else:
            [friend.permanent_buff(3, 0) for friend in friends]

    def _beetle(self):
        if self.lvl == 1:
            self.shop.buff(0, 1)
        elif self.lvl == 2:
            self.shop.buff(0, 2)
        else:
            self.shop.buff(0, 3)

    # give leftmost friend 1, 2, 3 atk
    def _bluebird(self):
        if self.lvl == 1:
            self.team.leftmost_unit().permanent_buff(1, 0)
        elif self.lvl == 2:
            self.team.leftmost_unit().permanent_buff(2, 0)
        else:
            self.team.leftmost_unit().permanent_buff(3, 0)

    # how to handle summons???
    def _cricket(self):
        # TODO
        pass

    def _duck(self):
        if self.lvl == 1:
            self.shop.buff(1, 1)
        elif self.lvl == 2:
            self.shop.buff(2, 2)
        else:
            self.shop.buff(3, 3)

    # on level give all friends +1/1, +2/2, X
    def _fish(self):
        if self.lvl == 1:
            print("this shouldn't happen! fish lvl 1 trigger")
            return
        if self.lvl == 2:
            self.buff(self.team.friends(), 1, 1)
        elif self.lvl == 3:
            self.buff(self.team.friends(), 2, 2)

    # friend summoned, give +1/2/3 atk until end of battle
    def _horse(self):
        if self.lvl == 1:
            self.team.animals[self.event_raiser].temp_buff(1, 0)
        elif self.lvl == 2:
            self.team.animals[self.event_raiser].temp_buff(2, 0)
        else:
            self.team.animals[self.event_raiser].temp_buff(3, 0)

    # buy food, gain x/x until end of battle
    def _ladybug(self):
        if self.lvl == 1:
            self.team.animals[self.team.acting].temp_buff(1, 1)
        elif self.lvl == 2:
            self.team.animals[self.team.acting].temp_buff(2, 2)
        else:
            self.team.animals[self.team.acting].temp_buff(3, 3)

    # start of battle deal 1/2/3 damage to random enemy
    def _mosquito(self):
        # TODO
        pass

    # buy, give a random friend +1/1, 2/2, 3/3
    def _otter(self):
        if self.lvl == 1:
            self.team.random_friend().permanent_buff(1, 1)
        elif self.lvl == 2:
            self.team.random_friend().permanent_buff(2, 2)
        else:
            self.team.random_friend().permanent_buff(3, 3)

    # gain extra +1/2/3 gold on sell
    def _pig(self):
        if self.lvl == 1:
            self.gold += 1
        elif self.lvl == 2:
            self.gold += 2
        else:
            self.gold += 3
        pass

    # have to implement equipments
    def _bat(self):
        # TODO
        pass

    def _crab(self):
        battle_hp = self.team.friend_ahead().battle_hp
        self.team.animals[self.team.acting].battle_hp = battle_hp

    def _dodo(self):
        battle_atk = self.team.animals[self.team.acting].battle_atk
        if self.lvl == 1:
            self.team.friend_ahead().battle_atk += battle_atk
        elif self.lvl == 2:
            self.team.friend_ahead().battle_atk += 2*battle_atk
        else:
            self.team.friend_ahead().battle_atk += 3*battle_atk

    def _dog(self):
        if self.lvl == 1:
            self.team.animals[self.team.acting].permanent_buff(1, 1)
        elif self.lvl == 2:
            self.team.animals[self.team.acting].permanent_buff(2, 2)
        else:
            self.team.animals[self.team.acting].permanent_buff(3, 3)

    def _dromedary(self):
        if self.lvl == 1:
            self.shop.buff(1, 1)
        elif self.lvl == 2:
            self.shop.buff(2, 2)
        else:
            self.shop.buff(3, 3)

    def _elephant(self):
        # TODO
        pass

    def _flamingo(self):
        friends = self.team.friends_behind(2)
        if self.lvl == 1:
            self.buff(friends, 1, 1)
        elif self.lvl == 2:
            self.buff(friends, 2, 2)
        else:
            self.buff(friends, 3, 3)

    # hedgehog has to trigger the hurt trigger!!
    def _hedgehog(self):
        # TODO
        pass

    def _peacock(self):
        if self.lvl == 1:
            self.team.animals[self.team.acting].temp_buff(2, 0)
        elif self.lvl == 2:
            self.team.animals[self.team.acting].temp_buff(4, 0)
        else:
            self.team.animals[self.team.acting].temp_buff(6, 0)

    # summons, ugh
    def _rat(self):
        # TODO
        pass

    def _shrimp(self):
        if self.lvl == 1:
            self.team.random_friend().temp_buff(0, 1)
        elif self.lvl == 2:
            self.team.random_friend().temp_buff(0, 2)
        else:
            self.team.random_friend().temp_buff(0, 3)

    # more summons!!
    def _spider(self):
        # TODO
        pass

    def _swan(self):
        if self.lvl == 1:
            self.gold += 1
        elif self.lvl == 2:
            self.gold += 2
        else:
            self.gold += 3

    def _tabby_cat(self):
        if self.lvl == 1:
            [friend.temp_buff(1, 0) for friend in self.team.friends()]
        elif self.lvl == 2:
            [friend.temp_buff(2, 0) for friend in self.team.friends()]
        else:
            [friend.temp_buff(3, 0) for friend in self.team.friends()]

    # triggers hurt ugh
    def _badger(self):
        # TODO
        pass

    # triggers hurt
    def _blowfish(self):
        # TODO
        pass

    def _camel(self):
        if self.lvl == 1:
            self.buff(self.team.friend_behind(), 1, 2)
        elif self.lvl == 2:
            self.buff(self.team.friend_behind(), 2, 4)
        else:
            self.buff(self.team.friend_behind(), 3, 6)

    def _caterpillar(self):
        if self.lvl == 1:
            self.team.animals[self.team.acting].xp += 1
        elif self.lvl == 2:
            self.team.animals[self.team.acting].xp += 1
        else:
            # TODO caterpillar level 3
            pass

    def _giraffe(self):
        if self.lvl == 1:
            self.buff(self.team.friends_ahead(1), 1, 1)
        elif self.lvl == 2:
            self.buff(self.team.friends_ahead(2), 1, 1)
        else:
            self.buff(self.team.friends_ahead(3), 1, 1)

    def _hatching_chick(self):
        if self.lvl == 1:
            self.team.friend_ahead().temp_buff(5, 5)
        elif self.lvl == 2:
            self.team.friend_ahead().permanent_buff(2, 2)
        else:
            self.team.friend_ahead().increase_xp(1)

    def _kangaroo(self):
        if self.lvl == 1:
            self.team.animals[self.team.acting].temp_buff(2, 2)
        elif self.lvl == 2:
            self.team.animals[self.team.acting].temp_buff(4, 4)
        else:
            self.team.animals[self.team.acting].temp_buff(6, 6)

    def _owl(self):
        if self.lvl == 1:
            self.team.random_friend().permanent_buff(2, 2)
        elif self.lvl == 2:
            self.team.random_friend().permanent_buff(4, 4)
        else:
            self.team.random_friend().permanent_buff(6, 6)

    def _ox(self):
        # TODO
        pass

    def _puppy(self):
        if self.gold < 2:
            return
        if self.lvl == 1:
            self.team.animals[self.team.acting].permanent_buff(2, 2)
        elif self.lvl == 2:
            self.team.animals[self.team.acting].permanent_buff(4, 4)
        else:
            self.team.animals[self.team.acting].permanent_buff(6, 6)

    def _rabbit(self):
        if self.lvl == 1:
            self.team.animals[self.event_raiser].permanent_buff(0, 1)
        elif self.lvl == 2:
            self.team.animals[self.event_raiser].permanent_buff(0, 2)
        else:
            self.team.animals[self.event_raiser].permanent_buff(0, 3)

    def _sheep(self):
        # TODO
        pass

    def _snail(self):
        if not self.battle_lost:
            return
        if self.lvl == 1:
            self.buff(self.team.friends(), 2, 1)
        elif self.lvl == 2:
            self.buff(self.team.friends(), 4, 2)
        else:
            self.buff(self.team.friends(), 6, 3)

    def _tropical_fish(self):
        if self.lvl == 1:
            self.team.friend_ahead().permanent_buff(0, 1)
            self.team.friend_behind().permanent_buff(0, 1)
        elif self.lvl == 2:
            self.team.friend_ahead().permanent_buff(0, 2)
            self.team.friend_behind().permanent_buff(0, 2)
        else:
            self.team.friend_ahead().permanent_buff(0, 3)
            self.team.friend_behind().permanent_buff(0, 3)

    def _turtle(self):
        # TODO
        pass

    def _whale(self):
        # TODO
        pass

    def _bison(self):
        if not self.team.has_lvl3():
            return
        if self.lvl == 1:
            self.team.animals[self.team.acting].permanent_buff(2, 2)
        elif self.lvl == 2:
            self.team.animals[self.team.acting].permanent_buff(4, 4)
        else:
            self.team.animals[self.team.acting].permanent_buff(6, 6)

    def _buffalo(self):
        if self.lvl == 1:
            self.team.animals[self.team.acting].permanent_buff(1, 1)
        elif self.lvl == 2:
            self.team.animals[self.team.acting].permanent_buff(2, 2)
        else:
            self.team.animals[self.team.acting].permanent_buff(3, 3)

    def _deer(self):
        # TODO
        pass

    def _dolphin(self):
        # TODO
        animal = self.enemy.lowest_health()
        if self.lvl == 1:
            pass
        elif self.lvl == 2:
            pass
        else:
            pass

    def _hippo(self):
        if self.lvl == 1:
            self.team.animals[self.team.acting].temp_buff(2, 2)
        elif self.lvl == 2:
            self.team.animals[self.team.acting].temp_buff(4, 4)
        else:
            self.team.animals[self.team.acting].temp_buff(6, 6)

    def _llama(self):
        if self.team.size() > 4:
            return
        if self.lvl == 1:
            self.team.animals[self.team.acting].permanent_buff(2, 2)
        elif self.lvl == 2:
            self.team.animals[self.team.acting].permanent_buff(4, 4)
        else:
            self.team.animals[self.team.acting].permanent_buff(6, 6)

    def _lobster(self):
        if self.lvl == 1:
            self.team.animals[self.event_raiser].permanent_buff(2, 2)
        elif self.lvl == 2:
            self.team.animals[self.event_raiser].permanent_buff(4, 4)
        else:
            self.team.animals[self.event_raiser].permanent_buff(6, 6)
        pass

    def _monkey(self):
        animal_to_buff = self.team.rightmost_unit()
        if self.lvl == 1:
            self.buff(animal_to_buff, 2, 2)
        elif self.lvl == 2:
            self.buff(animal_to_buff, 4, 4)
        else:
            self.buff(animal_to_buff, 6, 6)

    def _penguin(self):
        animals_to_buff = self.team.other_lvl2_or_3()
        if self.lvl == 1:
            self.buff(animals_to_buff, 1, 1)
        elif self.lvl == 2:
            self.buff(animals_to_buff, 2, 2)
        else:
            self.buff(animals_to_buff, 3, 3)

    def _poodle(self):
        animals_to_buff = self.team.ret_diff_tiers()
        if self.lvl == 1:
            for animal in animals_to_buff:
                animal.permanent_buff(1, 1)
        elif self.lvl == 2:
            for animal in animals_to_buff:
                animal.permanent_buff(2, 2)
        else:
            for animal in animals_to_buff:
                animal.permanent_buff(3, 3)

    def _rooster(self):
        # TODO
        pass

    def _skunk(self):
        # TODO
        pass

    def _squirrel(self):
        food_slot = self.shop.roster[-1]
        for slot in self.shop.roster:
            slot.item = food_slot.spawn(self.shop.tier)

    def _worm(self):
        if self.lvl == 1:
            self.team.animals[self.team.acting].permanent_buff(1, 1)
        elif self.lvl == 2:
            self.team.animals[self.team.acting].permanent_buff(2, 2)
        else:
            self.team.animals[self.team.acting].permanent_buff(3, 3)

    def _chicken(self):
        if self.lvl == 1:
            self.shop.perm_buff(1, 1)
        elif self.lvl == 2:
            self.shop.perm_buff(2, 2)
        else:
            self.shop.perm_buff(3, 3)

    # add cow's milk to shop
    def _cow(self):
        # TODO
        pass

    # deal 7/14/21 damage to last enemy
    def _crocodile(self):
        # TODO
        pass

    def _eagle(self):
        # TODO
        pass

    # limited activation count stored in Goat object
    def _goat(self):
        self.gold += 1

    def _microbe(self):
        # TODO
        pass

    # copy ability should be stored in the parrot object
    def _parrot(self):
        # TODO
        pass

    def _rhino(self):
        # TODO
        pass

    def _scorpion(self):
        pass

    def _seal(self):
        friends = self.team.random_friends(2)
        if self.lvl == 1:
            self.buff(friends, 1, 1)
        elif self.lvl == 2:
            self.buff(friends, 2, 2)
        else:
            self.buff(friends, 3, 3)

    def _shark(self):
        if self.lvl == 1:
            self.buff(self.team.animals[self.team.acting], 2, 1)
        elif self.lvl == 2:
            self.buff(self.team.animals[self.team.acting], 4, 2)
        else:
            self.buff(self.team.animals[self.team.acting], 6, 3)

    def _turkey(self):
        if self.lvl == 1:
            self.buff(self.team.animals[self.event_raiser], 3, 3)
        elif self.lvl == 2:
            self.buff(self.team.animals[self.event_raiser], 6, 6)
        else:
            self.buff(self.team.animals[self.event_raiser], 9, 9)

    # not 100% sure how to implement cat.
    def _cat(self):
        # TODO
        pass

    def _dragon(self):
        if self.lvl == 1:
            self.buff(self.team.friends(), 1, 1)
        elif self.lvl == 2:
            self.buff(self.team.friends(), 2, 2)
        else:
            self.buff(self.team.friends(), 2, 2)

    def _fly(self):
        # TODO
        pass

    def _gorilla(self):
        # TODO
        pass

    def _leopard(self):
        # TODO
        pass

    def _mammoth(self):
        if self.lvl == 1:
            self.buff(self.team.friends(), 2, 2)
        elif self.lvl == 2:
            self.buff(self.team.friends(), 4, 4)
        else:
            self.buff(self.team.friends(), 6, 6)

    def _octopus(self):
        # TODO
        pass

    def _sauropod(self):
        self.gold += 1

    def _snake(self):
        # TODO
        pass

    # how to do this??
    def _tiger(self):
        # TODO
        pass

    def _tyrannosaurus(self):
        if self.gold < 3:
            return
        if self.lvl == 1:
            self.buff(self.team.friends(), 2, 2)
        elif self.lvl == 2:
            self.buff(self.team.friends(), 4, 4)
        else:
            self.buff(self.team.friends(), 6, 6)


if __name__ == '__main__':
    while True:
        # a = MessageHandler()
        print(animals[int(input("\nAnimal number: "))])
