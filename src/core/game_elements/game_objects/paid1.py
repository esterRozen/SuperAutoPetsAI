import inspect
import sys
# noinspection PyUnresolvedReferences
from . import paid_1_pack


# this will create a list of all different animal objects, sorted into sub-lists
# according to their respective tiers
class Paid1:
    def __init__(self):
        self.animals = [[], [], [], [], [], []]
        for name, obj in inspect.getmembers(sys.modules[__name__]):
            if inspect.ismodule(obj):
                if name == 'paid_1_pack':
                    for anim_name, anim_obj in inspect.getmembers(obj):
                        module = inspect.getmodule(anim_obj)
                        if module is not None and inspect.isclass(anim_obj):
                            if module.__name__.endswith("tier_1"):
                                self.animals[0] += [anim_obj()]
                            elif module.__name__.endswith("tier_2"):
                                self.animals[1] += [anim_obj()]
                            elif module.__name__.endswith("tier_3"):
                                self.animals[2] += [anim_obj()]
                            elif module.__name__.endswith("tier_4"):
                                self.animals[3] += [anim_obj()]
                            elif module.__name__.endswith("tier_5"):
                                self.animals[4] += [anim_obj()]
                            elif module.__name__.endswith("tier_6"):
                                self.animals[5] += [anim_obj()]
