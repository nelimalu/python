from matplotlib import pyplot as plt
from Polynomial import Polynomial
import numpy as np
from Global import *

WINDOW_SHOW_LENGTH = 1


def plot(polynomial, color='black'):
	y_values = [polynomial.compute_at(x_coord) for x_coord in SPACE]
	plt.plot(SPACE, y_values, color=color)


def render():
	plt.title(f"title")
	plt.show()#block=False)
	# plt.pause(WINDOW_SHOW_LENGTH)
	# plt.close('all')


def plot_generation(generation):
	for genome in generation.get_genomes():
		plot(genome.get_polynomial())
