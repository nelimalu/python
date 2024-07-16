class Polynomial:
	def __init__(self, *args):
		self.coefficients = args;

	def compute_at(self, x):
		# sick one liner
		# return sum([lambda n, coefficient: coefficient * (x ** n) for n, coefficient in enumerate(self.coefficients[::-1])])

		y = 0
		for n, coefficient in enumerate(self.coefficients[::-1]):
			y += coefficient * (x ** n)
		return y

	def get_coeffs(self):
		return self.coefficients

	def __str__(self):
		return " + ".join([f"{coeff}x^{len(self.coefficients) - n - 1}" for n, coeff in enumerate(self.coefficients)])

