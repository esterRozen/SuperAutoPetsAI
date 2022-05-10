from Core.Overseer import MessageAgent
from .Items.eventnames import *


class EventProcessor:
    # acting should be the animal that is doing something
    # event raiser should be the animal whose triggers are going off.

    ################################################################

    # engine
    # apply to unit that acted (was bought)
    @staticmethod
    def buy(agent: MessageAgent):
        operation = agent.team.animals[agent.event_raiser[1]].trigger(BUY)
        agent.trigger_ability(operation)

    # engine
    # apply to all units
    @staticmethod
    def buy_food(agent: MessageAgent):
        for animal in agent.sorted_team:
            operation = animal.trigger(BUY_FOOD)
            agent.target = ("team", agent.team.animals.index(animal))
            agent.trigger_ability(operation)

    # engine
    # apply to all units
    @staticmethod
    def buy_T1_pet(agent: MessageAgent):
        for animal in agent.sorted_team:
            operation = animal.trigger(BUY_T1_PET)
            agent.target = agent.team.animals.index(animal)
            agent.trigger_ability(operation)

    # engine
    # apply to unit that acted (ate food)
    @staticmethod
    def eat_food(agent: MessageAgent):
        for animal in agent.sorted_team:
            operation = animal.trigger(EAT_FOOD)
            agent.target = ("team", agent.team.animals.index(animal))
            agent.trigger_ability(operation)

    # engine
    # apply to all units
    @staticmethod
    def end_turn(agent: MessageAgent):
        for animal in agent.sorted_team:
            operation = animal.trigger(END_TURN)
            agent.target = ("team", agent.team.animals.index(animal))
            agent.trigger_ability(operation)

    # engine
    # apply to all units except event raiser
    @staticmethod
    def friend_bought(agent: MessageAgent):
        for animal in agent.sorted_without_raiser:
            operation = animal.trigger(FRIEND_BOUGHT)
            agent.target = agent.team.animals.index(animal)
            agent.trigger_ability(operation)

    # engine
    # apply to all units except event raiser
    @staticmethod
    def friend_eats_food(agent: MessageAgent):
        for animal in agent.sorted_without_raiser:
            operation = animal.trigger(FRIEND_EATS_FOOD)
            agent.target = ("team", agent.team.animals.index(animal))
            agent.trigger_ability(operation)

    # engine
    # apply to all units
    @staticmethod
    def friend_sold(agent: MessageAgent):
        for animal in agent.sorted_team:
            operation = animal.trigger(FRIEND_SOLD)
            agent.target = agent.team.animals.index(animal)
            agent.trigger_ability(operation)

    # engine
    # apply to units except event raiser
    @staticmethod
    def friend_summoned_shop(agent: MessageAgent):
        for animal in agent.sorted_without_raiser:
            operation = animal.trigger(FRIEND_SUMMONED_SHOP)
            agent.target = ("team", agent.team.animals.index(animal))
            agent.trigger_ability(operation)

    # engine
    # apply to unit that raised event (got sold)
    @staticmethod
    def sell(agent: MessageAgent):
        operation = agent.team.animals[agent.event_raiser[1]].trigger(SELL)
        agent.trigger_ability(operation)

    # engine
    # apply to all units
    @staticmethod
    def start_turn(agent: MessageAgent):
        for animal in agent.sorted_team:
            operation = animal.trigger(START_TURN)
            agent.target = ("team", agent.team.animals.index(animal))
            agent.trigger_ability(operation)

    ################################################################

    # engine and battle system
    # apply to units left of event raiser
    @staticmethod
    def friend_ahead_faints(agent: MessageAgent):
        for animal in agent.sorted_left_of_raiser:
            operation = animal.trigger(FRIEND_AHEAD_FAINTS)
            agent.target = ("team", agent.team.animals.index(animal))
            agent.trigger_ability(operation)

    # engine and battle system
    # apply to all units
    @staticmethod
    def friend_faints(agent: MessageAgent):
        for animal in agent.sorted_team:
            operation = animal.trigger(FRIEND_FAINTS)
            agent.target = ("team", agent.team.animals.index(animal))
            agent.trigger_ability(operation)

    # engine and battle system
    # apply to unit that raised event (got hurt)
    @staticmethod
    def hurt(agent: MessageAgent):
        operation = agent.team.animals[agent.event_raiser[1]].trigger(HURT)
        agent.trigger_ability(operation)

    # both
    # apply to event raiser
    @staticmethod
    def is_summoned(agent: MessageAgent):
        operation = agent.team.animals[agent.event_raiser[1]].trigger(IS_SUMMONED)
        agent.trigger_ability(operation)

    # engine and battle system
    # apply to unit that raised event (got knocked out)
    @staticmethod
    def on_faint(agent: MessageAgent):
        operation = agent.team.animals[agent.event_raiser[1]].trigger(ON_FAINT)
        agent.trigger_ability(operation)

    # engine and battle system
    # apply to unit that raised event (went up a level)
    @staticmethod
    def on_level(agent: MessageAgent):
        operation = agent.team.animals[agent.event_raiser[1]].trigger(ON_LEVEL)
        agent.trigger_ability(operation)

    # engine and battle system
    # handles damage system, will check for faint
    # deal damage to friendly unit
    @staticmethod
    def damage_team(damage, pos):
        pass

    ################################################################

    # triggered by battle system (which feeds message to message agent)
    # apply to unit that raised event (is about to attack)
    @staticmethod
    def before_attack(agent: MessageAgent):
        operation = agent.team.animals[agent.event_raiser[1]].trigger(BEFORE_ATTACK)
        agent.trigger_ability(operation)

    # battle system
    # apply to all units
    @staticmethod
    def enemy_attacks(agent: MessageAgent):
        for animal in agent.sorted_team:
            operation = animal.trigger(ENEMY_ATTACKS)
            agent.target = ("team", agent.team.animals.index(animal))
            agent.trigger_ability(operation)

    # battle system
    # apply to all units left of event raiser
    @staticmethod
    def friend_ahead_attacks(agent: MessageAgent):
        for animal in agent.sorted_left_of_raiser:
            operation = animal.trigger(FRIEND_AHEAD_ATTACKS)
            agent.target = ("team", animal.team.animals.index(animal))
            agent.trigger_ability(operation)

    # battle system
    # apply to units except event raiser
    @staticmethod
    def friend_summoned_battle(agent: MessageAgent):
        for animal in agent.sorted_without_raiser:
            operation = animal.trigger(FRIEND_SUMMONED_BATTLE)
            agent.target = ("team", agent.team.animals.index(animal))
            agent.trigger_ability(operation)

    # battle system
    # apply to unit acting (which knocked unit out)
    @staticmethod
    def knock_out(agent: MessageAgent):
        operation = agent.team.animals[agent.event_raiser[1]].trigger(KNOCK_OUT)
        agent.trigger_ability(operation)

    # battle system
    # apply to all units
    @staticmethod
    def start_battle(agent: MessageAgent):
        for animal in agent.sorted_team:
            operation = animal.trigger(START_BATTLE)
            agent.trigger_ability(operation)

    # battle system
    # deal damage to enemy unit
    @staticmethod
    def deal_enemy(damage, pos):
        pass