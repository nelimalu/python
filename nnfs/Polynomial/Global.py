import numpy as np
from Polynomial import Polynomial

WORKING_RANGE = (-10, 10)
COMPUTED_RANGE = WORKING_RANGE[1] - WORKING_RANGE[0]
SPACE = np.linspace(WORKING_RANGE[0], WORKING_RANGE[1], COMPUTED_RANGE)
GOAL = Polynomial(1, 0, 0)
GENERATIVE_MAXIMA = max(GOAL.get_coeffs())

NUM_GENOMES = 1
NUM_GENERATIONS = 1
