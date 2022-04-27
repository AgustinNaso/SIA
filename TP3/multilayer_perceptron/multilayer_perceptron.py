import numpy as np
from layer import Layer
import constants


class MultilayerPerceptron:
    adaptive_rate = False

    def __init__(self, training_set, expected_output, learning_rate, learning_type=constants.INCREMENTAL,
                 learning_rate_params=None, momentum=False):
        self.training_set = training_set
        self.expected_output = expected_output
        self.learning_rate = learning_rate
        self.learning_type = learning_type
        self.layers = []
        self.error_min = None
        self.w_min = None
        self.momentum = momentum
        if learning_rate_params:
            self.adaptive_rate = True
            self.learning_rate_inc = learning_rate_params[0]
            self.learning_rate_dec = learning_rate_params[1]
            self.learning_rate_k = learning_rate_params[2]

    def train(self, epochs):
        error = 1
        prev_error = None
        self.error_min = float('inf')
        m = len(self.layers)
        k = 0
        for epoch in range(epochs):
            aux_training_set = self.training_set
            aux_expected_output = self.expected_output
            while len(aux_training_set) > 0:
                i_x = np.random.randint(0, len(aux_training_set))
                training_set = aux_training_set[i_x]
                expected_output = aux_expected_output[i_x]

                np.delete(aux_training_set, i_x, axis=0)
                np.delete(aux_expected_output, i_x, axis=0)

                self.layers[0].set_activations(training_set)
                for i in range(1, m):
                    self.layers[i].propagate()

                self.backpropagation(expected_output)

                if self.learning_type == constants.INCREMENTAL:
                    self.update_weights()

                aux_error = self.calculate_error(expected_output)
                error += aux_error

                if self.adaptive_rate and prev_error:
                    k = self.adapt_learning_rate(error - prev_error, k)
                prev_error = aux_error

            error *= 0.5
            if error < self.error_min:
                self.error_min = error

    def calculate_error(self, expected_output):
        m = len(self.layers)
        neurons = self.layers[m-1].neurons
        aux_sum = 0
        for i in range(len(neurons)):
            aux_sum += (expected_output[i] - neurons[i].activation)**2
        return aux_sum

    def backpropagation(self, expected_output):
        m = len(self.layers)
        for i in range(m - 1, 0, -1):
            layer = self.layers[i]
            for j in range(len(layer.neurons)):
                if i == m - 1:
                    layer[j].sigma = layer[j].excitation * (expected_output[i] - layer[j].activation)
                else:
                    upper_layer_neurons = self.layers[i + 1]
                    aux_sum = 0
                    for neuron in upper_layer_neurons:
                        aux_sum += neuron.weights[j] * neuron.sigma
                    layer[j].sigma = layer[j].excitation * aux_sum

    def update_weights(self):
        m = len(self.layers)
        for i in range(1, m):
            neurons = self.layers[i]
            prev_neurons_activations = self.layers[i - 1].get_neurons_activation()
            for neuron in neurons:
                neuron.update_weights(self.learning_rate, prev_neurons_activations, self.momentum)

    def add(self, neurons, g, layer):
        if layer == constants.FIRST:
            self.layers.append(Layer(neurons, None, None, constants.FIRST))
        else:
            prev_layer_neurons = len(self.layers[len(self.layers) - 1].neurons)
            self.layers.append(Layer(neurons, g, prev_layer_neurons, layer))

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
