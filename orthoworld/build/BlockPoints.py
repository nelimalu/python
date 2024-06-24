from Point import Point

class BlockPoints:
	def __init__(self, key_points: tuple):
		self.origin = key_points[0]
		self.surface_front = key_points[1]
		self.surface_left = key_points[2]
		self.surface_right = key_points[3]
		self.side_left = key_points[4]
		self.side_center = key_points[5]
		self.side_right = key_points[6]
