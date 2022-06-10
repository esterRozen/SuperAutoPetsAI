from typing import TYPE_CHECKING, Tuple

from ... import eventnames
from ...game_elements.abstract_elements import Animal

if TYPE_CHECKING:
    from .. import MessageAgent


def get_roster(agent: 'MessageAgent', actor: Tuple[str, int]):
    if actor[0] == "team":
        roster = agent.team
    elif actor[0] == "enemy":
        roster = agent.enemy
    else:
        raise ValueError(f"Invalid team type {actor[0]}")
    return roster


def for_sorted_both_trigger(agent: 'MessageAgent', event: str):
    animals = agent.sorted_team("both")

    animal_order = []
    for animal in animals:
        if animal in agent.team.animals:
            animal_order.append(
                ("team", agent.team.animals.index(animal), animal)
            )
        elif animal in agent.enemy.animals:
            animal_order.append(
                ("enemy", agent.enemy.animals.index(animal), animal)
            )
        else:
            raise ValueError(f"{animal} not present in either team")

    for team, pos, animal in animal_order:
        actor = ("team", pos)
        operation = animal.trigger(event)
        agent.trigger_ability(operation, actor, actor, animal)

        operation = animal.held.trigger(event)
        agent.trigger_ability(operation, actor, actor, animal)


def for_sorted_trigger(agent: 'MessageAgent', event: str, team: str = "team", fainted: Animal = None):
    roster = get_roster(agent, (team, 0))
    animals = agent.sorted_team(team)

    for animal in animals:
        idx = roster.animals.index(animal)
        actor = (team, idx)

        operation = animal.trigger(event)
        agent.trigger_ability(operation, actor, actor, fainted)

        operation = animal.held.trigger(event)
        agent.trigger_ability(operation, actor, actor, fainted)


def for_sorted_without_actor_trigger_(agent: 'MessageAgent', position: Tuple[str, int], event: str,
                                      fainted: Animal = None):
    roster = get_roster(agent, position)
    animals = agent.sorted_without_(position)
    team = position[0]

    target = position

    for animal in animals:
        position = roster.animals.index(animal)

        operation = animal.trigger(event)
        agent.trigger_ability(operation, (team, position), target, fainted)

        operation = animal.held.trigger(event)
        agent.trigger_ability(operation, (team, position), target, fainted)


def trigger_actor_ability(agent: 'MessageAgent', actor: Tuple[str, int], event: str, fainted_actor: Animal = None):
    if fainted_actor is None:
        animal = get_roster(agent, actor)[actor[1]]
    else:
        animal = fainted_actor

    operation = animal.trigger(event)
    agent.trigger_ability(operation, actor, actor, fainted_actor)

    operation = animal.held.trigger(event)
    agent.trigger_ability(operation, actor, actor, fainted_actor)


