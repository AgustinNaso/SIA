import numpy as np
from utils import import_data, standarize, get_headers


# eta = 0.02


class LinearPerceptron:
    def __init__(self, data, learning_rate):
        self.standard_inputs, self.eta, self.w = data, learning_rate, np.copy(standard_inputs[0])

    def train(self, epochs):
        for i in range(epochs):
            for x in range(len(self.standard_inputs)):
                y = self.output(self.standard_inputs[x])
                self.w = self.w + self.eta * y * (self.standard_inputs[x] - y * self.w)
        return self.w

    def output(self, x):
        ans = 0
        for j in range(len(self.w)):
            ans += self.w[j] * x[j]
        return ans


def get_mean(x, countries):
    for i, val in enumerate(x):
        print(f"COUNTRY: {countries[i]}")
        print(x[i])
        print("----------------------------")
        print(f"MEAN: {val.mean()}")
        print("----------------------------")
        x[i] = val - val.mean()
        print(x[i])
        print("----------------------------")
    return x


countries, inputs = import_data("europe.csv")
headers = get_headers("europe.csv")
standard_inputs = standarize(inputs)

# for i in range(1000):
# eta = 0.0877
eta = 0.01
perceptron = LinearPerceptron(standard_inputs, eta)
w = perceptron.train(1000)

first_component = []
for i in range(len(countries)):
# for i in range(1):
#     if perceptron.output(standard_inputs[i]) < 0:
#     print("eta: " + str(eta))
    first_component.append([countries[i], perceptron.output(standard_inputs[i])])
    print(countries[i][2:] + "    " + str(perceptron.output(standard_inputs[i])))
