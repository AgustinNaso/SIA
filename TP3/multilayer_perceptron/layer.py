from neuron import Neuron


class Layer:

    def __init__(self, neurons, g, prev_layer_neurons, is_first=False, training_set=None, is_last=False):
        self.neurons = []
        if is_first:
            for i in range(len(training_set)):
                self.neurons.append(Neuron(None, g, training_set[i], False))
        else:
            if not is_last:
                self.neurons.append(Neuron(None, g, 1, False))
            for i in range(neurons):
                self.neurons.append(Neuron(prev_layer_neurons, g, 0))

    def __str__(self):
        return self.neurons

    def get_neurons_activation(self):
        activations = []
        for neuron in self.neurons:
            activations.append(neuron.activation)
        return activations

    def propagate(self, prev_layer):
        for neuron in self.neurons:
            neuron.activate(prev_layer.get_neurons_activation())
