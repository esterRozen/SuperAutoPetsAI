from typing import TYPE_CHECKING, Tuple

from ...eventnames import *

if TYPE_CHECKING:
    from .. import MessageAgent


def maintain_actors(func):
    def wrapped_func(*args, **kwargs):
        actor_init = args[0].event_raiser
        target_init = args[0].target
        func(*args, **kwargs)
        args[0].event_raiser = actor_init
        args[0].target = target_init

    return wrapped_func


def get_roster(agent: 'MessageAgent', actor: Tuple[str, int]):
    if actor[0] == "team":
        roster = agent.team
    elif actor[0] == "enemy":
        roster = agent.enemy
    else:
        raise ValueError(f"Invalid team type {actor[0]}")
    return roster


@maintain_actors
def for_sorted_trigger(agent: 'MessageAgent', event: str, team: str = "team"):
    roster = get_roster(agent, (team, 0))
    animals = agent.sorted_team(team)

    for animal in animals:
        actor = roster.animals.index(animal)
        roster.acting = actor
        agent.event_raiser = (team, actor)

        operation = animal.trigger(event)
        agent.trigger_ability(operation)


@maintain_actors
def for_sorted_both_trigger(agent: 'MessageAgent', event: str):
    animals = agent.sorted_team("both")

    for animal in animals:
        if animal in agent.team.animals:
            agent.team.acting = agent.team.animals.index(animal)
            agent.event_raiser = ("team", agent.team.acting)
        elif animal in agent.enemy.animals:
            agent.enemy.acting = agent.enemy.animals.index(animal)
            agent.event_raiser = ("enemy", agent.enemy.acting)
        else:
            raise ValueError(f"{animal} not present in either team")
        operation = animal.trigger(event)
        agent.trigger_ability(operation)


@maintain_actors
def for_sorted_without_actor_trigger_(agent: 'MessageAgent', actor: Tuple[str, int], event: str):
    roster = get_roster(agent, actor)
    animals = agent.sorted_without_(actor)
    team = actor[0]

    for animal in animals:
        actor = roster.animals.index(animal)
        roster.acting = actor
        agent.event_raiser = (team, actor)

        operation = animal.trigger(event)
        agent.trigger_ability(operation)


@maintain_actors
def for_sorted_behind_(agent: 'MessageAgent', actor: Tuple[str, int], event: str):
    roster = get_roster(agent, actor)
    animals = agent.sorted_units_behind_(actor)
    team = actor[0]

    for animal in animals:
        actor = roster.animals.index(animal)
        roster.acting = actor
        agent.event_raiser = (team, actor)

        operation = animal.trigger(event)
        agent.trigger_ability(operation)


@maintain_actors
def trigger_actor_ability(agent: 'MessageAgent', actor: Tuple[str, int], event: str):
    team = get_roster(agent, actor)
    team.acting = actor[1]
    agent.event_raiser = actor
    operation = team.animals[actor[1]].trigger(event)
    agent.trigger_ability(operation)


