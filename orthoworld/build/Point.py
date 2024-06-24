class Point:
	def __init__(self, x: int, y: int):
		self.x: int = x
		self.y: int = y

	def get(self):
		return self.x, self.y

	def get_x(self):
		return self.x

	def get_y(self):
		return self.y

	def __str__(self):
		return f"x: {self.x} y: {self.y}"