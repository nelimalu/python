import numpy as np
from Polynomial import Polynomial
import math

WORKING_RANGE = (-10, 10)
COMPUTED_RANGE = WORKING_RANGE[1] - WORKING_RANGE[0]
SPACE = np.linspace(WORKING_RANGE[0], WORKING_RANGE[1], COMPUTED_RANGE)
GOAL = Polynomial(9/5, 32)
GENERATIVE_MAXIMA = max(GOAL.get_coeffs())

NUM_GENOMES = 50
NUM_GENERATIONS = 200

def sigmoid(x):
  return (2 / (1 + math.exp(-x))) - 1
