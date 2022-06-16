from src.core import Engine

__all__ = ['EngineAPI']

_limit = 50


class EngineAPI:
    loss_reward = -0.5
    win_reward = 1.0

    def __init__(self, engine: Engine):

        self.engine = engine

        self._action_lookup = {
            "sell": self.engine.sell,
            "buy": self.engine.buy,
            "reroll": self.engine.reroll,
            "end turn": self.engine.end_turn,
            "freeze": self.engine.freeze,
            "move": self.engine.move,
            "combine": self.engine.combine
        }

        self.__actions_this_turn = 0

    def action(self, *args):
        """
        Processes action state commands into engine readable commands
        Args:
            *args: arg[0] is action id
                   arg[1:] is information needed for that action

        Returns:

        """

        wins = self.engine.messenger.wins
        lives = self.engine.messenger.life

        if self.__actions_this_turn == _limit:
            self._action_lookup["end turn"]()
        else:
            self._action_lookup[args[0]](*args[1:])

        life_change = lives - self.engine.messenger.life

        reward = self.win_reward * (self.engine.messenger.wins - wins) + self.loss_reward * life_change
        done = self.engine.messenger.wins == 10

        return self.current_state(), reward, done, None

    def current_state(self):
        return self.engine.save(include_shop=True).as_array()

    def reset(self, mode: str):
        self.engine = self.engine.__class__(mode)
        return self.current_state()
