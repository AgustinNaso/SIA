import random
import math
import numpy as np

from TP2.individual import Individual
from population import Population


def elite_selection(population, size):
    # sort list of individuals by fitness
    new_population = population.population.copy()
    new_population.sort(key=lambda x: x.fitness, reverse=True)
    return new_population[0:size]


# based upon fitness proportional selection but made fairer
def stochastic_selection(population, size):
    sums = [0]
    total = 0
    for individual in population.population:
        total += individual.fitness
        sums.append(total)
    return select_population(population, sums, size)


def truncate_selection(population, size):
    new_population = population.population.copy()
    new_population.sort(key=lambda x: x.fitness, reverse=True)
    truncated = new_population[0:math.ceil(len(new_population) * 0.9)]
    return random.choices(truncated, k=size)


def roulette_wheel_selection(population, size):
    fitness_sum = population.fitness_sum()
    sums = [0]
    total = 0
    for individual in population.population:
        total += individual.fitness / fitness_sum
        sums.append(total)
    return select_population(population, sums, size)


def rank_selection(population, size):
    population.sort_desc()
    sums = [0]
    total = 0
    for i in range(population.size):
        total += (i + 1 + population.size) / population.size
        sums.append(total)
    return select_population(population, sums, size)


def select_population(population, sums, size):
    selected = set()
    while len(selected) < size:
        p = random.uniform(0, sums[population.size])
        for i in range(population.size):
            if sums[i] < p <= sums[i + 1]:
                selected.add(population.population[i])
    return list(selected)


def tournament_selection(population, size):
    selected = set()
    while len(selected) < size:
        u = random.uniform(0.5, 1)
        r = random.uniform(0, 1)
        couples = random.sample(population.population, 4)
        if r < u:
            first_winner = couples[0].get_max_fitness(couples[1])
            second_winner = couples[2].get_max_fitness(couples[3])
            selected.add(first_winner.get_max_fitness(second_winner))
        else:
            first_winner = couples[0].get_min_fitness(couples[1])
            second_winner = couples[2].get_min_fitness(couples[3])
            selected.add(first_winner.get_min_fitness(second_winner))
    return list(selected)


def boltzmann_selection(population, t, t0, tc, k, size):
    sums = [0]
    total = 0
    temp = get_temperature(t, t0, tc, k)
    boltzmann_sum = boltzmann_get_sum(population, temp)
    for individual in population.population:
        total += math.exp(individual.fitness/temp)/boltzmann_sum
        sums.append(total)
    return select_population(population, sums, size)


def get_temperature(t, t0, tc, k):
    return tc + (t0 - tc) * math.exp(-k * t)


def boltzmann_get_sum(population, temp):
    total = 0
    for individual in population.population:
        total += math.exp(individual.fitness/temp)
    return total


# test_population = Population(10)
# for i in range(test_population.size):
#     individual = Individual(np.random.randn(11))
#     test_population.population.append(individual)
# test_population.print_fitness()
# new_population = tournament_selection(test_population, 5)
# print("----------")
# for individual in new_population:
#     print(individual.fitness)
