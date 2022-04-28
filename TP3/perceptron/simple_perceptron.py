from TP3.perceptron.perceptron import Perceptron
import numpy as np


class SimplePerceptron(Perceptron):

    def __init__(self, training_set, expected_output, learning_rate):
        super().__init__(training_set, expected_output, learning_rate)

    def activation(self, excitation):
        return 1 if excitation >= 0 else -1

    def error(self, w):
        error = 0
        for i in range(len(self.training_set)):
            excitation = np.inner(self.training_set[i], w)
            error += abs(self.expected_output[i] - self.activation(excitation))
        return error
