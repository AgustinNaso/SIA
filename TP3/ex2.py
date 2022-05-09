import csv
import numpy as np
import json
from perceptron.linear_perceptron import LinearPerceptron
from perceptron.non_linear_perceptron import NonLinearPerceptron
from constants import *


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


with open("ex2_config.json") as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()

# Perceptron types: "linear" and "non linear"
perceptron_type = str(jsonObject["perceptron"])
learning_rate = int(jsonObject["learning_rate"])
epochs = int(jsonObject["epochs"])
test_set_start = int(jsonObject["test_set_start"])
test_set_end = int(jsonObject["test_set_end"])

inputs = import_data('data/ex2_training_set')
if perceptron_type == LINEAR:
    outputs = np.array(import_data('data/ex2_expected_output'), dtype=float)
    perceptron = LinearPerceptron(inputs, outputs, learning_rate)
else:
    outputs = normalize(np.array(import_data('data/ex2_expected_output'), dtype=float))
    perceptron = NonLinearPerceptron(inputs, outputs, learning_rate)

perceptron.train(epochs)
test_set = inputs[test_set_start:test_set_end]
test_output = outputs[test_set_start:test_set_end]

results = perceptron.test_input(test_set)
error = 0
for k in range(len(test_output)):
    error += abs(results[k] - test_output[k])

print(error/len(test_output))
