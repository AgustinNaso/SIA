from operator import attrgetter


class Population:
    def __init__(self, size):
        self.size = size
        self.population = []
        self.generation = 0

    def add_individual(self, individual):
        self.population.append(individual)
        return

    def min_fitness(self):
        return min(self.population, key=attrgetter('real_fitness')).real_fitness

    def set_new_population(self, new_population):
        self.population = new_population
        return

    def fitness_sum(self):
        return float(sum(individual.fitness for individual in self.population))

    def new_generation(self):
        self.generation += 1
        return

    def sort_desc(self):
        self.population.sort(key=lambda x: x.fitness, reverse=True)
