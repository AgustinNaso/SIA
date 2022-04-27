from neuron import Neuron
import TP3.constants as constants


class Layer:

    def __init__(self, neurons, g, prev_layer_neurons, layer):
        self.neurons = []
        if layer > constants.FIRST:
            if layer != constants.LAST:
                self.neurons.append(Neuron(None, g, 1, False))
            for i in range(neurons):
                self.neurons.append(Neuron(prev_layer_neurons, g, 0))

    def __str__(self):
        return self.neurons

    def set_activations(self, training_set):
        for i in range(len(training_set)):
            self.neurons.append(Neuron(None, None, training_set[i], False))

    def get_neurons_activation(self):
        activations = []
        for neuron in self.neurons:
            activations.append(neuron.activation)
        return activations

    def propagate(self, prev_layer):
        for neuron in self.neurons:
            neuron.activate(prev_layer.get_neurons_activation())
