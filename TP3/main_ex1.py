import numpy as np
from perceptron.simple_perceptron import SimplePerceptron


training_set = np.array([[-1, 1], [1, -1], [-1, -1]])
expected_output = np.array([-1, -1, -1])
# training_set = np.array([[-1, 1], [1, -1], [-1, -1], [1, 1]])
# expected_output = np.array([1, 1, -1, -1])
learning_rate = 0.1
iterations = 1000
perceptron = SimplePerceptron(training_set, expected_output, learning_rate)
perceptron.train(iterations)
results = perceptron.get_results(np.array([[1, 1]]))
for i in results:
    print(i)
