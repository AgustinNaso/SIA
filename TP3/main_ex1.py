import numpy as np
from perceptron.simple_perceptron import SimplePerceptron
import matplotlib.pyplot as plt

DOT_SIZE = 15
# training_set = np.array([[-1, 1], [1, 1], [-1, -1]])
# expected_output = np.array([-1, 1, -1])
training_set = np.array([[-1, 1], [1, -1], [-1, -1], [1, 1]])
expected_output = np.array([1, 1, -1, -1])
learning_rate = 0.01
iterations = 10000
perceptron = SimplePerceptron(training_set, expected_output, learning_rate)
perceptron.train(iterations)
# w = perceptron.w_min
# x = np.linspace(-2, 2, 100)
# y = -(w[0]*x/w[1]) - w[2]/w[1] 
# plt.title(f'Variacion de vector w con η = {learning_rate}, iteracion= {x}')
# plt.xlabel('ξ_1')
# plt.ylabel('ξ_2')
# plt.plot(x, y, label='line', linewidth=2)
# plt.plot(-1,-1, 'o', c='black', markersize=DOT_SIZE)
# plt.plot(-1,1, 'go' , markersize=DOT_SIZE)
# plt.plot(1,-1, 'go' , markersize=DOT_SIZE)
# plt.plot(1,1, 'o', markersize=DOT_SIZE)
# plt.ylim(-2,2)
# plt.show()

results = perceptron.test_input(np.array([[1, 1]]))
for i in results:
    print(i)
