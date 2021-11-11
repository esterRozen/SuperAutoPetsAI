from Core.Overseer.Handlers.Triggers import Triggers


# handles dealing damage to team members and opponents
# and calling the corresponding effects
class DamageEffects(Triggers):
    def __init__(self, mode):
        super(DamageEffects, self).__init__(mode)
