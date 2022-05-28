import numpy as np
from TP4.kohonen.neuron import Neuron


def get_distance(vector_1, vector_2):
    total_sum = 0
    for i in range(len(vector_1)):
        total_sum += (vector_1[i] - vector_2[i]) ** 2
    return np.sqrt(total_sum)


class Kohonen:
    def __init__(self, training_set, dimension, radius, learning_rate):
        self.training_set = np.array(training_set, dtype=float)
        self.dimension = dimension
        self.radius = radius
        self.learning_rate = learning_rate
        self.neurons = np.ndarray(dtype=Neuron, shape=(dimension, dimension))

    def initialize_weights(self):
        for i in range(self.dimension):
            for j in range(self.dimension):
                i_x = np.random.randint(0, len(self.training_set))
                chosen_w = self.training_set[i_x].copy()
                self.neurons[i][j] = Neuron(chosen_w)

    def train(self, epochs):
        activations = np.zeros(shape=(self.dimension, self.dimension))
        positions = np.arange(0, len(self.training_set))
        for i in range(epochs):
            np.random.shuffle(positions)
            radius = self.radius
            learning_rate = self.learning_rate
            for i_x in positions:
                chosen_xp = self.training_set[i_x]
                best_neuron, x, y = self.get_best_neuron(chosen_xp)
                self.update_weights_with_kohonen_rule(best_neuron, x, y, chosen_xp)
                activations[x][y] += 1
                self.radius = 1 if self.radius == 1 else self.radius - 1
                self.learning_rate = (1 / (1 + i))
            self.radius = radius
            self.learning_rate = learning_rate
        return activations

    def update_weights_with_kohonen_rule(self, best_neuron, x, y, chosen_xp):
        for i in range(self.dimension):
            for j in range(self.dimension):
                if get_distance([i, j], [x, y]) <= self.radius:
                    self.neurons[i][j].weights += self.learning_rate * (chosen_xp - self.neurons[i][j].weights)

    def get_best_neuron(self, chosen_xp):
        best_neuron = None
        best_neuron_x = 0
        best_neuron_y = 0
        min_distance = float("inf")
        for i in range(self.dimension):
            for j in range(self.dimension):
                new_distance = get_distance(self.neurons[i][j].weights, chosen_xp)
                if new_distance < min_distance:
                    min_distance = new_distance
                    best_neuron = self.neurons[i][j]
                    best_neuron_x, best_neuron_y = i, j
        return best_neuron, best_neuron_x, best_neuron_y
