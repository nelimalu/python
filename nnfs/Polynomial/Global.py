import numpy as np
from Polynomial import Polynomial

WORKING_RANGE = (-10, 10)
COMPUTED_RANGE = WORKING_RANGE[1] - WORKING_RANGE[0]
SPACE = np.linspace(WORKING_RANGE[0], WORKING_RANGE[1], COMPUTED_RANGE)
GOAL = Polynomial(1, 0, 0)
