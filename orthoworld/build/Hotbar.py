from Global import *

class Hotbar:
	BOX_SIZE = 30
	MARGIN = 3

	def __init__(self):
		self.selected_colour = Colour(128,128,128)
		self.colours = [
			(50,202,205),  # blue
			(255,205,172),  # brown
			(139,192,162),  # green
			(255,255,255),  # white
			(128,128,128),  # gray
			(20,20,20),  # black
			(254,152,140)  # red
		]
		self.width = (self.BOX_SIZE + self.MARGIN) * len(self.colours) + self.MARGIN
		self.x = WIDTH // 2 - self.width // 2
		self.height = self.BOX_SIZE + 2 * self.MARGIN
		self.y = HEIGHT - self.height

	def get_colour(self, mousepos):
		for i, colour in enumerate(self.colours):
			x = self.x + self.MARGIN * (i + 1) + self.BOX_SIZE * i
			y = self.y + self.MARGIN
			if x <= mousepos[0] <= x + self.BOX_SIZE and y <= mousepos[1] <= y + self.BOX_SIZE:
				return colour

		return None


	def draw(self, win):
		# pygame.draw.rect(win, (160, 160, 160), (self.x, self.y, self.width, self.height))
		for i, colour in enumerate(self.colours):
			if colour == self.selected_colour.get():
				pygame.draw.rect(win, self.selected_colour.shadow_copy().get(), (
					self.x + (self.MARGIN + self.BOX_SIZE) * i,
					self.y,
					self.BOX_SIZE + 2 * self.MARGIN,
					self.BOX_SIZE + 2 * self.MARGIN
				))
			pygame.draw.rect(win, colour, (
				self.x + self.MARGIN * (i + 1) + self.BOX_SIZE * i,
				self.y + self.MARGIN,
				self.BOX_SIZE,
				self.BOX_SIZE
			))
