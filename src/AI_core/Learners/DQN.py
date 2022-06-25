import random as rand
from typing import Optional

import keras
import keras.layers as layers
import numpy as np
import tensorflow as tf

from src.AI_core.environment import SAPGame
from src.AI_core.replay.replayers import Transition, ReplayMemory

_min_buffer = 50
_num_actions = 99


class DQN:
    replay = ReplayMemory()
    env = SAPGame()
    gamma = 0.95
    epsilon = 0.1

    def __init__(self):
        model = keras.Sequential()
        model.add(layers.Input(shape=(76,)))
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

    def write_weights_from(self, network_manager: 'DQN'):
        main = self.network.trainable_variables
        other = network_manager.network.trainable_variables
        for (main_var, other_var) in zip(main, other):
            main_var.assign(other_var.numpy())

    def action(self, observation):
        if rand.random() < self.epsilon:
            return rand.randrange(0, _num_actions)
        return np.argmax(self.evaluate_forward(observation))

    def act(self, state, prev_reward):
        action = self.action(state)
        next_state, reward, done, info = self.env.step(action)
        transition = Transition(state, action, prev_reward + reward, next_state, done)
        self.replay.push(transition)
        return transition

    def play_episode(self, target: 'DQN', mode: Optional[str] = None):
        done = False
        options = {"mode": mode}
        state = self.env.reset(options=options)
        sum_reward = 0
        loss_list = []
        while not done:
            transition = self.act(state, sum_reward)
            state = transition.next_state
            done = transition.done
            sum_reward = transition.reward

            loss = self.train_based_on(target)
            if loss is not None:
                loss_list.append(loss)

        return sum_reward, sum(loss_list) / len(loss_list)

    def evaluate_forward(self, inputs):
        return self.network(inputs)

    def train_based_on(self, target: 'DQN') -> Optional[tf.Tensor]:
        if self.replay.__len__() < _min_buffer:
            return None

        # 32 batch
        experiences = self.replay.sample_processed(32)
        # easy unpacking
        state = experiences.state
        action = experiences.action
        reward = experiences.reward
        next_state = experiences.next_state
        done = experiences.done

        s_t1_values_pred = target.evaluate_forward(next_state)
        # use discounting equation for visible reward values
        s_t1_values_actual = np.where(done, reward, reward + self.gamma * np.max(s_t1_values_pred, axis=1))

        # set loss as error of values.
        with tf.GradientTape() as recorder:
            action_values = tf.math.reduce_sum(
                self.evaluate_forward(state) * tf.one_hot(action, _num_actions),
                axis=1)
            loss = tf.math.reduce_mean(tf.square(s_t1_values_actual - action_values))

        training_variables = self.network.trainable_variables
        grads = recorder.gradient(loss, training_variables, None)
        self.optimizer.apply_gradients(zip(grads, training_variables))
        return loss


if __name__ == '__main__':
    copy_frequency = 10
    active_net = DQN()
    target_net = DQN()

    for i in range(10000):
        active_net.play_episode(target_net)
        active_net.epsilon = 0.999 * active_net.epsilon

        if i % copy_frequency == 0:
            target_net.write_weights_from(active_net)
