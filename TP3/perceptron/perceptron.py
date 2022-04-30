from random import shuffle
from select import epoll
import time
from abc import ABC, abstractmethod
from unittest import result
import numpy as np
import matplotlib.pyplot as plt
DOT_SIZE = 5


class Perceptron(ABC):

    def shuffle_training_set(self,training_set, outputs):
        for i in range(len(training_set)):
            rand1 = np.random.randint(low=0, high=len(training_set) - 1)
            aux = training_set[i]
            training_set[i] = training_set[rand1]
            training_set[rand1] = aux
            aux = outputs[i]
            outputs[i] = outputs[rand1]
            outputs[rand1] = aux
            

    def __init__(self, training_set, expected_output, learning_rate):
        self.training_set = np.array(list(map(lambda t: np.append(t, [1]), training_set)), dtype=float)
        self.expected_output = expected_output
        self.learning_rate = learning_rate
        self.error_min = None
        self.w_min = None

    # Training algorithm
    def train(self, iterations):
        accuracy = np.zeros(iterations)
        i = 0
        error = 1
        p = len(self.training_set)
        self.error_min = float('inf')
        w = np.zeros(len(self.training_set[0]))
        for j in range(len(self.training_set[0])):
            w[j] = np.random.uniform(low=-1, high=1)
        index_vector = np.arange(len(self.training_set[0]))
        print(index_vector)
        print(f'post: {index_vector}')
        epoch = 1
        while error > 0 and epoch < iterations:
            np.random.shuffle(index_vector)
            self.error_min = float('inf')
            error = 1
            for j in index_vector:
                excitation = np.dot(self.training_set[j], w)
                activation = self.activation(excitation)
                d_w = self.learning_rate * (self.expected_output[j] - activation) * self.training_set[j] * self.activation_derivative(excitation)
                print(f'w {w}')
                print(f'd_w {d_w}')
                w+=d_w
                error = self.error(w)
                if error < self.error_min:
                    self.error_min = error
                    self.w_min = w
                i += 1
            print(f"Minimum error {epoch}: " + str(self.error_min))
            print(f"Minimum weight {epoch}: " + str(self.w_min))
            w = self.w_min
            x = np.linspace(-2, 2, 100)
            y = -(w[0]*x/w[1]) - w[2]/w[1] 
            plt.title(f'Variacion de vector w con η = {self.learning_rate}, epoch= {epoch}')
            plt.xlabel('ξ_1')
            plt.ylabel('ξ_2')
            plt.plot(x, y, label='line', linewidth=2)
            plt.plot(-1,-1, 'o', c='black', markersize=DOT_SIZE)
            plt.plot(-1,1, 'go', markersize=DOT_SIZE)
            plt.plot(1,-1, 'go', markersize=DOT_SIZE)
            plt.plot(1,1, 'o', c='black', markersize=DOT_SIZE)
            plt.ylim(-2,2)
            plt.savefig(f'plots/{epoch}.png')
            plt.clf()
            epoch+=1

        #     print(i)
        # w = self.w_min
        # x = np.linspace(-2, 2, 100)
        # y = -(w[0]*x/w[1]) - w[2]/w[1] 
        # plt.title(f'Variacion de vector w con η = {self.learning_rate}, iteracion= {i}')
        # plt.xlabel('ξ_1')
        # plt.ylabel('ξ_2')
        # plt.plot(x, y, label='line', linewidth=2)
        # plt.plot(-1,-1, 'o', c='black', markersize=DOT_SIZE)
        # plt.plot(-1,1, 'go', markersize=DOT_SIZE)
        # plt.plot(1,-1, 'go', markersize=DOT_SIZE)
        # plt.plot(1,1, 'o', c='black', markersize=DOT_SIZE)
        # plt.ylim(-2,2)
        # plt.savefig(f'plots/{i}')
        # plt.clf()
           

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
