import json
import numpy as np

from individual import Individual
from population import Population
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
mutation_bound = int(jsonObject['mutation_bound'])
mutation_rate = float(jsonObject['mutation_rate'])
t0 = int(jsonObject['t0'])
tc = int(jsonObject['tc'])
k = int(jsonObject['k'])

starting_pop = Population(population_size)
for i in range(population_size):
    starting_pop.population.append(Individual(np.random.uniform(low=-30, high=30, size=11)))


def main():
    mutation = [mutation_rate, mutation_bound]
    results = main_algorithm(selection, crossbreed, population_size, generations, t0, tc, k, mutation)
    print(results[0])
    # for mutation in range(3):
    #     for selection in range(SELECTION_SIZE - 1):
    #         for j in range(CROSSBREED_SIZE):
    #             starting_pop_copy = starting_pop.population.copy()
    #             main_algorithm(selection, j, population_size, generations, t0, tc, k, mutation, starting_pop_copy)
    #
    # for i in range(3): selection = BOLTZMANN t0_1 = 2 * (i + 1) tc_1 = 1 * (i + 1) k_1 = 0.5 * (i + 1) for
    # crossbreed_i in range(CROSSBREED_SIZE): starting_pop_copy = starting_pop.population.copy() main_algorithm(
    # selection, crossbreed_i, population_size, generations, t0_1, tc_1, k_1, mutation, starting_pop_copy)


if __name__ == "__main__":
    main()
