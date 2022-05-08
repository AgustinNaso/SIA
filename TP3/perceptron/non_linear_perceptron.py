from TP3.perceptron.perceptron import Perceptron
import numpy as np


class NonLinearPerceptron(Perceptron):

    def __init__(self, training_set, expected_output, learning_rate):
        super().__init__(training_set, expected_output, learning_rate)
        self.max_value = max(expected_output)
        self.min_value = min(expected_output)

    def activation(self, excitation):
        return np.tanh(excitation)

    def error(self, w):
        error = 0
        for i in range(len(self.training_set)):
            excitation = np.inner(self.training_set[i], w)
            # error += (self.expected_output[i] - self.activation(excitation)) ** 2
            error += (self.scale_tanh(self.expected_output[i]) - self.scale_tanh(self.activation(excitation))) ** 2
        return 0.5 * error

    def activation_derivative(self, excitation):
        return 1 - np.tanh(excitation) ** 2

    def scale_tanh(self, value):
        return (((value + 1) / 2) * (self.max_value - self.min_value)) + self.min_value
