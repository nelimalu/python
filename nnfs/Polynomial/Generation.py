from Global import *
import random
from Genome import Genome
from Polynomial import Polynomial
from operator import attrgetter


class Generation:
	def __init__(self, prev_generation=None):
		self.prev_generation = prev_generation
		self.genomes = self.generate_genomes(prev_generation)
		self.best_genome = self.evaluate_genomes()

	def generate_genomes(self, prev_generation):
		if prev_generation is None:
			return [self.generate_random_genome() for _ in range(NUM_GENOMES)]
		return [self.generate_genome(prev_generation.get_best_genome()) for _ in range(NUM_GENOMES)]

	def generate_random_genome(self):
		return Genome(
			Polynomial(*[
				random.uniform(-GENERATIVE_MAXIMA, GENERATIVE_MAXIMA) for x in range(len(GOAL.get_coeffs()))
			])
		)

	def generate_genome(self, ancestor):
		return Genome(
			Polynomial(*[
				random.uniform(
					-ancestor.get_score(),
					ancestor.get_score()
				) for x in range(len(GOAL.get_coeffs()))
			])
		)

	def evaluate_genomes(self):
		return max(self.genomes, key=attrgetter('score'))

	def get_best_genome(self):
		return self.best_genome

	def get_genomes(self):
		return self.genomes


