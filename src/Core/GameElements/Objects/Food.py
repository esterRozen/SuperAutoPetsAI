import inspect
import sys
# noinspection PyUnresolvedReferences
from . import Equipment


# this will create a list of all different animal objects, sorted into sub-lists
# according to their respective tiers
class Items:
    def __init__(self):
        self.items = [[], [], [], [], [], []]
        for name, obj in inspect.getmembers(sys.modules[__name__]):
            if inspect.ismodule(obj):
                if name == 'Equipment':
                    for item_name, item_obj in inspect.getmembers(obj):
                        module = inspect.getmodule(item_obj)
                        if module is not None and inspect.isclass(item_obj):
                            if module.__name__.endswith("tier_1"):
                                self.items[0] += [item_obj()]
                            elif module.__name__.endswith("tier_2"):
                                self.items[1] += [item_obj()]
                            elif module.__name__.endswith("tier_3"):
                                self.items[2] += [item_obj()]
                            elif module.__name__.endswith("tier_4"):
                                self.items[3] += [item_obj()]
                            elif module.__name__.endswith("tier_5"):
                                self.items[4] += [item_obj()]
                            elif module.__name__.endswith("tier_6"):
                                self.items[5] += [item_obj()]
