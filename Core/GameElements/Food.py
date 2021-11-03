import inspect
import sys

# noinspection PyUnresolvedReferences
from Core.GameElements.Equipment import *


# meat and potatoes of it
# this will create a list of all different animal objects, sorted into sub-lists
# according to their respective tiers
class Items:
    def __init__(self):
        self.items = [[], [], [], [], [], []]
        for name, obj in inspect.getmembers(sys.modules[__name__]):
            if inspect.isclass(obj):
                class_name = inspect.getmodule(obj).__name__
                if class_name.startswith('Core.Animals.Equipment'):
                    if class_name.endswith("tier_1"):
                        self.items[0] += [obj()]
                    elif class_name.endswith("tier_2"):
                        self.items[1] += [obj()]
                    elif class_name.endswith("tier_3"):
                        self.items[2] += [obj()]
                    elif class_name.endswith("tier_4"):
                        self.items[3] += [obj()]
                    elif class_name.endswith("tier_5"):
                        self.items[4] += [obj()]
                    elif class_name.endswith("tier_6"):
                        self.items[5] += [obj()]