class EventProcessor:
    # distributes event calls out to all relevant units, in the desired order

    # acting should be the animal that is doing something!!
    # event raiser should be the animal whose triggers are going off.

    ################################################################

    # shop
    # apply to unit that acted (was bought)
    @staticmethod
    def buy(agent: 'MessageAgent', actor: Tuple[str, int]):
        trigger_actor_ability(agent, actor, BUY)

    # shop
    # apply to all units
    @staticmethod
    def buy_food(agent: 'MessageAgent'):
        for_sorted_trigger(agent, BUY_FOOD)

    # shop
    # apply to all units
    @staticmethod
    def buy_t1_pet(agent: 'MessageAgent'):
        for_sorted_trigger(agent, BUY_T1_PET)

    # engine
    # apply to unit that acted (ate food)
    @staticmethod
    def eat_food(agent: 'MessageAgent', actor: Tuple[str, int]):
        trigger_actor_ability(agent, actor, EAT_FOOD)

    # shop
    # apply to all units
    @staticmethod
    def end_turn(agent: 'MessageAgent'):
        for_sorted_trigger(agent, END_TURN)

    # shop
    # apply to all units except event raiser
    @staticmethod
    def friend_bought(agent: 'MessageAgent', actor: Tuple[str, int]):
        for_sorted_without_actor_trigger_(agent, actor, FRIEND_BOUGHT)

    # shop
    # apply to all units except event raiser
    @staticmethod
    def friend_eats_food(agent: 'MessageAgent', actor: Tuple[str, int]):
        for_sorted_without_actor_trigger_(agent, actor, FRIEND_EATS_FOOD)

    # shop
    # apply to all units except event raiser
    @staticmethod
    def friend_sold(agent: 'MessageAgent', actor: Tuple[str, int]):
        for_sorted_without_actor_trigger_(agent, actor, FRIEND_SOLD)

    # shop
    # apply to units except event raiser
    @staticmethod
    def friend_summoned_shop(agent: 'MessageAgent', actor: Tuple[str, int]):
        for_sorted_without_actor_trigger_(agent, actor, FRIEND_SUMMONED_SHOP)

    # shop
    # apply to unit that raised event (got sold)
    @staticmethod
    def sell(agent: 'MessageAgent', actor: Tuple[str, int]):
        trigger_actor_ability(agent, actor, SELL)

    # shop
    # apply to all units
    @staticmethod
    def start_turn(agent: 'MessageAgent'):
        for_sorted_trigger(agent, START_TURN)

    ################################################################

    # shop and battle system
    # apply to friendly units right of event raiser
    @staticmethod
    def friend_ahead_faints(agent: 'MessageAgent', actor: Tuple[str, int]):
        for_sorted_behind_(agent, actor, FRIEND_AHEAD_FAINTS)

    # shop and battle system
    # apply to all friendly units
    @staticmethod
    def friend_faints(agent: 'MessageAgent', actor: Tuple[str, int]):
        for_sorted_trigger(agent, FRIEND_FAINTS, actor[0])

    # shop and battle system
    # apply to unit that raised event (got hurt)
    @staticmethod
    def hurt(agent: 'MessageAgent', actor: Tuple[str, int]):
        trigger_actor_ability(agent, actor, HURT)

    # both
    # apply to unit that raised event (was summoned)
    @staticmethod
    def is_summoned(agent: 'MessageAgent', actor: Tuple[str, int]):
        trigger_actor_ability(agent, actor, IS_SUMMONED)

    # shop and battle system
    # apply to unit that raised event (got knocked out)
    @staticmethod
    def on_faint(agent: 'MessageAgent', actor: Tuple[str, int]):
        trigger_actor_ability(agent, actor, ON_FAINT)

    # shop and battle system
    # apply to unit that raised event (went up a level)
    @staticmethod
    def on_level(agent: 'MessageAgent', actor: Tuple[str, int]):
        trigger_actor_ability(agent, actor, ON_LEVEL)

    ################################################################

    # triggered by battle system (which feeds message to message agent)
    # apply to unit that raised event (is about to attack)
    @staticmethod
    def before_attack(agent: 'MessageAgent', actor: Tuple[str, int]):
        trigger_actor_ability(agent, actor, BEFORE_ATTACK)

    # battle system
    # apply to all friendly units
    @staticmethod
    def enemy_attacks(agent: 'MessageAgent', actor: Tuple[str, int]):
        for_sorted_trigger(agent, ENEMY_ATTACKS, actor[0])

    # battle system
    # apply to all friendly units left of event raiser
    @staticmethod
    def friend_ahead_attacks(agent: 'MessageAgent', actor: Tuple[str, int]):
        for_sorted_behind_(agent, actor, FRIEND_AHEAD_ATTACKS)

    # battle system
    # apply to all friendly units except event raiser
    @staticmethod
    def friend_summoned_battle(agent: 'MessageAgent', actor: Tuple[str, int]):
        for_sorted_without_actor_trigger_(agent, actor, FRIEND_SUMMONED_BATTLE)

    # battle system
    # apply to unit acting (which knocked unit out)
    @staticmethod
    def knock_out(agent: 'MessageAgent', actor: Tuple[str, int]):
        trigger_actor_ability(agent, actor, KNOCK_OUT)

    # battle system
    # apply to all units on both teams
    @staticmethod
    def start_battle(agent: 'MessageAgent'):
        for_sorted_both_trigger(agent, START_BATTLE)
