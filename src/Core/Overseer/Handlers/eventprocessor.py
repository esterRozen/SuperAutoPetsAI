from Core.Overseer import MessageAgent


class EventProcessor:
    # acting should be the animal that is doing something
    # event raiser should be the animal whose triggers are going off.

    ################################################################

    # engine
    # apply to unit that acted (was bought)
    @staticmethod
    def buy(agent: MessageAgent):
        operation = agent.team.animals[agent.event_raiser[1]].trigger("buy")
        agent.trigger_ability(operation)

    # engine
    # apply to all units
    @staticmethod
    def buy_food(agent: MessageAgent):
        for animal in agent.sorted_team:
            operation = animal.trigger("buy food")
            agent.target = agent.team.animals.index(animal)
            agent.trigger_ability(operation)

    # engine
    # apply to all units
    @staticmethod
    def buy_T1_pet(agent: MessageAgent):
        for animal in agent.sorted_team:
            operation = animal.trigger("buy t1 pet")
            agent.target = agent.team.animals.index(animal)
            agent.trigger_ability(operation)

    # engine
    # apply to unit that acted (ate food)
    @staticmethod
    def eat_food(agent: MessageAgent):
        for animal in agent.sorted_team:
            operation = animal.trigger("eat food")
            agent.target = agent.team.animals.index(animal)
            agent.trigger_ability(operation)

    # engine
    # apply to all units
    @staticmethod
    def start_turn(agent: MessageAgent):
        for animal in agent.sorted_team:
            operation = animal.trigger("start turn")
            agent.target = agent.team.animals.index(animal)
            agent.trigger_ability(operation)

    # engine
    # apply to unit that raised event (got sold)
    @staticmethod
    def sell(agent: MessageAgent):
        operation = agent.team.animals[agent.event_raiser[1]].trigger("sell")
        agent.trigger_ability(operation)

    # engine
    # apply to all units
    @staticmethod
    def end_turn(agent: MessageAgent):
        for animal in agent.sorted_team:
            operation = animal.trigger("end turn")
            agent.target = agent.team.animals.index(animal)
            agent.trigger_ability(operation)

    # engine
    # apply to all units except event raiser
    @staticmethod
    def friend_bought(agent: MessageAgent):
        for animal in agent.sorted_without_raiser:
            operation = animal.trigger("friend bought")
            agent.target = agent.team.animals.index(animal)
            agent.trigger_ability(operation)

    # engine
    # apply to all units except event raiser
    @staticmethod
    def friend_eats_food(agent: MessageAgent):
        for animal in agent.sorted_without_raiser:
            operation = animal.trigger("friend eats food")
            agent.target = agent.team.animals.index(animal)
            agent.trigger_ability(operation)

    # engine
    # apply to all units
    @staticmethod
    def friend_sold(agent: MessageAgent):
        for animal in agent.sorted_team:
            operation = animal.trigger("friend sold")
            agent.target = agent.team.animals.index(animal)
            agent.trigger_ability(operation)

    # engine
    # apply to units except event raiser
    @staticmethod
    def friend_summoned_shop(agent: MessageAgent):
        pass

    ################################################################

    # engine and battle system
    # apply to all units
    @staticmethod
    def friend_faints(agent: MessageAgent):
        pass

    # engine and battle system
    # apply to unit that raised event (got knocked out)
    @staticmethod
    def on_faint(agent: MessageAgent):
        pass

    # engine and battle system
    # apply to unit that raised event (went up a level)
    @staticmethod
    def on_level(agent: MessageAgent):
        pass

    # engine and battle system
    # apply to units left of event raiser
    @staticmethod
    def friend_ahead_faints(agent: MessageAgent):
        pass

    # engine and battle system
    # apply to unit that event (got hurt)
    @staticmethod
    def hurt(agent: MessageAgent):
        pass

    # engine and battle system
    # handles damage system, will check for faint
    # deal damage to friendly unit
    @staticmethod
    def damage_team(damage, pos):
        pass

    ################################################################

    # battle system
    # apply to all units
    @staticmethod
    def start_battle(agent: MessageAgent):
        pass

    # triggered by battle system (which feeds message to message agent)
    @staticmethod
    def before_attack(agent: MessageAgent):
        agent.handle(agent.team.rightmost_unit().trigger("before attack"))

    # battle system
    # apply to units except event raiser
    @staticmethod
    def friend_summoned_battle(agent: MessageAgent):
        pass

    # battle system
    # apply to unit acting (which knocked unit out)
    @staticmethod
    def knock_out(agent: MessageAgent):
        pass

    # battle system
    # deal damage to enemy unit
    @staticmethod
    def deal_enemy(damage, pos):
        pass
