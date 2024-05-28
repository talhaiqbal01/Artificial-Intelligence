"""
Genetic Algorithm Class
"""
import random
from algorithms.genetic_algorithm.knapsack_problem.chromosome import Chromosome


class GeneticAlgorithm:
    def __init__(self, population, mutation_rate, generations):
        self.population = population
        self.mutation_rate = mutation_rate
        self.generations = generations

    def selection(self):
        """
        Select the fittest individuals to be parents.
        :return:
        """
        sorted_population = sorted(self.population.individuals, key=lambda x: x.fitness, reverse=True)
        return sorted_population[:2]

    def crossover(self, parent1, parent2):
        """
        Perform crossover between two parents to produce a child.
        :param parent1:
        :param parent2:
        :return:
        """
        crossover_point = random.randint(1, len(parent1.genes) - 1)
        child_genes = parent1.genes[:crossover_point] + parent2.genes[crossover_point:]
        return Chromosome(child_genes, self.population.items, self.population.max_weight)

    def mutate(self, individual):
        """
        Mutate an individual's genes by flipping a random bit.
        :param individual:
        :return:
        """
        if random.random() < self.mutation_rate:
            index = random.randint(0, len(individual.genes) - 1)
            individual.genes[index] = 1 - individual.genes[index]
        individual.fitness = individual.calculate_fitness()

    def run(self):
        """
        Run the genetic algorithm for a specified number of generations.
        :return:
        """
        for _ in range(self.generations):
            new_population = []
            parent1, parent2 = self.selection()
            for _ in range(self.population.size // 2):
                child1 = self.crossover(parent1, parent2)
                child2 = self.crossover(parent2, parent1)
                self.mutate(child1)
                self.mutate(child2)
                new_population.extend([child1, child2])
            self.population.individuals = new_population
        best_individual = max(self.population.individuals, key=lambda x: x.fitness)
        return best_individual
