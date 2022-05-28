import inspect
import sys

# noinspection PyUnresolvedReferences
from typing import List, Union
# noinspection PyUnresolvedReferences
from . import units, equipment

base = [
    [
        'Ant', 'Beaver', 'Cricket', 'Duck', 'Fish',
        'Horse', 'Mosquito', 'Otter', 'Pig', 'Sloth',
    ], [
        'Crab', 'Dodo', 'Elephant', 'Flamingo', 'Hedgehog',
        'Peacock', 'Rat', 'Shrimp', 'Spider', 'Swan'
    ], [
        'Badger', 'Blowfish', 'Camel', 'Dog', 'Giraffe', 'Kangaroo',
        'Ox', 'Rabbit', 'Sheep', 'Snail', 'Turtle'
    ], [
        'Bison', 'Deer', 'Dolphin', 'Hippo', 'Parrot',
        'Penguin', 'Rooster', 'Skunk', 'Squirrel', 'Whale', 'Worm'
    ], [
        'Cow', 'Crocodile', 'Monkey', 'Rhino', 'Scorpion', 'Seal',
        'Shark', 'Turkey'
    ], [
        'Boar', 'Cat', 'Dragon', 'Fly', 'Gorilla',
        'Leopard', 'Mammoth', 'Snake', 'Tiger'
    ],
    ['Bee', 'Bus', 'Chick', 'DirtyRat', 'FlyFriend', 'Ram', 'ZombieCricket']
]

paid_1 = [
    [
        'Ant', 'Beaver', 'Beetle', 'Bluebird', 'Cricket', 'Fish',
        'Ladybug', 'Mosquito', 'Pig', 'Sloth',
    ], [
        'Bat', 'Dromedary', 'Flamingo', 'Hedgehog', 'Peacock',
        'Rat', 'Shrimp', 'Spider', 'Swan', 'TabbyCat'
    ], [
        'Blowfish', 'Caterpillar', 'Dog', 'HatchingChick',
        'Owl', 'Puppy', 'Rabbit', 'Sheep', 'Snail', 'TropicalFish',
        'Turtle'
    ], [
        'Bison', 'Buffalo', 'Deer', 'Dolphin', 'Llama',
        'Lobster', 'Microbe', 'Rooster', 'Skunk', 'Squirrel', 'Worm'
    ], [
        'Chicken', 'Cow', 'Eagle', 'Goat', 'Poodle', 'Rhino', 'Scorpion',
        'Seal', 'Shark', 'Turkey'
    ], [
        'Boar', 'Dragon', 'Gorilla', 'Leopard', 'Mammoth', 'Octopus',
        'Sauropod', 'Tiger', 'Tyrannosaurus'
    ], [
        'Bee', 'Bus', 'Butterfly', 'Chick', 'DirtyRat', 'FlyFriend',
        'Ram', 'ZombieCricket'
    ]
]

base_items = [
    ['Apple', 'Honey'],
    ['Cupcake', 'MeatBone', 'SleepingPill'],
    ['Garlic', 'SaladBowl'],
    ['CannedFood', 'Pear'],
    ['Chili', 'Chocolate', 'Sushi'],
    ['Melon', 'Mushroom', 'Pizza', 'Steak'],
    ['BestMilk', 'BetterMilk', 'Coconut', 'Milk', 'Peanut', 'Weak'],
]

paid_1_items = [
    ['Apple', 'Honey'],
    ['Cupcake', 'MeatBone', 'SleepingPill'],
    ['Garlic', 'SaladBowl'],
    ['CannedFood', 'Pear'],
    ['Chili', 'Chocolate', 'Sushi'],
    ['Melon', 'Mushroom', 'Pizza', 'Steak'],
    ['BestMilk', 'BetterMilk', 'Coconut', 'Milk', 'Peanut', 'Weak'],
]


def get_object_list(pack_type: str) -> List[List[str]]:
    if pack_type == "base pack":
        return base
    if pack_type == "base pack items":
        return base_items

    if pack_type == "paid pack 1":
        return paid_1
    if pack_type == "paid pack 1 items":
        return paid_1_items
    raise ValueError(f"{pack_type} is not a valid pack")


def add_unit_if_present(collection, list_objs, unit, name, tier: int):
    if name in collection[tier - 1]:
        list_objs[tier - 1].append(unit)
    elif name in collection[6]:
        list_objs[6].append(unit)


# this will create a list of all different animal or equipment objects,
# sorted into sub-lists according to their respective tiers
# last list are the un-rollable objects
class GameObjects:
    def __init__(self, pack_type: str):
        self.objs = [[], [], [], [], [], [], []]

        for name, obj in inspect.getmembers(sys.modules[__name__]):
            if inspect.ismodule(obj) and (name == 'units' or name == 'equipment'):
                obj_collection = get_object_list(pack_type)

                for anim_name, anim_obj in inspect.getmembers(obj):
                    module = inspect.getmodule(anim_obj)

                    if module is not None and inspect.isclass(anim_obj):
                        if module.__name__.endswith("tier_1"):
                            add_unit_if_present(obj_collection, self.objs,
                                                anim_obj(), anim_name, 1)

                        elif module.__name__.endswith("tier_2"):
                            add_unit_if_present(obj_collection, self.objs,
                                                anim_obj(), anim_name, 2)

                        elif module.__name__.endswith("tier_3"):
                            add_unit_if_present(obj_collection, self.objs,
                                                anim_obj(), anim_name, 3)

                        elif module.__name__.endswith("tier_4"):
                            add_unit_if_present(obj_collection, self.objs,
                                                anim_obj(), anim_name, 4)

                        elif module.__name__.endswith("tier_5"):
                            add_unit_if_present(obj_collection, self.objs,
                                                anim_obj(), anim_name, 5)

                        elif module.__name__.endswith("tier_6"):
                            add_unit_if_present(obj_collection, self.objs,
                                                anim_obj(), anim_name, 6)
