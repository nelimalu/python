from matplotlib import pyplot as plt
from Polynomial import Polynomial
import numpy as np
from Global import *
import Graphics
from Generation import Generation


def main():
	generation = Generation()
	print(generation.get_best_genome().get_score())

	Graphics.plot(GOAL, color='blue')
	Graphics.plot_generation(generation)
	Graphics.render()


if __name__ == "__main__":
	main()
