import csv
from TP3.constants import *
import numpy as np
from multilayer_perceptron.multilayer_perceptron import MultilayerPerceptron


def normalize(output):
    min_expected = min(output)
    max_expected = max(output)
    return np.array(list(map(lambda x: 2 * ((x - min_expected) / (max_expected - min_expected)) - 1, output)))


def import_data(file, quantity):
    csv_file = open(file, 'r')
    csv_reader = csv.reader(csv_file, delimiter=" ")
    data = []
    entry = []
    row_count = 0
    for row in csv_reader:
        if quantity == 1:
            entry = [float(a) for a in row if a != '']
            data.append(entry)
        else:
            if row_count == quantity:
                data.append(entry)
                entry = []
            else:
                for a in row:
                    if a != '':
                        entry.append(float(a))
    return data


inputs = import_data('data/ex3_training_set', 7)
outputs = import_data('data/ex3_3_expected_output', 1)
# outputs = np.array([[1], [0], [1], [0], [1], [0], [1], [0], [1], [0]], dtype=float)
# outputs = np.array(import_data('data/ex3_2_expected_output', 1), dtype=float)
# training_set = np.array([[-1, 1], [1, -1], [-1, -1], [1, 1]], dtype=float)
# expected_output = np.array([[-1], [-1], [-1], [1]], dtype=float)
# test_set = np.array([[1, 1]], dtype=float)
# test_outputs = np.array([[1]], dtype=float)
learning_rate = 0.01
training_set = np.array(inputs, dtype=float)
test_set = np.array(inputs[1:3], dtype=float)
expected_output = np.array(outputs, dtype=float)
test_outputs = np.array(outputs[1:3], dtype=float)
learning_rate_params = [0.2, 0.2, 5]
perceptron = MultilayerPerceptron(training_set, expected_output, learning_rate, learning_rate_params)
# perceptron = MultilayerPerceptron(training_set, expected_output, learning_rate)
perceptron.add(35, FIRST)
perceptron.add(6, MIDDLE)
perceptron.add(3, MIDDLE)
perceptron.add(1, LAST)
perceptron.train(500)

results = np.array(perceptron.test_input(test_set), dtype=float)
print('Expected      Result')

for i in range(results.size):
    print(f'{test_outputs[i]}    {results[i]}')
