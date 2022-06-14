import keras
import keras.layers as layers
import numpy as np
import tensorflow as tf

from src.AI_core.environment import SAPGame
from src.AI_core.replay.replayers import MultiChannelReplay

_min_buffer = 50
_num_actions = 99


class DQN:
    replay = MultiChannelReplay(20)
    env = SAPGame()
    gamma = 0.95
    epsilon = 0.04

    def __init__(self):
        model = keras.Sequential()
        model.add(layers.Input(shape=(61,)))
        model.add(layers.Dense(40))
        model.add(layers.BatchNormalization())

        model.add(layers.Dense(30))
        model.add(layers.BatchNormalization())
        model.add(layers.LeakyReLU())

        model.add(layers.Dense(30))
        model.add(layers.BatchNormalization())

        model.add(layers.Dense(_num_actions))
        model.add(layers.BatchNormalization())

        model.compile(jit_compile=True)

        self.network = model
        self.optimizer = tf.optimizers.Adagrad()

    def actions(self, observations):
        return np.argmax(self.evaluate_forward(observations))

    def act(self, observations):
        for observation in observations:
            pass

    def evaluate_forward(self, inputs):
        return self.network(inputs)

    def train(self, target: 'DQN'):
        # if self.replay.__len__() < _min_buffer:
        #     return

        experiences = self.replay.sample_processed(32)
        state = experiences.state
        action = experiences.action
        reward = experiences.reward
        next_state = experiences.next_state
        done = experiences.done

        s_t1_values_pred = target.evaluate_forward(next_state)
        s_t1_values_actual = np.where(done, reward, reward + self.gamma * np.max(s_t1_values_pred, axis=1))

        with tf.GradientTape as recorder:
            action_values = tf.math.reduce_sum(
                self.evaluate_forward(state) * tf.one_hot(action, _num_actions),
                axis=1)
            loss = tf.math.reduce_mean(tf.square(s_t1_values_actual - action_values))

        training_variables = self.network.trainable_variables
        grads = recorder.gradient(loss, training_variables, None)
        self.optimizer.apply_gradients(zip(grads, training_variables))
        return loss


if __name__ == '__main__':
    active = DQN()
    target = DQN()

    active.train(target)
