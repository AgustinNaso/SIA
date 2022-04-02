from typing import Final

import numpy as np

from TP2.selection import BOLTZMANN
from main_algorithm import main_algorithm
import matplotlib.pyplot as plt

selection = 0
selection_name = ["Elite", "Truncate", "Roulette Wheel", "Rank", "Tournament", "Boltzmann"]
SELECTION_SIZE: Final = 6
crossbreed = 1
crossbreed_name = ["Simple", "Multiple", "Uniform"]
CROSSBREED_SIZE: Final = 3
population_size = 500
generations = 500
t0 = 1
tc = 1
k = 10
stop_criteria = 100

for i in range(SELECTION_SIZE):
    selection = i
    for j in range(CROSSBREED_SIZE):
        crossbreed = j
        if selection == BOLTZMANN:
            t0 = 4
            tc = 8
            k = 15
        ans = main_algorithm(selection, crossbreed, population_size, generations, t0, tc, k, stop_criteria)
        y = ans[1]
        x = np.arange(1, generations + 1)
        plt.plot(x, y)
        plt.xlabel("Iteración")
        plt.ylabel("Error")
        plt.title(selection_name[i] + "+" + crossbreed_name[j])
        plt.show()
