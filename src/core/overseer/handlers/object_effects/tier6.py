from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ... import MessageAgent


class Tier6:
    @staticmethod
    def boar(agent: 'MessageAgent'):
        # TODO
        pass

    # not 100% sure how to implement cat.
    @staticmethod
    def cat(agent: 'MessageAgent'):
        # TODO
        pass

    @staticmethod
    def dragon(agent: 'MessageAgent'):
        if agent.lvl == 1:
            agent.buff(agent.team.friends(), 1, 1)
        elif agent.lvl == 2:
            agent.buff(agent.team.friends(), 2, 2)
        else:
            agent.buff(agent.team.friends(), 2, 2)

    @staticmethod
    def fly(agent: 'MessageAgent'):
        # TODO
        pass

    @staticmethod
    def gorilla(agent: 'MessageAgent'):
        # TODO
        pass

    @staticmethod
    def leopard(agent: 'MessageAgent'):
        # TODO
        pass

    @staticmethod
    def mammoth(agent: 'MessageAgent'):
        if agent.lvl == 1:
            agent.buff(agent.team.friends(), 2, 2)
        elif agent.lvl == 2:
            agent.buff(agent.team.friends(), 4, 4)
        else:
            agent.buff(agent.team.friends(), 6, 6)

    @staticmethod
    def octopus(agent: 'MessageAgent'):
        # TODO
        pass

    @staticmethod
    def sauropod(agent: 'MessageAgent'):
        agent.gold += 1

    @staticmethod
    def snake(agent: 'MessageAgent'):
        # TODO
        pass

    # how to do this??
    @staticmethod
    def tiger(agent: 'MessageAgent'):
        # TODO
        pass

    @staticmethod
    def tyrannosaurus(agent: 'MessageAgent'):
        if agent.gold < 3:
            return
        if agent.lvl == 1:
            agent.buff(agent.team.friends(), 2, 2)
        elif agent.lvl == 2:
            agent.buff(agent.team.friends(), 4, 4)
        else:
            agent.buff(agent.team.friends(), 6, 6)
