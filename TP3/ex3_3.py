import numpy as np

import ex3_utils
from TP3.constants import FIRST, MIDDLE, LAST
from multilayer_perceptron.multilayer_perceptron import MultilayerPerceptron


def ex3(learning_rate, epochs, layers):
    inputs = ex3_utils.import_data('data/ex3_23_training_set', 7)
    outputs = np.array(ex3_utils.import_data('data/ex3_3_expected_output', 1), dtype=float)

    training_set = np.array(inputs)
    expected_output = np.array(outputs)

    learning_rate = learning_rate
    epochs = epochs
    perceptron = MultilayerPerceptron(training_set, expected_output, learning_rate)
    perceptron.add(35, FIRST)
    for i in range(len(layers)):
        perceptron.add(layers[i], MIDDLE)
    perceptron.add(10, LAST)
    perceptron.train(epochs)

    training_set = create_noise(training_set)
    results = np.array(perceptron.test_input(training_set), dtype=float)
    print('Expected   Result')

    for i in range(len(results)):
        print(f'{get_max_index(expected_output[i])}          {get_max_index(results[i])}')


def get_max_index(array):
    max = 0
    index = 0
    for i in range(len(array)):
        if max < array[i]:
            max = array[i]
            index = i
    return index


def create_noise(test_set):
    for i in range(len(test_set)):
        for j in range(len(test_set[i])):
            if j % 5 == 0 and j != 0:
                test_set[i][j] = noise(test_set[i][j])
    return test_set


def noise(number):
    probability = np.random.rand(1)[0]
    if probability < 0.02:
        if number == 1:
            return 0
        else:
            return 1
    return number
