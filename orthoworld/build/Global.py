import pygame.gfxdraw

# width and height of the window
WIDTH = 640
HEIGHT = 480

# pixel coordinate of (0, 0, 0)
ORIGIN_X = WIDTH // 2
ORIGIN_Y = HEIGHT // 3

WORLDSIZE = 3

def draw_polygon(surf, coords, colour):
	pygame.gfxdraw.filled_polygon(surf, coords, colour)
	pygame.gfxdraw.aapolygon(surf, coords, (100, 100, 100))

class Colour:
	HIGHLIGHT = 10
	SHADOW = 10

	def __init__(self, r, g, b):
		self.r = r
		self.g = g
		self.b = b

	def get(self):
		return self.r, self.b, self.g

	def get_highlight(self):
		return (
			min(255, self.r + self.HIGHLIGHT),
			min(255, self.g + self.HIGHLIGHT),
			min(255, self.b + self.HIGHLIGHT)
		)

	def get_shadow(self):
		return (
			max(0, self.r - self.SHADOW),
			max(0, self.g - self.SHADOW),
			max(0, self.b - self.SHADOW)
		)
