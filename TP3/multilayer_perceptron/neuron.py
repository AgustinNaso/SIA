import numpy as np
import constants


class Neuron:
    excitation = 0
    activation = 0

    def __init__(self, prev_layer_neurons, g, activation, has_weights=True):
        self.activation = activation
        self.g = g
        if has_weights:
            self.weights = np.random.randint(-1, 1, prev_layer_neurons, dtype=float)

    def excite(self, prev_layer_activations):
        self.excitation = np.inner(self.weights, prev_layer_activations) + constants.BIAS
        return self.excitation

    def activate(self, prev_layer_activations):
        self.activation = self.g(self.excite(prev_layer_activations))
        return self.activation

    # def error(self):
