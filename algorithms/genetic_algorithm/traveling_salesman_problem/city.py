"""
City Class
"""
import numpy as np


class City:
    def __init__(self, x, y):
        """
        Initializes a city with x and y coordinates.
        :param x:
        :param y:
        """
        self.x = x
        self.y = y

    def distance_to(self, city):
        """Calculates the distance between this city and another city."""
        return np.sqrt((self.x - city.x) ** 2 + (self.y - city.y) ** 2)

    def __repr__(self):
        """String representation of a city."""
        return f"({self.x}, {self.y})"
