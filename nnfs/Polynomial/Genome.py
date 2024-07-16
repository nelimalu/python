from Global import *


class Genome:
	def __init__(self, polynomial):
		self.polynomial = polynomial
		self.score = self.evaluate()

	def evaluate(self):
		total_error = 0
		for x_coord in SPACE:
			total_error += abs(self.polynomial.compute_at(x_coord) - GOAL.compute_at(x_coord))
		return total_error

	def get_polynomial(self):
		return self.polynomial

	def get_score(self):
		return self.score
