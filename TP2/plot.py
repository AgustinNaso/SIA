from typing import Final

import numpy as np

from TP2.individual import Individual
from TP2.population import Population
from main_algorithm import BOLTZMANN
from main_algorithm import main_algorithm
import matplotlib.pyplot as plt
import csv

selection_name = ["Elite", "Truncate", "Roulette Wheel", "Rank", "Tournament", "Boltzmann"]
SELECTION_SIZE: Final = 6
crossbreed_name = ["Simple", "Multiple", "Uniform"]
CROSSBREED_SIZE: Final = 3
population_size = 50
generations = 500
t0 = 2
tc = 1
k = 0.5
save_path = "C:/Users/agus_/Desktop/SIA CHARTS/P150/Mutacion Baja/"
extension = ".png"
color = ['red', 'blue', 'green']

starting_pop = Population(population_size)
for i in range(population_size):
    starting_pop.population.append(Individual(np.random.uniform(low=-30, high=30, size=11)))


def plot(selection, mutation_type, starting_population, temperature=-1):
    x = np.arange(1, generations + 1)
    for crossbreed in range(1):
        ans = main_algorithm(selection, crossbreed, population_size, generations, t0, tc, k, mutation_type,
                             starting_population)
        y = ans[1]
        plt.plot(x, y, color=color[crossbreed])
        plt.xlabel("Iteración")
        plt.ylabel("Error")
        title = selection_name[selection] + " + " + "Mutación Baja"
        if temperature >= 0:
            title += f" + T{temperature}"
        plt.title(title)
    # save_title = title
    # plt.savefig(save_path + save_title + extension)
    plt.show()
    # first = 500
    # for i in range(len(y)):
    #     if y[i] == 0.0:
    #         first = i
    # y_2 = y[first - 100:first]
    # x_2 = x[first - 100:first]
    # plt.plot(x_2, y_2)
    # title = "Observacion Ampliada\n" + title
    # save_title = "AMP " + save_title
    # plt.title(title)
    # plt.xlabel("Iteración")
    # plt.ylabel("Error")
    # plt.savefig(save_path + save_title + extension)
    # plt.show()


for mutation in range(3):
    for selection in range(SELECTION_SIZE - 1):
        starting_pop_copy = starting_pop.population.copy()
        plot(selection, mutation, starting_pop_copy)

#
# # Graficos boltzmann variando  temperaturas y k
# for i in range(3):
#     selection = BOLTZMANN
#     t0 = 2 * (i + 1)
#     tc = 1 * (i + 1)
#     k = 0.5 * (i + 1)
#     for crossbreed in range(CROSSBREED_SIZE):
#         plot(selection, crossbreed, i)
