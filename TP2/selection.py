import random
import math
from typing import Final

BOLTZMANN: Final = 5



def elite_selection(population, size):
    # sort list of individuals by fitness
    new_population = population.sort()
    return new_population[0:size]


# based upon fitness proportional selection but made fairer
# def stochastic_selection(population, size):
#     sums = [0]
#     total = 0
#     for individual in population.population:
#         total += individual.fitness
#         sums.append(total)
#     return select_population(population.population, sums, size)


def truncate_selection(population, size):
    new_population = population.sort()
    truncated = new_population[0:math.ceil(population.size * 0.9)]
    return random.choices(truncated, k=size)


def roulette_wheel_selection(population, size):
    fitness_sum = population.fitness_sum()
    sums = [0]
    total = 0
    for individual in population.population:
        total += (1 / (1 + individual.fitness)) / fitness_sum
        sums.append(total)
    return select_population(population.population, sums, size)


def rank_selection(population, size):
    new_population = population.sort()
    sums = [0]
    f1 = []
    total_f1 = 0
    for i in range(population.size):
        f1i = (population.size - (i + 1)) / population.size
        total_f1 += f1i
        f1.append(f1i)
    total = 0
    for fi in f1:
        total += fi/total_f1
        sums.append(total)
    return select_population(new_population, sums, size)


def select_population(population, sums, size):
    selected = []
    while len(selected) < size:
        p = random.uniform(0, 1)
        for i in range(len(population)):
            if sums[i] < p <= sums[i + 1]:
                selected.append(population[i])
    return selected


def tournament_selection(population, size):
    selected = []
    while len(selected) < size:
        u = random.uniform(0.5, 1)
        r = random.uniform(0, 1)
        couples = random.sample(population.population, 4)
        if r < u:
            first_winner = couples[0].get_max_fitness(couples[1])
            second_winner = couples[2].get_max_fitness(couples[3])
            selected.append(first_winner.get_max_fitness(second_winner))
        else:
            first_winner = couples[0].get_min_fitness(couples[1])
            second_winner = couples[2].get_min_fitness(couples[3])
            selected.append(first_winner.get_min_fitness(second_winner))
    return selected


def boltzmann_selection(population, t, t0, tc, k, size):
    sums = [0]
    total = 0
    temp = get_temperature(t, t0, tc, k)
    boltzmann_sum = boltzmann_get_sum(population, temp)
    for individual in population.population:
        total += math.exp((1 / (1 + individual.fitness))/temp)/boltzmann_sum
        sums.append(total)
    return select_population(population.population, sums, size)


def get_temperature(t, t0, tc, k):
    return tc + (t0 - tc) * math.exp(-k * t)


def boltzmann_get_sum(population, temp):
    total = 0
    for individual in population.population:
        total += math.exp((1 / (1 + individual.fitness))/temp)
    return total


# test_population = Population(10)
# for i in range(test_population.size):
#     individual = Individual(np.random.uniform(low=-30, high=30, size=11))
#     test_population.population.append(individual)
# test_population.print_fitness()
# new_population = roulette_wheel_selection(test_population, 5)
# print("----------")
# for individual in new_population:
#     print(individual.fitness)
