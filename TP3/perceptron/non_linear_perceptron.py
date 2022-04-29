from TP3.perceptron.perceptron import Perceptron
import numpy as np


class NonLinearPerceptron(Perceptron):

    def __init__(self, training_set, expected_output, learning_rate):
        super().__init__(training_set, expected_output, learning_rate)

    def activation(self, excitation):
        return np.tanh(excitation)

    def error(self, w):
        error = 0
        for i in range(len(self.training_set)):
            excitation = np.inner(self.training_set[i], w)
            error += (self.expected_output[i] - self.activation(excitation)) ** 2
        return 0.5 * error

    def activation_derivative(self, excitation):
        return 1 - np.tanh(excitation)**2

