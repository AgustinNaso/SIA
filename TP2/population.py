from operator import attrgetter


class Population:
    def __init__(self, size):
        self.size = size
        self.population = []
        self.generation = 0

    def min_fitness(self):
        return min(self.population, key=attrgetter('fitness')).fitness

    def fitness_sum(self):
        return float(sum((1 / (1 + individual.fitness)) for individual in self.population))

    def sort(self):
        new_population = self.population.copy()
        new_population.sort(key=lambda x: x.fitness)
        return new_population

    def print_fitness(self):
        string = ""
        for individual in self.population:
            string += str(individual.fitness) + " "
        print(string)
