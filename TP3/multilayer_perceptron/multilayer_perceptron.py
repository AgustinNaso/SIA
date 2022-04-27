import numpy as np
from layer import Layer

INCREMENTAL = "incremental"
BATCH = "batch"


class MultilayerPerceptron:
    def __init__(self, training_set, expected_output, learning_rate, learning_type=INCREMENTAL, momentum=None,
                 learning_rate_params=None):
        self.training_set = np.array(list(map(lambda t: np.append(t, [1]), training_set)))
        self.expected_output = expected_output
        self.learning_rate = learning_rate
        self.learning_type = learning_type
        self.layers = []
        self.error_min = None
        self.w_min = None
        if momentum:
            self.momentum = momentum
        if learning_rate_params:
            self.learning_rate_inc = learning_rate_params[0]
            self.learning_rate_dec = learning_rate_params[1]
            self.learning_rate_k = learning_rate_params[2]

    def train(self, epochs):
        error = 1
        prev_error = error
        self.error_min = float('inf')
        m = len(self.layers)
        for epoch in range(epochs):
            aux_training_set = self.training_set
            aux_expected_output = self.expected_output
            while len(aux_training_set) > 0:
                i_x = np.random.randint(0, len(aux_training_set))
                training_set = aux_training_set[i_x]
                expected_output = aux_expected_output[i_x]

                np.delete(aux_training_set, i_x, axis=0)
                np.delete(aux_expected_output, i_x, axis=0)

                # for i in range(1, m):

    def add(self, neurons, g, is_first=False, is_last=False):
        if is_first:
            self.layers.append(Layer(neurons, None, None, is_first))
        else:
            prev_layer_neurons = len(self.layers[len(self.layers) - 1].neurons)
            if is_last:
                self.layers.append(Layer(neurons, g, prev_layer_neurons, is_first, is_last))
            else:
                self.layers.append(Layer(neurons, g, prev_layer_neurons))

    def adapt_learning_rate(self, delta_error, k):
        if delta_error < 0:
            if k > 0:
                k = 0
            k -= 1
            if k == -self.learning_rate:
                self.learning_rate += self.learning_rate_inc
        elif delta_error > 0:
            if k < 0:
                k = 0
            k += 1
            if k == self.learning_rate:
                self.learning_rate -= self.learning_rate_dec * self.learning_rate
        else:
            k = 0
        return k
