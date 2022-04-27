import numpy as np


class MultilayerPerceptron:
    def __init__(self, training_set, expected_output, learning_rate, layers, momentum, learning_type, learning_rate_params = None):
        self.training_set = np.array(list(map(lambda t: np.append(t, [1]), training_set)))
        self.expected_output = expected_output
        self.learning_rate = learning_rate
        self.layers = layers
        self.error_min = None
        self.w_min = None

    # def train(self, epochs):
    #     w = np.random.uniform(-1, 1, len(self.training_set[0]))
    #     error = 1
    #     p = len(self.training_set)
    #     self.error_min = float('inf')
    #     for epoch in range(epochs):
    #         while error > 0:
    #             i_x = np.random.randint(1, p)
