from typing import List
import numpy as np
from numpy.random import random

from genetic_algorithm.Individuals.individual import Individual


class ScalingSelection:
    @staticmethod
    def select(population: List[Individual]) -> List[Individual]:
        # Calcular la escala de ajuste
        scaling_factor = 2.0 * len(population)

        # Calcular el ajuste acumulado
        cumulative_adjustment = 0.0
        cumulative_adjustments = []
        for individual in population:
            cumulative_adjustment += scaling_factor * individual.fitness
            cumulative_adjustments.append(cumulative_adjustment)

        # Seleccionar n+1 individuos usando el método de escalado
        selected_parents = []
        while len(selected_parents) < len(population) + 1:
            threshold = cumulative_adjustments[-1] * random()
            index = next(
                i
                for i, adjustment in enumerate(cumulative_adjustments)
                if adjustment >= threshold
            )
            new_parent = population[index]

            # Verificar que el nuevo padre sea diferente del último padre seleccionado
            if not selected_parents or not np.array_equal(
                new_parent.genotype, selected_parents[-1].genotype
            ):
                selected_parents.append(new_parent)

        return selected_parents
