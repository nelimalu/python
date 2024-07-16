import numpy as np
from matplotlib import pyplot as plt
import math
from random import randint, random
from time import sleep

WORKING_RANGE = (-10, 10)
COMPUTED_RANGE = WORKING_RANGE[1] - WORKING_RANGE[0]
SPACE = np.linspace(WORKING_RANGE[0], WORKING_RANGE[1], COMPUTED_RANGE)
GENERATION_SKIP = 10
COMPUTE_GENERATIONS = 100
TRAINING_FUNCTION_COEFFS = [2, 0, 0]
NUM_GENOMES = 1


def sigmoid(x):
	try:
		return abs(2 / (1 + (math.e ** (-x))) - 1)
	except OverflowError:
		return 0


def poly_coefficients(coeffs):
	o = len(coeffs)
	y = 0
	for i in range(o):
		y += coeffs[i] * SPACE ** i
	return y


def compute_function(x, network):
	y = 0
	for power, coefficient in enumerate(network[::-1]):
		y += coefficient * (x ** power)
	return y


def grade_network(network, goal):
	score = 0
	for i in range(WORKING_RANGE[0], WORKING_RANGE[1] + 1):
		achieved = compute_function(i, network)
		required = compute_function(i, goal)
		print("aaa", achieved, required)
		score += sigmoid(required - achieved)

	return score / COMPUTED_RANGE


def update_network(network, score):
	new_network = [0 for i in range(len(network))]
	for i, coeff in enumerate(network):
		new_network[i] = coeff + (1 - score) * random() * 2
	return new_network


def regenerate_networks(network, score):
	return [update_network(network, score) for i in range(NUM_GENOMES)]


# plt.plot(x, poly_coefficients(coeffs[::-1]))
# plt.show()

def main():
	networks = [
		[randint(-5, 5) for j in range(len(TRAINING_FUNCTION_COEFFS))] for i in range(NUM_GENOMES)
	]

	for generation in range(COMPUTE_GENERATIONS):
		best_score = 0
		best_index = 0
		for i, network in enumerate(networks):
			score = grade_network(network, TRAINING_FUNCTION_COEFFS)
			print(score)
			if score < best_score:
				best_score = score
				best_index = i

			if generation % GENERATION_SKIP == 0:
				plt.plot(SPACE, poly_coefficients(networks[i][::-1]))

		# networks[i] = update_network(network, score)
		networks = regenerate_networks(networks[best_index], best_score)
			

		if generation % GENERATION_SKIP == 0:
			plt.plot(SPACE, poly_coefficients(TRAINING_FUNCTION_COEFFS[::-1]))
			plt.title(f"Gen. {generation}")
			plt.show(block=False)
			plt.pause(1)
			plt.close('all')


main()
