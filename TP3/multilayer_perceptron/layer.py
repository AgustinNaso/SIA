from TP3.multilayer_perceptron.neuron import Neuron
from TP3.constants import *
import numpy as np


class Layer:

    def __init__(self, neurons, prev_layer_neurons, layer):
        self.neurons = []
        if layer > FIRST:
            self.neurons = [Neuron(prev_layer_neurons, 0) for i in range(neurons)]

    def __str__(self):
        return self.neurons

    def set_activations(self, training_set):
        for i in range(len(training_set)):
            self.neurons.append(Neuron(None, training_set[i], False))

    def get_neurons_activation(self):
        return np.array(list(map(lambda neuron: neuron.activation, self.neurons)))

    def propagate(self, prev_layer):
        for neuron in self.neurons:
            neuron.activate(prev_layer.get_neurons_activation())
