import json
import numpy as np

from TP2.individual import Individual
from TP2.population import Population
from main_algorithm import main_algorithm

with open("settings.json") as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()

SELECTION_SIZE = 6
crossbreed_name = ["Simple", "Multiple", "Uniform"]
CROSSBREED_SIZE = 3

selection = int(jsonObject['selection'])
crossbreed = int(jsonObject['crossbreed'])
population_size = int(jsonObject['size'])
generations = int(jsonObject['generations'])
t0 = int(jsonObject['t0'])
tc = int(jsonObject['tc'])
k = int(jsonObject['k'])

starting_pop = Population(population_size)
for i in range(population_size):
    starting_pop.population.append(Individual(np.random.uniform(low=-30, high=30, size=11)))


def main():
    for mutation in range(3):
        for j in range(CROSSBREED_SIZE):
            starting_pop_copy = starting_pop.population.copy()
            main_algorithm(5, j, population_size, generations, t0, tc, k, mutation, starting_pop_copy)


if __name__ == "__main__":
    main()
