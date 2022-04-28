import numpy as np
from perceptron.simple_perceptron import SimplePerceptron
import matplotlib.pyplot as plt


# training_set = np.array([[-1, 1], [1, -1], [-1, -1]])
# expected_output = np.array([-1, -1, -1])
training_set = np.array([[-1, 1], [1, -1], [-1, -1], [1, 1]])
expected_output = np.array([-1, -1, -1, 1])
learning_rate = 0.08
iterations = 10000
perceptron = SimplePerceptron(training_set, expected_output, learning_rate)
perceptron.train(iterations)
y1 = perceptron.getPointOverlineResult(perceptron.w_min, -1)
point1 = np.array([-1, y1])
y2 = perceptron.getPointOverlineResult(perceptron.w_min, 1)
point2 = np.array([1, y2])

x_values = [point1[0], point2[0]]
y_values = [point1[1], point2[1]]
plt.plot(x_values, y_values)
plt.plot(-1,-1, 'go')
plt.plot(-1,1, 'go')
plt.plot(1,-1, 'go')
plt.plot(1,1, 'go')

plt.show()

results = perceptron.test_input(np.array([[1, 1]]))
for i in results:
    print(i)
