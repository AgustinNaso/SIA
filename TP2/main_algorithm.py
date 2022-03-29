import json
from typing import Final

import numpy as np
from individual import Individual
from population import Population
from selection import elite_selection, stochastic_selection, truncate_selection, roulette_wheel_selection, \
    rank_selection, tournament_selection, boltzmann_selection
from crossbreed import simple_crossbreed, multiple_crossbreed, uniform_crossbreed
from mutation import mutation

BOLTZMANN: Final = 6
with open("settings.json") as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()

selection = int(jsonObject['selection'])
crossbreed = int(jsonObject['crossbreed'])
population_size = int(jsonObject['size'])
generations = int(jsonObject['generations'])
t0 = int(jsonObject['t0'])
tc = int(jsonObject['tc'])
k = int(jsonObject['k'])
stop_criteria = int(jsonObject['stop_criteria'])

selections = np.array([elite_selection, stochastic_selection, truncate_selection, roulette_wheel_selection,
                       rank_selection, tournament_selection, boltzmann_selection])
crossbreed_methods = np.array([simple_crossbreed, multiple_crossbreed, uniform_crossbreed])


def main_algorithm():
    population = Population(population_size)
    for i in range(population_size):
        population.population.append(Individual(np.random.randn(11)))
    min_fitness = population.min_fitness()
    count = stop_criteria
    for i in range(generations):
        total = population_size
        while total < 2 * population_size:
            if selection == BOLTZMANN:
                parents = selections[selection](population, i, t0, tc, k, 2)
            else:
                parents = selections[selection](population, 2)
            children = crossbreed_methods[crossbreed](parents[0], parents[1])
            for individual in children:
                population.population.append(mutation(individual))
            total += 2
        if selection == BOLTZMANN:
            population.set_new_population(selections[selection](population, i, t0, tc, k, population_size))
        else:
            population.population = selections[selection](population, population_size)
        new_min_fitness = population.min_fitness()
        if new_min_fitness == min_fitness:
            count -= 1
            if count < 0:
                return new_min_fitness
        elif new_min_fitness < min_fitness:
            min_fitness = new_min_fitness
            count = stop_criteria
            print(min_fitness)
    return min_fitness


main_algorithm()
