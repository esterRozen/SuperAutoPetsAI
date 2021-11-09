import inspect
import sys

# noinspection PyUnresolvedReferences
from .Base_Pack import *


# meat and potatoes of it <- future me weirded out past me said this
# this will create a list of all different animal objects, sorted into sub-lists
# according to their respective tiers
class Base:
    def __init__(self):
        self.animals = [[], [], [], [], [], []]
        for name, obj in inspect.getmembers(sys.modules[__name__]):
            if inspect.isclass(obj):
                class_name = inspect.getmodule(obj).__name__
                if class_name.startswith('Core.GameElements.Base_Pack'):
                    if class_name.endswith("tier_1"):
                        self.animals[0] += [obj()]
                    elif class_name.endswith("tier_2"):
                        self.animals[1] += [obj()]
                    elif class_name.endswith("tier_3"):
                        self.animals[2] += [obj()]
                    elif class_name.endswith("tier_4"):
                        self.animals[3] += [obj()]
                    elif class_name.endswith("tier_5"):
                        self.animals[4] += [obj()]
                    elif class_name.endswith("tier_6"):
                        self.animals[5] += [obj()]
