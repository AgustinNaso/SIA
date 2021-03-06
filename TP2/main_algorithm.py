import json
from typing import Final

import numpy as np
from individual import Individual
from population import Population
from selection import elite_selection, truncate_selection, roulette_wheel_selection, \
    rank_selection, tournament_selection, boltzmann_selection
from crossbreed import simple_crossbreed, multiple_crossbreed, uniform_crossbreed
from mutation import mutation

selection_name = ["Elite", "Truncate", "Roulette Wheel", "Rank", "Tournament", "Boltzmann"]
crossbreed_name = ["Simple", "Multiple", "Uniform"]
mutation_name = ["Alta", "Media", "Baja"]


BOLTZMANN: Final = 5
with open("settings.json") as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()

selections = np.array([elite_selection, truncate_selection, roulette_wheel_selection,
                       rank_selection, tournament_selection, boltzmann_selection])
crossbreed_methods = np.array([simple_crossbreed, multiple_crossbreed, uniform_crossbreed])


def main_algorithm(selection, crossbreed, population_size, generations, t0, tc, k, mutation_type,
                   initial_population=None):
    best_gen = [1, 1]
    # Initializing and populating
    population = Population(population_size)
    if initial_population is None:
        for i in range(population_size):
            population.population.append(Individual(np.random.uniform(low=-30, high=30, size=11)))
    else:
        for i in range(len(initial_population)):
            population.population.append(initial_population[i])
    min_fitness = population.min_fitness()
    population_fitness = []

    for i in range(generations):
        children = []
        while len(children) < population_size:
            if selection == BOLTZMANN:
                parents = selections[selection](population, i, t0, tc, k, 2)
            else:
                parents = selections[selection](population, 2)
            new_children = crossbreed_methods[crossbreed](parents[0], parents[1])
            for child in new_children:
                children.append(mutation(child, mutation_type))

        for child in children:
            child.reset_fitness()
            population.population.append(child)
            population.size += 1
        if selection == BOLTZMANN:
            population.population = selections[selection](population, i, t0, tc, k, population_size)
        else:
            population.population = selections[selection](population, population_size)
        population.size = population_size

        min_fitness = population.min_fitness()
        population_fitness.append(min_fitness)
        if min_fitness < best_gen[1]:
            best_gen[0] = i
            best_gen[1] = min_fitness
    return [min_fitness, population_fitness]
