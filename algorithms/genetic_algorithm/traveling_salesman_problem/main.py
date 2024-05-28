"""
Main Runner for Genetic Algorithm (Traveling Salesman Problem)
"""
import random
from algorithms.genetic_algorithm.traveling_salesman_problem.city import City
from algorithms.genetic_algorithm.traveling_salesman_problem.fitness import Fitness
from algorithms.genetic_algorithm.traveling_salesman_problem.genetic_algorithm import GeneticAlgorithm

if __name__ == "__main__":
    city_list = [City(x=int(random.random() * 200), y=int(random.random() * 200)) for _ in range(20)]
    ga = GeneticAlgorithm(population_size=100, mutation_rate=0.01, generations=500, cities=city_list)
    best_route = ga.run()
    best_distance = Fitness(best_route).route_distance()
    print(f"Best distance: {best_distance}")
    print(f"Best route: {best_route}")
