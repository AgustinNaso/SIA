from neuron import Neuron


class Layer:

    def __init__(self, neurons, g, lastLayerNeurons,isFirst):
        self.Neurons = []
        for i in range(neurons):
            self.Neurons.append(Neuron(lastLayerNeurons, g))

    def __str__(self):
        return self.Neurons
