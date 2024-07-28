from Global import *
import random
from Genome import Genome
from Polynomial import Polynomial
from operator import attrgetter


class Generation:
	def __init__(self, current_generation, prev_generation=None):
		self.prev_generation = prev_generation
		self.genomes = self.generate_genomes(prev_generation, current_generation)
		self.best_genome = self.evaluate_genomes()

	def generate_genomes(self, prev_best, current_generation):
		if prev_best is None:
			return [self.generate_random_genome() for _ in range(NUM_GENOMES)]
		return [self.generate_genome(prev_best, current_generation) for _ in range(NUM_GENOMES)]

	def generate_random_genome(self):
		return Genome(
			Polynomial(*[
				random.uniform(-GENERATIVE_MAXIMA, GENERATIVE_MAXIMA) for x in range(len(GOAL.get_coeffs()))
			])
		)

	def generate_genome(self, ancestor, current_generation):
		return Genome(
			Polynomial(*[
				ancestor.get_polynomial().get_coeffs()[x] + self.algorithm(ancestor, current_generation)
				 for x in range(len(GOAL.get_coeffs()))
			])
		)

	def evaluate_genomes(self):
		return min(self.genomes, key=attrgetter('score'))

	def get_best_genome(self):
		return self.best_genome

	def get_genomes(self):
		return self.genomes

	def algorithm(self, ancestor, current_generation):
		if current_generation < NUM_GENERATIONS // 4:
			return self.gauss_algorithm(ancestor)
		elif current_generation < NUM_GENERATIONS // 2:
			return self.uniform_algorithm(ancestor)
		else:
			return self.quadratic_algorithm(ancestor)


	def uniform_algorithm(self, ancestor):
		return random.uniform(
			-1 / ancestor.get_score(),
			1 / ancestor.get_score()
		)

	def quadratic_algorithm(self, ancestor):
		return random.uniform(
			-ancestor.get_score() ** 2,
			ancestor.get_score() ** 2
		)

	def gauss_algorithm(self, ancestor):
		return random.gauss(
			0,
			sigmoid(ancestor.get_score())
		)


