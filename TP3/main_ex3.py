import csv
from TP3.constants import *
import numpy as np
from multilayer_perceptron.multilayer_perceptron import MultilayerPerceptron


def normalize(output):
    min_expected = min(output)
    max_expected = max(output)
    return np.array(list(map(lambda x: 2 * ((x - min_expected) / (max_expected - min_expected)) - 1, output)))

def import_data(file):
    csv_file = open(file, 'r')
    csv_reader = csv.reader(csv_file, delimiter=" ")
    data = []
    for row in csv_reader:
        entry = [float(a) for a in row if a != '']
        data.append(entry)
    return data


inputs = import_data('data/ex3_training_set')
outputs = normalize(np.array(import_data('data/ex3_expected_output'), dtype=float))
# training_set = np.array([[-1, 1], [1, -1], [-1, -1], [1, 1]], dtype=float)
# expected_output = np.array([[-1], [-1], [-1], [1]], dtype=float)
# test_set = np.array([[1, 1]], dtype=float)
# test_outputs = np.array([[1]], dtype=float)
learning_rate = 0.01
training_set = np.array(inputs[10:], dtype=float)
test_set = np.array(inputs[:10], dtype=float)
expected_output = np.array(outputs[10:], dtype=float)
print(expected_output)
test_outputs = np.array(outputs[:10], dtype=float)
learning_rate_params = [0.2, 0.2, 5]
perceptron = MultilayerPerceptron(training_set, expected_output, learning_rate, learning_rate_params)
# perceptron = MultilayerPerceptron(training_set, expected_output, learning_rate)
perceptron.add(2, FIRST)
perceptron.add(6, MIDDLE)
perceptron.add(1, LAST)
perceptron.train(100)

results = np.array(perceptron.test_input(test_set), dtype=float)
print('Expected      Result')

for i in range(results.size):
    print(f'{test_outputs[i]}    {results[i]}')
