from typing import TYPE_CHECKING, List, Tuple

from ....eventnames import ON_FAINT, EAT_FOOD, ON_LEVEL, FRIEND_EATS_FOOD, FRIEND_AHEAD_FAINTS, FRIEND_FAINTS
from ....game_elements.abstract_elements import Animal
from ....game_elements.game_objects.animals import Bee

if TYPE_CHECKING:
    from ... import MessageAgent


# called when the item is given to a unit (specified in acting team member)
# handles applying the effect/equipping the item.
class Equipment:
    @staticmethod
    def apple(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        agent.actor(actor).permanent_buff(1, 1)

    @staticmethod
    def honey(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int], fainted: Animal):
        bee = Bee()
        agent.summon(bee, actor)

    ###################################################################

    @staticmethod
    def cupcake(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        agent.actor(actor).temp_buff(3, 3)

    @staticmethod
    def meat_bone(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        pass

    @staticmethod
    def sleeping_pill(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        # raise faint, have variables set properly
        animal = agent.team[actor[1]]

        agent.enqueue_event(ON_FAINT,
                            actor=actor, fainted=animal)
        agent.team.faint(actor[1])

        agent.enqueue_event(FRIEND_AHEAD_FAINTS,
                            actor=actor, fainted=animal)

        agent.enqueue_event(FRIEND_FAINTS,
                            actor=actor, fainted=animal)

    ###################################################################

    @staticmethod
    def weak(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        pass

    @staticmethod
    def garlic(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        pass

    @staticmethod
    def salad_bowl(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        units: List[int] = agent.team.random_units_idx(2)
        for unit in units:
            agent.enqueue_event(EAT_FOOD,
                                actor=("team", unit))

            agent.enqueue_event(FRIEND_EATS_FOOD,
                                actor=("team", unit))

            agent.team[unit].permanent_buff(2, 2)

    ###################################################################

    @staticmethod
    def canned_food(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        agent.shop.perm_buff(2, 1)

    @staticmethod
    def pear(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        agent.actor(actor).permanent_buff(2, 2)

    ###################################################################

    @staticmethod
    def best_milk(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        agent.actor(actor).permanent_buff(6, 3)

    @staticmethod
    def better_milk(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        agent.actor(actor).permanent_buff(4, 2)

    @staticmethod
    def chili(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        pass

    @staticmethod
    def chocolate(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        lvl = agent.actor(actor).level
        agent.actor(actor).increase_xp(1)

        if agent.actor(actor).level - lvl:
            agent.enqueue_event(ON_LEVEL,
                                actor=actor)

    @staticmethod
    def milk(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        agent.actor(actor).permanent_buff(2, 1)

    @staticmethod
    def peanut(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        pass

    ###################################################################

    @staticmethod
    def sushi(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        units: List[int] = agent.team.random_units_idx(3)
        for unit in units:
            agent.event_raiser = ("team", unit)
            agent.handle_events()

            agent.event_raiser = ("team", unit)
            agent.handle_events()

            agent.team[unit].permanent_buff(1, 1)

    @staticmethod
    def coconut(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        pass

    @staticmethod
    def melon(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        pass

    @staticmethod
    def mushroom(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int], fainted: Animal):
        summoned_animal: Animal = fainted.__new__(type(fainted))
        summoned_animal.hp = 1
        summoned_animal.atk = 1
        summoned_animal.battle_hp = 1
        summoned_animal.battle_atk = 1

        agent.summon(summoned_animal, actor)

    @staticmethod
    def pizza(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        units: List[int] = agent.team.random_units_idx(2)
        for unit in units:
            agent.event_raiser = ("team", unit)
            agent.handle_events()

            agent.event_raiser = ("team", unit)
            agent.handle_events()

            agent.team[unit].permanent_buff(2, 2)

    @staticmethod
    def steak(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        pass
