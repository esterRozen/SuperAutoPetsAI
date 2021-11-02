import sys, inspect
from Core.Animals.Paid_1_Pack import *


# meat and potatoes of it
# this will create a list of all different animal objects, sorted into sublists
# according to their respective tiers
class Paid1:
    def __init__(self):
        self.animals = []
        for name, obj in inspect.getmembers(sys.modules[__name__]):
            if inspect.isclass(obj):
                class_name = inspect.getmodule(obj).__name__
                if class_name.startswith('Core.Animals.Paid_1'):
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