from Core.Overseer import MessageAgent


class Tier5:
    @staticmethod
    def chicken(agent: MessageAgent):
        if agent.lvl == 1:
            agent.shop.perm_buff(1, 1)
        elif agent.lvl == 2:
            agent.shop.perm_buff(2, 2)
        else:
            agent.shop.perm_buff(3, 3)

    # add cow's milk to shop
    @staticmethod
    def cow(agent: MessageAgent):
        # TODO
        pass

    # deal 7/14/21 damage to last enemy
    @staticmethod
    def crocodile(agent: MessageAgent):
        # TODO
        pass

    @staticmethod
    def eagle(agent: MessageAgent):
        # TODO
        pass

    # limited activation count stored in Goat object
    @staticmethod
    def goat(agent: MessageAgent):
        agent.gold += 1

    @staticmethod
    def microbe(agent: MessageAgent):
        # TODO
        pass

    @staticmethod
    def monkey(agent: MessageAgent):
        animal_to_buff = agent.team.rightmost_unit()
        if agent.lvl == 1:
            agent.buff(animal_to_buff, 2, 2)
        elif agent.lvl == 2:
            agent.buff(animal_to_buff, 4, 4)
        else:
            agent.buff(animal_to_buff, 6, 6)

    # copy ability should be stored in the parrot object
    @staticmethod
    def parrot(agent: MessageAgent):
        # TODO
        pass

    @staticmethod
    def rhino(agent: MessageAgent):
        # TODO
        pass

    @staticmethod
    def scorpion(agent: MessageAgent):
        pass

    @staticmethod
    def seal(agent: MessageAgent):
        friends = agent.team.random_friends(2)
        if agent.lvl == 1:
            agent.buff(friends, 1, 1)
        elif agent.lvl == 2:
            agent.buff(friends, 2, 2)
        else:
            agent.buff(friends, 3, 3)

    @staticmethod
    def shark(agent: MessageAgent):
        if agent.lvl == 1:
            agent.buff(agent.team.animals[agent.team.acting], 2, 1)
        elif agent.lvl == 2:
            agent.buff(agent.team.animals[agent.team.acting], 4, 2)
        else:
            agent.buff(agent.team.animals[agent.team.acting], 6, 3)

    @staticmethod
    def turkey(agent: MessageAgent):
        if agent.lvl == 1:
            agent.buff(agent.team.animals[agent.event_raiser], 3, 3)
        elif agent.lvl == 2:
            agent.buff(agent.team.animals[agent.event_raiser], 6, 6)
        else:
            agent.buff(agent.team.animals[agent.event_raiser], 9, 9)
