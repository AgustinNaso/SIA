import numpy as np
from perceptron.simple_perceptron import SimplePerceptron
import matplotlib.pyplot as plt

DOT_SIZE = 15
# training_set = np.array([[-1, 1], [1, -1], [-1, -1]])
# expected_output = np.array([-1, -1, -1])
training_set = np.array([[-1, 1], [1, -1], [-1, -1], [1, 1]])
expected_output = np.array([-1, -1, -1, 1])
learning_rate = 0.00001
iterations = 1000
perceptron = SimplePerceptron(training_set, expected_output, learning_rate)
perceptron.train(iterations)
y1 = perceptron.get_point_overline_result(perceptron.w_min, -1.2)
point1 = np.array([-1.2, y1])
y2 = perceptron.get_point_overline_result(perceptron.w_min, 1.2)
point2 = np.array([1.2, y2])

perceptron.plot()

x_values = [point1[0], point2[0]]
y_values = [point1[1], point2[1]]
plt.plot(x_values, y_values)
plt.plot(-1,-1, 'o', c='black', markersize=DOT_SIZE)
plt.plot(-1,1, 'o', c='black', markersize=DOT_SIZE)
plt.plot(1,-1, 'o', c='black', markersize=DOT_SIZE)
plt.plot(1,1, 'go', markersize=DOT_SIZE)
plt.ylim(-1.5, 1.5)

plt.show()

results = perceptron.test_input(np.array([[1, 1]]))
for i in results:
    print(i)
