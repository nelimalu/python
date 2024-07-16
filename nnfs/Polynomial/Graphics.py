from matplotlib import pyplot as plt
from Polynomial import Polynomial
import numpy as np
from Global import *

WINDOW_SHOW_LENGTH = 1


def plot(polynomial):
	y_values = [polynomial.compute_at(x_coord) for x_coord in SPACE]
	plt.plot(SPACE, y_values)


def render():
	plt.title(f"title")
	plt.show()#block=False)
	# plt.pause(WINDOW_SHOW_LENGTH)
	# plt.close('all')
