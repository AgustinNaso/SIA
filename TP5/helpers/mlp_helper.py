import numpy as np
from TP5.multilayer_perceptron.multilayer_perceptron import MultilayerPerceptron
from TP5.multilayer_perceptron.constants import *


def create_multilayer_perceptron_and_train(training_set: np.ndarray, expected_output: np.ndarray, learning_rate: float,
                                           epochs: int, layers: np.ndarray, batch_size: int,
                                           momentum=False, adaptive_params=None, noise_coverage=None,
                                           noise_factor=None) -> MultilayerPerceptron:
    perceptron = MultilayerPerceptron(training_set, expected_output, learning_rate, adaptive_params, batch_size,
                                      momentum)
    # For basic autoencoder, training set should be the same as expected output
    perceptron.add(len(training_set[0]), FIRST)
    for i in range(len(layers)):
        perceptron.add(layers[i], MIDDLE)
    perceptron.add(len(expected_output[0]), LAST)
    if noise_coverage:
        perceptron.train(epochs, noise_coverage, noise_factor)
    else:
        perceptron.train(epochs)
    return perceptron

def round_array(array):
    for idx in range(len(array)):
        array[idx] = 1 if array[idx] > 0.7 else 0
    return np.array(array).reshape(7, 5)


def concept_vector(point1, point2, point_amount):
    delta_0 = point2[0] - point1[0]
    delta_1 = point2[1] - point1[1]
    vector = []
    for i in range(point_amount):
        vector.append([point1[0] + delta_0 * (i / point_amount), point1[1] + delta_1 * (i / point_amount)])
    return np.array(vector)