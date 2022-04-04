from typing import Final

import numpy as np

from main_algorithm import BOLTZMANN
from main_algorithm import main_algorithm
import matplotlib.pyplot as plt

selection_name = ["Elite", "Truncate", "Roulette Wheel", "Rank", "Tournament", "Boltzmann"]
SELECTION_SIZE: Final = 6
crossbreed_name = ["Simple", "Multiple", "Uniform"]
CROSSBREED_SIZE: Final = 3
population_size = 100
generations = 500
t0 = 2
tc = 1
k = 0.5

def plot(selection, crossbreed):
    ans = main_algorithm(selection, crossbreed, population_size, generations, t0, tc, k)
    y = ans[1]
    x = np.arange(1, generations + 1)
    plt.plot(x, y)
    plt.xlabel("Iteración")
    plt.ylabel("Error")
    plt.title(selection_name[selection] + " + " + crossbreed_name[crossbreed] + " + " + "Mutación Alta")
    plt.show()
    first = 500
    for i in range(len(y)):
        if y[i] == 0:
            first = i
    y_2 = y[first-100:first]
    x_2 = x[first-100:first]
    plt.plot(x_2, y_2)
    plt.title(f"Observacion Ampliada\n {selection_name[selection]} + {crossbreed_name[crossbreed]} + Mutación Alta")
    plt.xlabel("Iteración")
    plt.ylabel("Error")
    plt.show()


for selection in range(SELECTION_SIZE - 1):
    for crossbreed in range(CROSSBREED_SIZE):
        plot(selection, crossbreed)

# Graficos boltzmann variando  temperaturas y k
for i in range(3):
    selection = BOLTZMANN
    t0 = 2 * (i + 1)
    tc = 1 * (i + 1)
    k = 0.5 * (i + 1)
    for crossbreed in range(CROSSBREED_SIZE):
        plot(selection, crossbreed)
