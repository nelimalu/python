from matplotlib import pyplot as plt
from Polynomial import Polynomial
import numpy as np
from Global import *
import Graphics
from Generation import Generation


def main():
	generations = [Generation(0)]
	generational_best = None
	# Graphics.render()

	for i in range(1, NUM_GENERATIONS + 1):
		best_in_current_generation = generations[-1].get_best_genome()

		#print(best_in_current_generation.get_score())
		Graphics.plot_generation(generations[-1])
		Graphics.plot(best_in_current_generation.get_polynomial(), color="red")
		Graphics.plot(GOAL, color='blue')
		Graphics.update(i)

		if generational_best is None or best_in_current_generation.get_score() < generational_best.get_score():
			generational_best = best_in_current_generation

		print(generational_best.get_score())

		generations.append(
			Generation(i, generational_best)
		)

	print(generations[-1].get_best_genome().get_polynomial().get_coeffs())


if __name__ == "__main__":
	main()
