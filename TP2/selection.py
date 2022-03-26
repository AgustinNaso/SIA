def elite_selection(population):
    # sort list of individuals by fitness
    population.sort(key=lambda x: x.fitness, reverse=True)
    return population[0:population.size]

# def roulette_wheel_selection(population):
#     fitness_sum = population.fitness_sum()
#     for individual in population.population:
