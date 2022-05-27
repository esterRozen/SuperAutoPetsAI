from typing import TYPE_CHECKING, List

from ....eventnames import ON_FAINT, EAT_FOOD, ON_LEVEL
from ....game_elements.game_objects.equipment import *

if TYPE_CHECKING:
    from ... import MessageAgent


# called when the item is given to a unit (specified in acting team member)
class Equipment:
    @staticmethod
    def apple(agent: 'MessageAgent'):
        # raise eat food
        actor = agent.team.acting
        agent.event_raiser = ("team", agent.team.acting)
        agent.handle_event(EAT_FOOD)
        agent.team[actor].permanent_buff(1, 1)

    @staticmethod
    def honey(agent: 'MessageAgent'):
        # raise eat food
        actor = agent.team.acting
        agent.event_raiser = ("team", agent.team.acting)
        agent.handle_event(EAT_FOOD)
        agent.team[actor].held = Honey()

    @staticmethod
    def cupcake(agent: 'MessageAgent'):
        # raise eat food
        actor = agent.team.acting
        agent.event_raiser = ("team", agent.team.acting)
        agent.handle_event(EAT_FOOD)
        agent.team[actor].temp_buff(3, 3)

    @staticmethod
    def meat_bone(agent: 'MessageAgent'):
        # raise eat food
        actor = agent.team.acting
        agent.event_raiser = ("team", agent.team.acting)
        agent.handle_event(EAT_FOOD)
        agent.team[actor].held = MeatBone()

    @staticmethod
    def sleeping_pill(agent: 'MessageAgent'):
        # raise eat food
        # raise faint, have variables set properly
        actor = agent.team.acting
        agent.event_raiser = ("team", agent.team.acting)
        agent.handle_event(EAT_FOOD)

        agent.event_raiser = ("team", actor)
        agent.handle_event(ON_FAINT)
        agent.team.faint(actor)

    @staticmethod
    def garlic(agent: 'MessageAgent'):
        actor = agent.team.acting
        agent.event_raiser = ("team", agent.team.acting)
        agent.handle_event(EAT_FOOD)

        agent.team[actor].held = Garlic()

    @staticmethod
    def salad_bowl(agent: 'MessageAgent'):
        units: List[int] = agent.team.random_units_idx(2)
        for unit in units:
            agent.event_raiser = ("team", unit)
            agent.handle_event(EAT_FOOD)

            agent.team[unit].permanent_buff(2, 2)

    @staticmethod
    def canned_food(agent: 'MessageAgent'):
        agent.shop.perm_buff(2, 1)

    @staticmethod
    def pear(agent: 'MessageAgent'):
        actor = agent.team.acting
        agent.event_raiser = ("team", agent.team.acting)
        agent.handle_event(EAT_FOOD)

        agent.team[actor].permanent_buff(2, 2)

    @staticmethod
    def best_milk(agent: 'MessageAgent'):
        actor = agent.team.acting
        agent.event_raiser = ("team", agent.team.acting)
        agent.handle_event(EAT_FOOD)

        agent.team[actor].permanent_buff(6, 3)

    @staticmethod
    def better_milk(agent: 'MessageAgent'):
        actor = agent.team.acting
        agent.event_raiser = ("team", agent.team.acting)
        agent.handle_event(EAT_FOOD)

        agent.team[actor].permanent_buff(4, 2)

    @staticmethod
    def chili(agent: 'MessageAgent'):
        actor = agent.team.acting
        agent.event_raiser = ("team", agent.team.acting)
        agent.handle_event(EAT_FOOD)

        agent.team[actor].held = Chili()

    @staticmethod
    def chocolate(agent: 'MessageAgent'):
        actor = agent.team.acting
        agent.event_raiser = ("team", agent.team.acting)
        agent.handle_event(EAT_FOOD)

        lvl = agent.team[actor].level
        agent.team[actor].increase_xp(1)

        if agent.team[actor].level - lvl:
            agent.event_raiser = ("team", actor)
            agent.handle_event(ON_LEVEL)

    @staticmethod
    def milk(agent: 'MessageAgent'):
        actor = agent.team.acting
        agent.event_raiser = ("team", agent.team.acting)
        agent.handle_event(EAT_FOOD)

        agent.team[actor].permanent_buff(2, 1)

    @staticmethod
    def peanut(agent: 'MessageAgent'):
        actor = agent.team.acting
        agent.event_raiser = ("team", agent.team.acting)
        agent.handle_event(EAT_FOOD)

        agent.team[actor].held = Peanut()

    @staticmethod
    def sushi(agent: 'MessageAgent'):
        units: List[int] = agent.team.random_units_idx(3)
        for unit in units:
            agent.event_raiser = ("team", unit)
            agent.handle_event(EAT_FOOD)

            agent.team[unit].permanent_buff(1, 1)

    @staticmethod
    def coconut(agent: 'MessageAgent'):
        actor = agent.team.acting
        agent.event_raiser = ("team", agent.team.acting)
        agent.handle_event(EAT_FOOD)

        agent.team[actor].held = Coconut()

    @staticmethod
    def melon(agent: 'MessageAgent'):
        actor = agent.team.acting
        agent.event_raiser = ("team", agent.team.acting)
        agent.handle_event(EAT_FOOD)

        agent.team[actor].held = Melon()

    @staticmethod
    def mushroom(agent: 'MessageAgent'):
        actor = agent.team.acting
        agent.event_raiser = ("team", agent.team.acting)
        agent.handle_event(EAT_FOOD)

        agent.team[actor].held = Mushroom()

    @staticmethod
    def pizza(agent: 'MessageAgent'):
        units: List[int] = agent.team.random_units_idx(2)
        for unit in units:
            agent.event_raiser = ("team", unit)
            agent.handle_event(EAT_FOOD)

            agent.team[unit].permanent_buff(2, 2)

    @staticmethod
    def steak(agent: 'MessageAgent'):
        actor = agent.team.acting
        agent.event_raiser = ("team", agent.team.acting)
        agent.handle_event(EAT_FOOD)

        agent.team[actor].held = Steak()
