import numpy as np
import json
from perceptron.simple_perceptron import SimplePerceptron
from constants import *


def get_point_overline_result(weights, x):
    return -(weights[0] / weights[1]) * x - weights[2] / weights[1]


with open("ex1_config.json") as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()

problem = str(jsonObject["problem"])
if problem == XOR:
    training_set = np.array([[-1, 1], [1, -1], [-1, -1], [1, 1]])
    expected_output = np.array([1, 1, -1, -1])
else:
    training_set = np.array([[-1, 1], [1, -1], [-1, -1], [1, 1]])
    expected_output = np.array([-1, -1, -1, 1])

learning_rate = int(jsonObject["learning_rate"])
iterations = int(jsonObject["iterations"])
perceptron = SimplePerceptron(training_set, expected_output, learning_rate)
perceptron.train(iterations)

results = perceptron.test_input(np.array([[1, 1]]))
for i in results:
    print(i)
