from operator import attrgetter


class Population:
    def __init__(self, size):
        self.size = size
        self.population = []
        self.generation = 0

    def max_fitness(self):
        return max(self.population, key=attrgetter('fitness')).fitness

    def fitness_sum(self):
        return float(sum(individual.fitness for individual in self.population))

    def sort_desc(self):
        new_population = self.population.copy()
        new_population.sort(key=lambda x: x.fitness, reverse=True)
        return new_population

    def print_fitness(self):
        string = ""
        for individual in self.population:
            string += str(individual.fitness) + " "
        print(string)
