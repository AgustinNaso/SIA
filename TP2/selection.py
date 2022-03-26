import random


def elite_selection(population):
    # sort list of individuals by fitness
    population.sort(key=lambda x: x.fitness, reverse=True)
    return population[0:population.size]


def roulette_wheel_selection(population):
    fitness_sum = population.fitness_sum()
    probabilities = []
    for individual in population.population:
        probabilities.append(individual.fitness / fitness_sum)
    return select_pupolation(population, probabilities)


def rank_selection(population):
    population.sort(key=lambda x: x.fitness, reverse=True)
    fitness_sum = population.fitness_sum()
    probabilities = []
    for individual in population.population:
        probabilities.append((individual.fitness + fitness_sum) / fitness_sum)
    return select_pupolation(population, probabilities)


def select_pupolation(population, probabilities):
    selected = set()
    n = len(selected)
    while n < population.size:
        i = 0
        p = random.random()
        current = probabilities[i]
        while p > current:
            p -= current
            i += 1
            current = probabilities[i]
        selected.add(population.population[i])
        n = len(selected)
    return selected
