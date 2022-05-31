import numpy as np
from utils import import_data, standarize, get_headers
from pca import get_pca_first_components, get_pca_first_component
import matplotlib.pyplot as plt

# eta = 0.02
INITIAL_VALUE = 2


class LinearPerceptron:
    def __init__(self, data, learning_rate):
        self.standard_inputs, self.eta, self.w = data, learning_rate, np.copy(standard_inputs[INITIAL_VALUE])

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


def printComparationWithPCA(oja, pca, countries):
    print("oja\t\t\t\tpca\t\t\tdifference\t\tcountries")
    maxdiff = abs(oja[0] - pca[0])
    for z in range(len(countries)):
        if maxdiff < abs(oja[z] - pca[z]):
            maxdiff = abs(oja[z] - pca[z])
        if oja[z] > 0:
            print(f' {oja[z]:.5f}\t\t {pca[z]:.5f}\t\t{abs(oja[z] - pca[z]):.5f}\t\t{countries[z]} ')
        else:
            print(f'{oja[z]:.5f}\t\t{pca[z]:.5f}\t\t{abs(oja[z] - pca[z]):.5f}\t\t{countries[z]} ')
    print("max error: " + str(maxdiff))

def plot_variables(variable_names, axis):
    plt.barh([i for i in range(len(axis))], axis)
    plt.yticks([i for i in range(len(axis))], variable_names)

def plot_index(countries, components):
    data = [ (name, component) for name, component in zip(countries, components)]
    sorted_data = np.array(sorted(data, key=lambda x: x[1]))
    plt.barh([i for i in range(len(sorted_data))], sorted_data[:,1])
    plt.yticks([i for i in range(len(sorted_data))], sorted_data[:,0])
    plt.xticks([]) # do not display all numbers

countries, inputs = import_data("europe.csv")
headers = get_headers("europe.csv")
standard_inputs = standarize(inputs)

eta = 0.0001
perceptron = LinearPerceptron(standard_inputs, eta)
w = perceptron.train(1000)

first_component = []
for i in range(len(countries)):
    first_component.append(perceptron.output(standard_inputs[i]))


data = [ (name, componentOja, componentPca) for name, componentOja, componentPca in zip(countries, first_component
                                                                                        , get_pca_first_components())]
sorted_data = np.array(sorted(data, key=lambda x: x[1]))

countriesS = []
ojaS = []
pcaS = []
for i in range(len(countries)):
    countriesS.append(sorted_data[i][0])
    ojaS.append(float(sorted_data[i][1]))
    pcaS.append(float(sorted_data[i][2]))

printComparationWithPCA(ojaS, pcaS, countriesS)
#
# plt.figure("Oja first component register")
# plot_variables(headers, perceptron.w)
# plt.title("Oja first component registers")
# plt.tight_layout()
# plt.subplots_adjust(top=0.94)
# plt.savefig("ojaFirstComponents")
# # plt.show()
# #
# plt.close()
# plt.figure(" pca first component")
# plot_variables(headers, get_pca_first_component())
# plt.title("Pca first component registers")
# plt.tight_layout()
# plt.subplots_adjust(top=0.94)
# plt.savefig("PCAFirstComponents")
# # plt.show()
# #
# plt.close()
# plt.figure("index oja")
# plot_index(countries, first_component)
# plt.title("Oja index")
# plt.tight_layout()
# plt.subplots_adjust(top=0.94)
# plt.savefig("OjaIndex")
# # # plt.show()
# #
# plt.close()
# plt.figure("index pca")
# plot_index(countries, get_pca_first_components())
# plt.title("Pca index")
# plt.tight_layout()
# plt.subplots_adjust(top=0.94)
# plt.savefig("PcaIndex")
# # # plt.show()
