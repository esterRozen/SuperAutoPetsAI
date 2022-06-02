from typing import TYPE_CHECKING

from ...abstract_elements import Equipment, Animal
if TYPE_CHECKING:
    from ....overseer import MessageAgent


class _Tier5(Equipment):
    def __init__(self):
        super(_Tier5, self).__init__()

    @property
    def tier(self):
        return 5


class Chili(_Tier5):
    id = 410

    def query(self, animal: Animal, agent: 'MessageAgent', damage: int, message: str) -> int:
        if message == "outgoing":
            if animal in agent.team:
                actor = ("team", 0)
                target = ("enemy", 0)
            else:
                actor = ("enemy", 0)
                target = ("team", 0)

            second_unit = agent.team_opposing_(actor).second_unit
            if second_unit is not None:
                target = (target[0], agent.target_team.animals.index(second_unit))
                agent.deal_sneak_damage_handle_hurt(actor, target, 5)
            return damage
        return damage


class Chocolate(_Tier5):
    id = 411


class Peanut(_Tier5):
    id = 412
    rollable = False

    def query(self, animal: Animal, agent: 'MessageAgent', damage: int, message: str) -> int:
        if message == "outgoing":
            damage += 50
            return damage
        return damage


class Sushi(_Tier5):
    id = 413
    is_targeted = False


class Milk(_Tier5):
    id = 414
    rollable = False
    cost = 0


class Better_Milk(_Tier5):
    id = 415
    rollable = False
    cost = 0


class Best_Milk(_Tier5):
    id = 416
    rollable = False
    cost = 0
