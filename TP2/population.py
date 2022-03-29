from operator import attrgetter


class Population:
    def __init__(self, size):
        self.size = size
        self.population = []
        self.generation = 0

    def min_fitness(self):
        return min(self.population, key=attrgetter('real_fitness')).real_fitness

    def fitness_sum(self):
        return float(sum(individual.fitness for individual in self.population))

    def sort_desc(self):
        self.population.sort(key=lambda x: x.fitness, reverse=True)

    def print_fitness(self):
        string = ""
        for individual in self.population:
            string += str(individual.fitness) + " "
        print(string)
