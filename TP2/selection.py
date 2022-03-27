import random
import math

STOCHASTIC = "stochastic"
ROULETTE = "roulette"
RANK = "rank"
BOLTZMANN = "boltzmann"


def elite_selection(population):
    # sort list of individuals by fitness
    population.sort(key=lambda x: x.fitness, reverse=True)
    return population[0:population.size]


# based upon fitness proportional selection but made fairer
def stochastic_selection(population):
    fitness = []
    for individual in population:
        fitness.append(individual.fitness)
    return select_population(STOCHASTIC, population, fitness)


def truncate_selection(population):
    population.sort(key=lambda x: x.fitness, reverse=True)
    truncated = population[0:population.size * 0.9]
    return random.sample(truncated, population.size)


def roulette_wheel_selection(population):
    fitness_sum = population.fitness_sum()
    probabilities = []
    for individual in population.population:
        probabilities.append(individual.fitness / fitness_sum)
    return select_population(ROULETTE, population, probabilities)


def rank_selection(population):
    population.sort(key=lambda x: x.fitness, reverse=True)
    probabilities = []
    for i in range(population.size):
        probabilities.append((i + 1 + population.size) / population.size)
    return select_population(RANK, population, probabilities)


def select_population(method, population, probabilities):
    selected = set()
    while len(selected) < population.size:
        i = 0
        if method == (ROULETTE or RANK or BOLTZMANN):
            p = random.uniform(0, 1)
        else:
            p = random.uniform(0, population.fitness_sum)
        current = probabilities[i]
        while p > current:
            p -= current
            i += 1
            current = probabilities[i]
        selected.add(population.population[i])
    return selected


def tournament_selection(population):
    selected = set()
    while len(selected) < population.size:
        u = random.uniform(0.5, 1)
        r = random.uniform(0, 1)
        couples = random.sample(population, 4)
        if r < u:
            first_winner = couples[0].get_max_fitness(couples[1])
            second_winner = couples[2].get_max_fitness(couples[3])
            selected.add(first_winner.get_max_fitness(second_winner))
        else:
            first_winner = couples[0].get_min_fitness(couples[1])
            second_winner = couples[2].get_min_fitness(couples[3])
            selected.add(first_winner.get_min_fitness(second_winner))


def boltzmann_selection(population, t, t0, tc, k):
    probabilities = []
    temp = get_temperature(t, t0, tc, k)
    total = boltzmann_get_sum(population, temp)
    for individual in population:
        probabilities.append(math.exp(individual.fitness/temp)/total)
    return select_population(BOLTZMANN, population, probabilities)


def get_temperature(t, t0, tc, k):
    return tc + (t0 - tc) * math.exp(-k * t)


def boltzmann_get_sum(population, temp):
    total = 0
    for individual in population:
        total += math.exp(individual.fitness/temp)
    return total
