"""
Chromosome Class
"""


class Chromosome:
    def __init__(self, genes, items, max_weight):
        self.genes = genes
        self.items = items
        self.max_weight = max_weight
        self.fitness = self.calculate_fitness()

    def calculate_fitness(self):
        """
        Calculate the fitness based on total value and weight constraint.
        :return:
        """
        total_weight = sum(gene * item['weight'] for gene, item in zip(self.genes, self.items))
        if total_weight > self.max_weight:
            return 0  # Invalid solution
        total_value = sum(gene * item['value'] for gene, item in zip(self.genes, self.items))
        return total_value
