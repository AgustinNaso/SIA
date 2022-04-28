import csv
from TP3.constants import *
import numpy as np
from multilayer_perceptron.multilayer_perceptron import MultilayerPerceptron


def import_data(file):
    csv_file = open(file, 'r')
    csv_reader = csv.reader(csv_file, delimiter=" ")
    data = []
    for row in csv_reader:
        entry = [float(a) for a in row if a != '']
        data.append(entry)
    return data


inputs = import_data('data/ex3_training_set')
outputs = np.array(import_data('data/ex3_expected_output'), dtype=float)
# print(outputs)
learning_rate = 0.02
training_set = inputs[:60]
test_set = np.array(inputs[60:], dtype=float)
expected_output = outputs[:60]
test_outputs = np.array(outputs[60:], dtype=float)
perceptron = MultilayerPerceptron(training_set, expected_output, learning_rate, 1)
perceptron.add(len(training_set[0]), FIRST)
perceptron.add(3, MIDDLE)
perceptron.add(2, MIDDLE)
perceptron.add(len(expected_output[0]), LAST)
perceptron.train(100)

results = np.array(perceptron.test_input(test_set), dtype=float)
print('Expected      Result')

for i in range(results.size):
    print(f'{test_outputs[i]}    {results[i]}')
