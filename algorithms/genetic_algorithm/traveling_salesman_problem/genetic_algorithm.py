"""
Genetic Algorithm Class
"""
import random
import numpy as np
from algorithms.genetic_algorithm.traveling_salesman_problem.fitness import Fitness


class GeneticAlgorithm:
    def __init__(self, population_size, mutation_rate, generations, cities):
        """Initializes the genetic algorithm with parameters."""
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.generations = generations
        self.cities = cities
        self.population = self.initial_population()

    def initial_population(self):
        """Creates the initial population randomly."""
        return [random.sample(self.cities, len(self.cities)) for _ in range(self.population_size)]

    def rank_routes(self):
        """Ranks routes based on fitness scores."""
        fitness_results = {i: Fitness(self.population[i]).route_fitness() for i in range(len(self.population))}
        return sorted(fitness_results.items(), key=lambda x: x[1], reverse=True)

    def selection(self, ranked_routes):
        """Selects routes based on their fitness scores."""
        selection_results = []
        df = np.cumsum([ranked_routes[i][1] for i in range(len(ranked_routes))])
        for _ in range(self.population_size):
            pick = random.random()
            for i in range(len(ranked_routes)):
                if pick <= df[i] / df[-1]:  # Ensure normalization
                    selection_results.append(ranked_routes[i][0])
                    break
        return selection_results

    def mating_pool(self, selection_results):
        """Creates the mating pool based on selected routes."""
        return [self.population[index] for index in selection_results]

    @staticmethod
    def breed(parent1, parent2):
        """Performs crossover between two parents to create an offspring."""
        start, end = sorted(random.sample(range(len(parent1)), 2))
        child_p1 = parent1[start:end + 1]
        child_p2 = [item for item in parent2 if item not in child_p1]
        return child_p1 + child_p2

    def breed_population(self, matingpool):
        """Breeds the entire population."""
        children = []
        length = len(matingpool)
        for i in range(length):
            parent1 = matingpool[i]
            parent2 = matingpool[(i + 1) % length]
            child = self.breed(parent1, parent2)
            children.append(child)
        return children

    def mutate(self, individual):
        """Mutates an individual by swapping two cities."""
        for swapped in range(len(individual)):
            if random.random() < self.mutation_rate:
                swap_with = int(random.random() * len(individual))
                city1, city2 = individual[swapped], individual[swap_with]
                individual[swapped], individual[swap_with] = city2, city1
        return individual

    def mutate_population(self, population):
        """Mutates the entire population."""
        return [self.mutate(individual) for individual in population]

    def next_generation(self):
        """Produces the next generation."""
        ranked_routes = self.rank_routes()
        selection_results = self.selection(ranked_routes)
        matingpool = self.mating_pool(selection_results)
        children = self.breed_population(matingpool)
        next_generation = self.mutate_population(children)
        return next_generation

    def run(self):
        """Runs the genetic algorithm for the specified number of generations."""
        for _ in range(self.generations):
            self.population = self.next_generation()
        best_route_index = self.rank_routes()[0][0]
        return self.population[best_route_index]
