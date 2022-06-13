import keras
import keras.layers as layers

from src.AI_core.environment import SAPGame
from src.AI_core.replay.replayers import MultiChannelReplay


class DQN:
    replay = MultiChannelReplay(20)
    env = SAPGame(replay=replay)

    def __init__(self):
        model = keras.Sequential()
        model.add(layers.Input(shape=(61,)))
        model.add(layers.Dense(40))
        model.add(layers.LeakyReLU())

        model.add(layers.Dense(30))
        model.add(layers.BatchNormalization())

        model.add(layers.Dense(30))

        model.add(layers.Dense(99))

        model.compile(jit_compile=True)


if __name__ == '__main__':
    DQN()
