class Population:
    def __init__(self, size):
        self.size = size
        self.population = []
        self.generation = 0

    def add_individual(self, individual):
        self.population.append(individual)
        return

    def fitness_sum(self):
        return float(sum(individual.fitness for individual in self.population))

    def new_generation(self):
        self.generation += 1
        return
