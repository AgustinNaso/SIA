import numpy as np
from utils import import_data, standarize, get_headers

eta = 0.01


class LinearPerceptron:
    def __init__(self, standard_inputs, eta):
        self.standard_inputs, self.eta, self.w = standard_inputs, eta, np.random.rand(len(standard_inputs[0]))

    def train(self, epochs):
        for i in range(epochs):
            for x in range(len(self.standard_inputs)):
                y = self.output(self.standard_inputs[x])
                self.w = self.w + eta * y * (self.standard_inputs[x] - y * self.w)
        return self.w

    def output(self, x):
        ans = 0
        for i in range(len(self.w)):
            ans += self.w[i] * x[i]
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

perceptron = LinearPerceptron(standard_inputs, eta)
w = perceptron.train(5000)

print(headers)
print(w.__str__())
