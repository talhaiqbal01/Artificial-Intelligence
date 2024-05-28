"""
Main Runner of the Genetic Algorithm (Knapsack Problem)
"""
from algorithms.genetic_algorithm.knapsack_problem.population import Population
from algorithms.genetic_algorithm.knapsack_problem.genetic_algorithm import GeneticAlgorithm

items = [
    {"weight": 10, "value": 60},
    {"weight": 20, "value": 100},
    {"weight": 30, "value": 120},
]
max_weight = 50
population_size = 100
mutation_rate = 0.01
generations = 500

if __name__ == "__main__":
    initial_population = Population(population_size, items, max_weight)
    ga = GeneticAlgorithm(initial_population, mutation_rate, generations)

    best_individual = ga.run()
    print("Best solution found:", best_individual.genes)
    print("Total value:", best_individual.fitness)
