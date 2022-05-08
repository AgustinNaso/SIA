import time
from abc import ABC, abstractmethod
import numpy as np
import matplotlib.pyplot as plt

DOT_SIZE = 5


class Perceptron(ABC):

    def __init__(self, training_set, expected_output, learning_rate):
        self.training_set = np.array(list(map(lambda t: np.append(t, [1]), training_set)), dtype=float)
        self.expected_output = expected_output
        self.learning_rate = learning_rate
        self.error_min = None
        self.w_min = None
        self.results = []
        self.results_train = []
        self.errors = []

    # Training algorithm
    def train(self, epochs, test_set=None):
        i = 0
        error = 1
        p = len(self.training_set)
        self.error_min = float('inf')
        w = np.random.rand(len(self.training_set[0]))
        positions = np.arange(0, len(self.training_set))

        while error > 0 and i < epochs:
            np.random.shuffle(positions)
            for i_x in positions:

                excitation = np.inner(self.training_set[i_x], w)
                activation = self.activation(excitation)
                w += self.learning_rate * (self.expected_output[i_x] - activation) * self.training_set[
                    i_x] * self.activation_derivative(excitation)

                error = self.error(w)

                if error < self.error_min:
                    self.error_min = error
                    self.w_min = w

            if test_set:
                self.errors.append(self.error_min)
                self.results.append(self.test_input(test_set))
                self.results_train.append(self.test_input(self.training_set, True))
                self.error_min = float('inf')

            i += 1

    def plot(self):
        print(self.training_set)

    def test_input(self, test_set, training=False):
        if not training:
            real_input = np.array(list(map(lambda t: np.append(t, [1]), test_set)), dtype=float)
        else:
            real_input = test_set
        results = []
        for i in range(len(test_set)):
            excitation = np.inner(real_input[i], self.w_min)
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
