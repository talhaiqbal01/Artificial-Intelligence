"""
Fitness Class
"""


class Fitness:
    def __init__(self, route):
        """
        Initializes fitness calculation for a given route.
        :param route:
        """
        self.route = route
        self.distance = 0
        self.fitness = 0.0

    def route_distance(self):
        """
        Calculates total distance of the route.
        :return:
        """
        if self.distance == 0:
            for i in range(len(self.route)):
                from_city = self.route[i]
                to_city = self.route[(i + 1) % len(self.route)]
                self.distance += from_city.distance_to(to_city)
        return self.distance

    def route_fitness(self):
        """
        Calculates fitness score of the route (inverse of distance).
        :return:
        """
        if self.fitness == 0:
            self.fitness = 1 / float(self.route_distance())
        return self.fitness
