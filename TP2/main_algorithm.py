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
        population.population.append(Individual(np.random.uniform(low=-30, high=30, size=11)))
    max_fitness = 0
    count = stop_criteria
    for i in range(generations):
        # total = population_size
        # print(population.population[0])
        children = []
        while len(children) < population_size:
            if selection == BOLTZMANN:
                parents = selections[selection](population, i, t0, tc, k, 2)
            else:
                parents = selections[selection](population, 2)
            local_children = crossbreed_methods[crossbreed](parents[0], parents[1])
            for child in local_children:
                children.append(child)
            # total += 2
        for child in children:
            population.population.append(mutation(child))
        # print(len(population.population))
        if selection == BOLTZMANN:
            population.population = selections[selection](population, i, t0, tc, k, population_size)
        else:
            # print(f'Esta es la pop: {population}')
            population.population = selections[selection](population, population_size)
        # print(len(population.population))
        if population.max_fitness() == max_fitness:
            count -= 1
            if count < 0:
                return max_fitness
        # elif new_max_fitness > max_fitness:
        #     max_fitness = new_max_fitness
        #     count = stop_criteria
        # print(max_fitness)
        max_fitness = population.max_fitness()
        # print(max_fitness)
        # print(population.population[1])
    return max_fitness


aux = main_algorithm()
print(aux)
