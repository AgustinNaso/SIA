from abc import ABC, abstractmethod
import numpy as np
import constants


class Perceptron(ABC):

    def __init__(self, training_set, expected_output, learning_rate):
        self.training_set = training_set
        self.expected_output = expected_output
        self.learning_rate = learning_rate
        self.error_min = None
        self.w_min = None

    # Training algorithm
    def train(self, iterations):
        i = 0
        error = 1
        p = len(self.training_set)
        self.error_min = float('inf')
        w = np.zeros(len(self.training_set[0]), dtype=float)
        while error > 0 and i < iterations:
            i_x = np.random.randint(1, p)
            excitation = np.inner(self.training_set[i_x], w) + constants.BIAS
            activation = self.activation(excitation)
            w += self.learning_rate * (self.expected_output[i_x] - activation) * self.training_set[i_x] * self.activation_derivative(excitation)
            error = self.error(w)
            if error < self.error_min:
                self.error_min = error
                self.w_min = w
            i += 1

    def get_results(self, test_input):
        results = []
        for i in range(len(test_input)):
            excitation = np.inner(test_input[i], self.w_min) + constants.BIAS
            results.append(self.activation(excitation))
        return results

    @abstractmethod
    def activation(self, excitation):
        pass

    @abstractmethod
    def error(self, w):
        pass

    def activation_derivative(self, excitation):
        return 1
