from typing import Optional

import numpy as np
import tensorflow as tf

from src.AI_core.learners.DQN import DQN

_min_buffer = 50
_num_actions = 99


# TODO convert DQN to AQN
class AQN(DQN):
    def train_based_on(self, target: 'AQN') -> Optional[tf.Tensor]:
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
        adv_values_pred = s_t1_values_pred - tf.reshape(tf.reduce_max(s_t1_values_pred, axis=1), [-1, 1])
        # use discounting equation for visible reward values
        adv_values_actual = np.where(done, reward, reward + self.gamma * np.max(adv_values_pred, axis=1))

        # set loss as error of values.
        # TODO set loss to be advantage loss
        with tf.GradientTape() as recorder:
            action_values = tf.math.reduce_sum(
                    self.evaluate_forward(state) * tf.one_hot(action, _num_actions),
                    axis=1)
            loss = tf.math.reduce_mean(tf.square(adv_values_actual - action_values))

        training_variables = self.network.trainable_variables
        grads = recorder.gradient(loss, training_variables, None)
        self.optimizer.apply_gradients(zip(grads, training_variables))
        return loss


if __name__ == '__main__':
    copy_frequency = 10
    active_net = AQN()
    target_net = AQN()

    for i in range(10000):
        active_net.play_episode(target_net)
        active_net.epsilon = 0.999 * active_net.epsilon

        if i % copy_frequency == 0:
            target_net.write_weights_from(active_net)
