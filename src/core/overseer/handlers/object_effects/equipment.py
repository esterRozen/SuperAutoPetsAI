from typing import TYPE_CHECKING, List

from ....eventnames import ON_FAINT, EAT_FOOD, ON_LEVEL, FRIEND_EATS_FOOD
from ....game_elements.game_objects import equipment

if TYPE_CHECKING:
    from ... import MessageAgent


# called when the item is given to a unit (specified in acting team member)
# handles applying the effect/equipping the item.
class Equipment:
    @staticmethod
    def apple(agent: 'MessageAgent'):
        agent.team[agent.event_raiser[1]].permanent_buff(1, 1)

    @staticmethod
    def honey(agent: 'MessageAgent'):
        agent.team[agent.event_raiser[1]].held = equipment.Honey()

    @staticmethod
    def cupcake(agent: 'MessageAgent'):
        agent.team[agent.event_raiser[1]].temp_buff(3, 3)

    @staticmethod
    def meat_bone(agent: 'MessageAgent'):
        agent.team[agent.event_raiser[1]].held = equipment.Meat_Bone()

    @staticmethod
    def sleeping_pill(agent: 'MessageAgent'):
        # raise faint, have variables set properly
        actor = agent.event_raiser[1]
        agent.handle_events()
        agent.team.faint(actor)

    @staticmethod
    def weak(agent: 'MessageAgent'):
        agent.team[agent.event_raiser[1]].held = equipment.Weak()

    @staticmethod
    def garlic(agent: 'MessageAgent'):
        agent.team[agent.event_raiser[1]].held = equipment.Garlic()

    @staticmethod
    def salad_bowl(agent: 'MessageAgent'):
        units: List[int] = agent.team.random_units_idx(2)
        for unit in units:
            agent.event_raiser = ("team", unit)
            agent.handle_events()

            agent.event_raiser = ("team", unit)
            agent.handle_events()

            agent.team[unit].permanent_buff(2, 2)

    @staticmethod
    def canned_food(agent: 'MessageAgent'):
        agent.shop.perm_buff(2, 1)

    @staticmethod
    def pear(agent: 'MessageAgent'):
        agent.team[agent.event_raiser[1]].permanent_buff(2, 2)

    @staticmethod
    def best_milk(agent: 'MessageAgent'):
        agent.team[agent.event_raiser[1]].permanent_buff(6, 3)

    @staticmethod
    def better_milk(agent: 'MessageAgent'):
        agent.team[agent.event_raiser[1]].permanent_buff(4, 2)

    @staticmethod
    def chili(agent: 'MessageAgent'):
        agent.team[agent.event_raiser[1]].held = equipment.Chili()

    @staticmethod
    def chocolate(agent: 'MessageAgent'):
        lvl = agent.team[agent.event_raiser[1]].level
        agent.team[agent.event_raiser[1]].increase_xp(1)

        if agent.team[agent.event_raiser[1]].level - lvl:
            agent.handle_events()

    @staticmethod
    def milk(agent: 'MessageAgent'):
        agent.team[agent.event_raiser[1]].permanent_buff(2, 1)

    @staticmethod
    def peanut(agent: 'MessageAgent'):
        agent.team[agent.event_raiser[1]].held = equipment.Peanut()

    @staticmethod
    def sushi(agent: 'MessageAgent'):
        units: List[int] = agent.team.random_units_idx(3)
        for unit in units:
            agent.event_raiser = ("team", unit)
            agent.handle_events()

            agent.event_raiser = ("team", unit)
            agent.handle_events()

            agent.team[unit].permanent_buff(1, 1)

    @staticmethod
    def coconut(agent: 'MessageAgent'):
        agent.team[agent.event_raiser[1]].held = equipment.Coconut()

    @staticmethod
    def melon(agent: 'MessageAgent'):
        agent.team[agent.event_raiser[1]].held = equipment.Melon()

    @staticmethod
    def mushroom(agent: 'MessageAgent'):
        agent.team[agent.event_raiser[1]].held = equipment.Mushroom()

    @staticmethod
    def pizza(agent: 'MessageAgent'):
        units: List[int] = agent.team.random_units_idx(2)
        for unit in units:
            agent.event_raiser = ("team", unit)
            agent.handle_events()

            agent.event_raiser = ("team", unit)
            agent.handle_events()

            agent.team[unit].permanent_buff(2, 2)

    @staticmethod
    def steak(agent: 'MessageAgent'):
        agent.team[agent.event_raiser[1]].held = equipment.Steak()
