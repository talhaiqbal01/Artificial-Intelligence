from algorithms.genetic_algorithm.knapsack_problem.chromosome import Chromosome
import random


class Population:
    def __init__(self, size, items, max_weight):
        self.size = size
        self.items = items
        self.max_weight = max_weight
        self.individuals = self.initialize_population()

    def initialize_population(self):
        """
        Create an initial population with random chromosomes.
        :return:
        """
        return [Chromosome([random.randint(0, 1) for _ in self.items], self.items, self.max_weight) for _ in
                range(self.size)]