class EventProcessor:
    # distributes event calls out to all relevant units, in the desired order

    # acting should be the animal that is doing something!!
    # event raiser should be the animal whose triggers are going off.

    ################################################################

    # shop
    # apply to unit that acted (was bought)
    @staticmethod
    def buy(agent: 'MessageAgent', actor: Tuple[str, int]):
        trigger_actor_ability(agent, actor, eventnames.BUY)

    # shop
    # apply to all units
    @staticmethod
    def buy_food(agent: 'MessageAgent'):
        for_sorted_trigger(agent, eventnames.BUY_FOOD)

    # shop
    # apply to all units
    @staticmethod
    def buy_t1_pet(agent: 'MessageAgent'):
        for_sorted_trigger(agent, eventnames.BUY_T1_PET)

    # engine
    # apply to unit that acted (ate food)
    @staticmethod
    def eat_food(agent: 'MessageAgent', actor: Tuple[str, int]):
        trigger_actor_ability(agent, actor, eventnames.EAT_FOOD)

    # shop
    # apply to all units
    @staticmethod
    def end_turn(agent: 'MessageAgent'):
        for_sorted_trigger(agent, eventnames.END_TURN)

    # shop
    # apply to all units except event raiser
    @staticmethod
    def friend_bought(agent: 'MessageAgent', actor: Tuple[str, int]):
        for_sorted_without_actor_trigger_(agent, actor, eventnames.FRIEND_BOUGHT)

    # shop
    # apply to all units except event raiser
    @staticmethod
    def friend_eats_food(agent: 'MessageAgent', actor: Tuple[str, int]):
        for_sorted_without_actor_trigger_(agent, actor, eventnames.FRIEND_EATS_FOOD)

    # shop
    # apply to all units except event raiser
    @staticmethod
    def friend_sold(agent: 'MessageAgent', actor: Tuple[str, int]):
        for_sorted_trigger(agent, eventnames.FRIEND_SOLD)

    # shop
    # apply to units except event raiser
    @staticmethod
    def friend_summoned_shop(agent: 'MessageAgent', actor: Tuple[str, int]):
        for_sorted_without_actor_trigger_(agent, actor, eventnames.FRIEND_SUMMONED_SHOP)

    # shop
    # apply to unit that raised event (got sold)
    @staticmethod
    def sell(agent: 'MessageAgent', actor: Tuple[str, int]):
        trigger_actor_ability(agent, actor, eventnames.SELL)

    # shop
    # apply to all units
    @staticmethod
    def start_turn(agent: 'MessageAgent'):
        for_sorted_trigger(agent, eventnames.START_TURN)

    ################################################################

    # shop and battle system
    # apply to friendly units right of event raiser
    @staticmethod
    def friend_ahead_faints(agent: 'MessageAgent', actor: Tuple[str, int]):
        team = get_roster(agent, actor)
        animal_behind = (actor[0], team.animals.index(team.friend_behind(actor[1])))

        trigger_actor_ability(agent, animal_behind, eventnames.FRIEND_AHEAD_FAINTS)

    # shop and battle system
    # apply to all friendly units
    @staticmethod
    def friend_faints(agent: 'MessageAgent', actor: Tuple[str, int], fainted: Animal):
        for_sorted_trigger(agent, eventnames.FRIEND_FAINTS, actor[0], fainted)

    # shop and battle system
    # apply to unit that raised event (got hurt)
    @staticmethod
    def hurt(agent: 'MessageAgent', actor: Tuple[str, int]):
        trigger_actor_ability(agent, actor, eventnames.HURT)

    # both
    # apply to unit that raised event (was summoned)
    @staticmethod
    def is_summoned(agent: 'MessageAgent', actor: Tuple[str, int]):
        trigger_actor_ability(agent, actor, eventnames.IS_SUMMONED)

    # shop and battle system
    # apply to unit that raised event (got knocked out)
    @staticmethod
    def on_faint(agent: 'MessageAgent', actor: Tuple[str, int], fainted: Animal):
        trigger_actor_ability(agent, actor, eventnames.ON_FAINT, fainted)

    # shop and battle system
    # apply to unit that raised event (went up a level)
    @staticmethod
    def on_level(agent: 'MessageAgent', actor: Tuple[str, int]):
        trigger_actor_ability(agent, actor, eventnames.ON_LEVEL)

    ################################################################

    # triggered by battle system (which feeds message to message agent)
    # apply to unit that raised event (is about to attack)
    @staticmethod
    def before_attack(agent: 'MessageAgent', actor: Tuple[str, int]):
        trigger_actor_ability(agent, actor, eventnames.BEFORE_ATTACK)

    # battle system
    # apply to friendly units
    @staticmethod
    def battle_end(agent: 'MessageAgent'):
        for_sorted_trigger(agent, eventnames.BATTLE_END)

    # battle system
    # apply to all units
    @staticmethod
    def before_battle(agent: 'MessageAgent'):
        for_sorted_both_trigger(agent, eventnames.BEFORE_BATTLE)

    # battle system
    # apply to all friendly units left of event raiser
    @staticmethod
    def friend_ahead_attacks(agent: 'MessageAgent', actor: Tuple[str, int]):
        team = get_roster(agent, actor)
        animal_behind = (actor[0], team.animals.index(team.friend_behind(actor[1])))

        trigger_actor_ability(agent, animal_behind, eventnames.FRIEND_AHEAD_ATTACKS)

    # battle system
    # apply to all friendly units except event raiser
    @staticmethod
    def friend_summoned_battle(agent: 'MessageAgent', actor: Tuple[str, int]):
        for_sorted_without_actor_trigger_(agent, actor, eventnames.FRIEND_SUMMONED_BATTLE)

    # battle system
    # apply to unit acting (which knocked unit out)
    @staticmethod
    def knock_out(agent: 'MessageAgent', actor: Tuple[str, int]):
        trigger_actor_ability(agent, actor, eventnames.KNOCK_OUT)

    # battle system
    # apply to all units on both teams
    @staticmethod
    def start_battle(agent: 'MessageAgent'):
        for_sorted_both_trigger(agent, eventnames.START_BATTLE)
