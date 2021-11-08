from Core.Shop.shop import Shop
from Core.Overseer.BaseHandler import BaseHandler
from Core.GameElements.simpleClasses import Empty, Equipment, Animal
from Core.Team.team import Team

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
        self.lvl = 0
        self.gold = 0
        self.turn = 1
        self.event_raiser = 0
        self.team = Team([Empty()]*5, [Equipment()]*5)
        self.shop = Shop(mode, 3, 1)
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

    def load(self, team, turn, gold=10, shop=None):
        # re-enter the shop from a given game state
        pass

    def send_engine_message(self, message):
        # for unit in roster sorted by descending attack, then descending
        # hp, send message, handle response
        pass

    def handle(self, message):
        # trigger function that manipulates roster
        self.lvl = self.team.level()
        self.func[message]()

    def buff(self, unit: Animal, atk, hp):
        if self.in_shop:
            unit.permanent_buff(atk, hp)
        else:
            unit.temp_buff(atk, hp)
        return

    def _nop(self):
        pass

    # assume event which triggered event handler has already resolved!!!
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

        pass

    # how to handle summons???
    def _cricket(self):
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
        pass

    # friend summoned, give +1/2/3 atk until end of battle
    def _horse(self):
        if self.lvl == 1:
            self.team.animals[self.event_raiser].temp_buff(1, 0)
        elif self.lvl == 2:
            self.team.animals[self.event_raiser].temp_buff(2, 0)
        else:
            self.team.animals[self.event_raiser].temp_buff(3, 0)

    #
    def _ladybug(self):
        pass

    # start of battle deal 1/2/3 damage to random enemy
    def _mosquito(self):
        pass

    # buy, give a random friend +1/1, 2/2, 3/3
    def _otter(self):
        if self.lvl == 1:
            self.team.random_friend().permanent_buff(1, 1)
        elif self.lvl == 2:
            self.team.random_friend().permanent_buff(2, 2)
        else:
            self.team.random_friend().permanent_buff(3, 3)

    # have to implement money
    def _pig(self):
        pass

    # have to implement equipments
    def _bat(self):
        pass

    def _crab(self):
        pass

    def _dodo(self):
        pass

    def _dog(self):
        pass

    def _dromedary(self):
        pass

    def _elephant(self):
        pass

    def _flamingo(self):
        pass

    def _hedgehog(self):
        pass

    def _peacock(self):
        pass

    def _rat(self):
        pass

    def _shrimp(self):
        pass

    def _spider(self):
        pass

    def _swan(self):
        pass

    def _tabby_cat(self):
        pass

    def _badger(self):
        pass

    def _blowfish(self):
        pass

    def _camel(self):
        pass

    def _caterpillar(self):
        pass

    def _giraffe(self):
        pass

    def _hatching_chick(self):
        pass

    def _kangaroo(self):
        pass

    def _owl(self):
        pass

    def _ox(self):
        pass

    def _puppy(self):
        pass

    def _rabbit(self):
        pass

    def _sheep(self):
        pass

    def _snail(self):
        pass

    def _tropical_fish(self):
        pass

    def _turtle(self):
        pass

    def _whale(self):
        pass

    def _bison(self):
        pass

    def _buffalo(self):
        pass

    def _deer(self):
        pass

    def _dolphin(self):
        pass

    def _hippo(self):
        pass

    def _llama(self):
        pass

    def _lobster(self):
        pass

    def _monkey(self):
        pass

    def _penguin(self):
        pass

    def _poodle(self):
        pass

    def _rooster(self):
        pass

    def _skunk(self):
        pass

    def _squirrel(self):
        pass

    def _worm(self):
        pass

    def _chicken(self):
        pass

    def _cow(self):
        pass

    def _crocodile(self):
        pass

    def _eagle(self):
        pass

    def _goat(self):
        pass

    def _microbe(self):
        pass

    def _parrot(self):
        pass

    def _rhino(self):
        pass

    def _scorpion(self):
        pass

    def _seal(self):
        pass

    def _shark(self):
        pass

    def _turkey(self):
        pass

    def _cat(self):
        pass

    def _dragon(self):
        pass

    def _fly(self):
        pass

    def _gorilla(self):
        pass

    def _leopard(self):
        pass

    def _mammoth(self):
        pass

    def _octopus(self):
        pass

    def _sauropod(self):
        pass

    def _snake(self):
        pass

    def _tiger(self):
        pass

    def _tyrannosaurus(self):
        pass


