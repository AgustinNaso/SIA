import numpy as np

import ex3_utils
from TP3.constants import FIRST, MIDDLE, LAST
from multilayer_perceptron.multilayer_perceptron import MultilayerPerceptron


def ex1(learning_rate, epochs, layers):
    inputs = ex3_utils.import_data('data/ex3_1_training_set')
    outputs = ex3_utils.normalize(np.array(ex3_utils.import_data('data/ex3_1_expected_output'), dtype=float))

    training_set = np.array(inputs)
    expected_output = np.array(outputs)

    learning_rate = learning_rate
    epochs = epochs
    perceptron = MultilayerPerceptron(training_set, expected_output, learning_rate)
    perceptron.add(2, FIRST)
    for i in range(len(layers)):
        perceptron.add(layers[i], MIDDLE)
    perceptron.add(1, LAST)
    perceptron.train(epochs)

    test_set = np.array([[1, 1], [-1, 1]], dtype=float)
    test_outputs = np.array([[1], [-1]], dtype=float)

    results = np.array(perceptron.test_input(test_set), dtype=float)
    print('Expected      Result')

    for i in range(results.size):
        print(f'{test_outputs[i]}    {results[i]}')

