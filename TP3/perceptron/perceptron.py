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

    # Training algorithm
    def train(self, epochs):
        i = 0
        error = 1
        p = len(self.training_set)
        self.error_min = float('inf')
        w = np.random.rand(len(self.training_set[0]))
        print(w)
        positions = np.arange(0, len(self.training_set))
        print(positions)
        while error > 0 and i < epochs:
            np.random.shuffle(positions)
            for i_x in positions:
                print(f' ix: {i_x}')
                excitation = np.inner(self.training_set[i_x], w)
                activation = self.activation(excitation)
                w += self.learning_rate * (self.expected_output[i_x] - activation) * self.training_set[i_x] * self.activation_derivative(excitation)
                print(w)
                error = self.error(w)
                if error < self.error_min:
                    self.error_min = error
                    self.w_min = w
            i += 1
            print("Minimum error: " + str(self.error_min))
            print("Minimum weight: " + str(self.w_min))
            w = self.w_min
            x = np.linspace(-2, 2, 100)
            y = -(w[0]*x/w[1]) - w[2]/w[1] 
            plt.title(f'Variacion de vector w con η = {self.learning_rate}, epoca= {i}')
            plt.xlabel('ξ_1')
            plt.ylabel('ξ_2')
            plt.plot(x, y, label='line', linewidth=2)
            plt.plot(-1,-1, 'o', c='black', markersize=DOT_SIZE)
            plt.plot(-1,1, 'go', markersize=DOT_SIZE)
            plt.plot(1,-1, 'go', markersize=DOT_SIZE)
            plt.plot(1,1, 'o', c='black', markersize=DOT_SIZE)
            plt.ylim(-2,2)
            plt.savefig(f'plots/{i}')
            plt.clf()
           

    def plot(self):
        print(self.training_set)

    def test_input(self, test_set):
        real_input = np.array(list(map(lambda t: np.append(t, [1]), test_set)), dtype=float)
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