# noinspection DuplicatedCode
class BattleMessageHandler(BaseHandler):
    def __init__(self):
        self.roster = [Empty]*5
        self.enemy = [Empty]*5

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

    def load(self, team, turn):
        # enter new battle with team
        pass

    def fight(self, enemy):
        self.enemy = enemy

    def send_engine_message(self, message):
        # for unit in roster sorted by descending attack, then descending
        # hp, send message, handle response
        pass

    def handle(self, message):
        # trigger function that manipulates roster
        self.func[message]()

    def _nop(self):
        pass

    def _ant(self):
        pass

    def _beaver(self):
        pass

    def _beetle(self):
        pass

    def _bluebird(self):
        pass

    def _cricket(self):
        pass

    def _duck(self):
        pass

    def _fish(self):
        pass

    def _horse(self):
        pass

    def _ladybug(self):
        pass

    def _mosquito(self):
        pass

    def _otter(self):
        pass

    def _pig(self):
        pass

    def _bat(self):
        pass

    def _crab(self):
        pass

    def _dodo(self):
        pass

    def _dog(self):
        pass

    def _dromedary(self):
        pass

    def _elephant(self):
        pass

    def _flamingo(self):
        pass

    def _hedgehog(self):
        pass

    def _peacock(self):
        pass

    def _rat(self):
        pass

    def _shrimp(self):
        pass

    def _spider(self):
        pass

    def _swan(self):
        pass

    def _tabby_cat(self):
        pass

    def _badger(self):
        pass

    def _blowfish(self):
        pass

    def _camel(self):
        pass

    def _caterpillar(self):
        pass

    def _giraffe(self):
        pass

    def _hatching_chick(self):
        pass

    def _kangaroo(self):
        pass

    def _owl(self):
        pass

    def _ox(self):
        pass

    def _puppy(self):
        pass

    def _rabbit(self):
        pass

    def _sheep(self):
        pass

    def _snail(self):
        pass

    def _tropical_fish(self):
        pass

    def _turtle(self):
        pass

    def _whale(self):
        pass

    def _bison(self):
        pass

    def _buffalo(self):
        pass

    def _deer(self):
        pass

    def _dolphin(self):
        pass

    def _hippo(self):
        pass

    def _llama(self):
        pass

    def _lobster(self):
        pass

    def _monkey(self):
        pass

    def _penguin(self):
        pass

    def _poodle(self):
        pass

    def _rooster(self):
        pass

    def _skunk(self):
        pass

    def _squirrel(self):
        pass

    def _worm(self):
        pass

    def _chicken(self):
        pass

    def _cow(self):
        pass

    def _crocodile(self):
        pass

    def _eagle(self):
        pass

    def _goat(self):
        pass

    def _microbe(self):
        pass

    def _parrot(self):
        pass

    def _rhino(self):
        pass

    def _scorpion(self):
        pass

    def _seal(self):
        pass

    def _shark(self):
        pass

    def _turkey(self):
        pass

    def _cat(self):
        pass

    def _dragon(self):
        pass

    def _fly(self):
        pass

    def _gorilla(self):
        pass

    def _leopard(self):
        pass

    def _mammoth(self):
        pass

    def _octopus(self):
        pass

    def _sauropod(self):
        pass

    def _snake(self):
        pass

    def _tiger(self):
        pass

    def _tyrannosaurus(self):
        pass


if __name__ == '__main__':
    while True:
        a = MessageHandler()
        print(animals[int(input("\nAnimal number: "))])
