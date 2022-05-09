from perceptron.perceptron import Perceptron
import numpy as np


class LinearPerceptron(Perceptron):

    def __init__(self, training_set, expected_output, learning_rate):
        super().__init__(training_set, expected_output, learning_rate)

    def activation(self, excitation):
        return excitation

    def error(self, w):
        error = 0
        for i in range(len(self.training_set)):
            excitation = np.inner(self.training_set[i], w)
            error += (self.expected_output[i] - excitation) ** 2
        return 0.5 * error
