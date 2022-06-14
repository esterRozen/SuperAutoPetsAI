import inspect
import sys
from threading import Lock

from typing import List, Dict, Union
from . import animals, equipment


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
    ['Bee', 'Bus', 'Chick', 'Dirty_Rat', 'Fly_Friend', 'Ram', 'Zombie_Cricket']
]

paid_1 = [
    [
        'Ant', 'Beaver', 'Beetle', 'Bluebird', 'Cricket', 'Fish',
        'Ladybug', 'Mosquito', 'Pig', 'Sloth',
    ], [
        'Bat', 'Dromedary', 'Flamingo', 'Hedgehog', 'Peacock',
        'Rat', 'Shrimp', 'Spider', 'Swan', 'Tabby_Cat'
    ], [
        'Blowfish', 'Dog', 'Hatching_Chick',
        'Owl', 'Puppy', 'Rabbit', 'Sheep', 'Snail', 'Tropical_Fish',
        'Turtle'
    ], [
        'Bison', 'Buffalo', 'Caterpillar', 'Deer', 'Dolphin', 'Llama',
        'Lobster', 'Microbe', 'Rooster', 'Skunk', 'Squirrel', 'Worm'
    ], [
        'Chicken', 'Cow', 'Eagle', 'Goat', 'Poodle', 'Rhino', 'Scorpion',
        'Seal', 'Shark', 'Turkey'
    ], [
        'Boar', 'Dragon', 'Gorilla', 'Leopard', 'Mammoth', 'Octopus',
        'Sauropod', 'Tiger', 'Tyrannosaurus'
    ], [
        'Bee', 'Bus', 'Butterfly', 'Chick', 'Dirty_Rat', 'Fly_Friend',
        'Ram', 'Zombie_Cricket'
    ]
]

base_items = [
    ['Apple', 'Honey'],
    ['Cupcake', 'Meat_Bone', 'Sleeping_Pill'],
    ['Garlic', 'Salad_Bowl'],
    ['Canned_Food', 'Pear'],
    ['Chili', 'Chocolate', 'Sushi'],
    ['Melon', 'Mushroom', 'Pizza', 'Steak'],
    ['Best_Milk', 'Better_Milk', 'Coconut', 'Milk', 'Peanut', 'Weak'],
]

paid_1_items = [
    ['Apple', 'Honey'],
    ['Cupcake', 'Meat_Bone', 'Sleeping_Pill'],
    ['Garlic', 'Salad_Bowl'],
    ['Canned_Food', 'Pear'],
    ['Chili', 'Chocolate', 'Sushi'],
    ['Melon', 'Mushroom', 'Pizza', 'Steak'],
    ['Best_Milk', 'Better_Milk', 'Coconut', 'Milk', 'Peanut', 'Weak'],
]

pack_names = [
    "base pack", "base pack items",
    "paid pack 1", "paid pack 1 items"
]


class MetaSingleton(type):
    _instances = {}

    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance

        return cls._instances[cls]


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


def add_item_if_in_collection(collection, list_objs, unit, name, tier: int):
    if name in collection[tier - 1]:
        list_objs[tier - 1].append(unit)
    elif name in collection[6]:
        list_objs[6].append(unit)


# this will create a list of all different animal or equipment objects,
# sorted into sub-lists according to their respective tiers
# last list are the un-rollable objects
class GameObjects:
    def __init__(self):
        """
        supports flags:
            "base pack"
            "base pack items"
            "paid pack 1"
            "paid pack 1 items"
        Args:
        """
        self.animals = {}
        self.packs: Dict[str, List[List[Union[type(animals.Animal), type(equipment.Equipment)]]]] = {}
        for pack in pack_names:
            self.objs = [[], [], [], [], [], [], []]

            for name, obj in inspect.getmembers(sys.modules[__name__]):
                if inspect.ismodule(obj) and (name == 'animals' or name == 'equipment'):
                    obj_collection = get_object_list(pack)

                    for item_name, item_obj in inspect.getmembers(obj):
                        module = inspect.getmodule(item_obj)

                        if module is not None and inspect.isclass(item_obj):
                            if module.__name__.endswith("tier_1"):
                                add_item_if_in_collection(obj_collection, self.objs,
                                                          item_obj(), item_name, 1)
                                self.animals[item_obj().id] = item_obj

                            elif module.__name__.endswith("tier_2"):
                                add_item_if_in_collection(obj_collection, self.objs,
                                                          item_obj(), item_name, 2)
                                self.animals[item_obj().id] = item_obj

                            elif module.__name__.endswith("tier_3"):
                                add_item_if_in_collection(obj_collection, self.objs,
                                                          item_obj(), item_name, 3)
                                self.animals[item_obj().id] = item_obj

                            elif module.__name__.endswith("tier_4"):
                                add_item_if_in_collection(obj_collection, self.objs,
                                                          item_obj(), item_name, 4)
                                self.animals[item_obj().id] = item_obj

                            elif module.__name__.endswith("tier_5"):
                                add_item_if_in_collection(obj_collection, self.objs,
                                                          item_obj(), item_name, 5)
                                self.animals[item_obj().id] = item_obj

                            elif module.__name__.endswith("tier_6"):
                                add_item_if_in_collection(obj_collection, self.objs,
                                                          item_obj(), item_name, 6)
                                self.animals[item_obj().id] = item_obj

            self.packs[pack] = self.objs
