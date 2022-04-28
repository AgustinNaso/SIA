import time
from abc import ABC, abstractmethod
import numpy as np
import constants
import matplotlib.pyplot as plt

class Perceptron(ABC):

    def __init__(self, training_set, expected_output, learning_rate):
        self.training_set = np.array(list(map(lambda t: np.append(t, [1]), training_set)), dtype=float)
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
        while error > 0.001 and i < iterations:
            i_x = np.random.randint(1, p)
            excitation = np.inner(self.training_set[i_x], w)
            activation = self.activation(excitation)
            w += self.learning_rate * (self.expected_output[i_x] - activation) * self.training_set[i_x] * self.activation_derivative(excitation)
            error = self.error(w)
            if error < self.error_min:
                self.error_min = error
                self.w_min = w
            i += 1
        print("Minimum error: " + str(self.error_min))
        print("Minimum weight: " + str(self.w_min))

    def plot(self):
        print(self.training_set)

    def test_input(self, test_set):
        real_input = np.array(list(map(lambda t: np.append(t, [1]), test_set)), dtype=float)
        results = []
        for i in range(len(test_set)):
            excitation = np.inner(real_input[i], self.w_min)
            results.append(self.activation(excitation))
        return results

    def getPointOverlineResult(self, weights, x):
        return -(weights[0] / weights[1]) * x - weights[2] / weights[1]

    @abstractmethod
    def activation(self, excitation):
        pass

    @abstractmethod
    def error(self, w):
        pass

    def activation_derivative(self, excitation):
        return 1
