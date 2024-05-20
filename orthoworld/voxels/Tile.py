import pygame.gfxdraw
from random import randint
import Renderer
import Global

class Tile:
	def __init__(self, x: int, y: int, gridsize: int, parent):
		self.x: int = x
		self.y: int = y
		self.is_left_edge = x == gridsize - 1
		self.is_right_edge = y == gridsize - 1
		self.colour = (128,128,128)
		self.parent = parent
		self.tileheight = parent.tileheight * 1.5
		self.height = -randint(0, 0) * self.tileheight
		self.top_points = self.find_top_points()

	def find_top_points(self):
		render_x = self.parent.origin[0] - (self.x * self.parent.tilewidth) + (self.y * self.parent.tilewidth)
		render_y = self.parent.origin[1] + (self.x * self.parent.tileheight) + ((self.y) * self.parent.tileheight)

		return [
			(render_x, render_y + self.height),
			(render_x - self.parent.tilewidth, render_y + self.parent.tileheight + self.height),
			(render_x, render_y + 2 * self.parent.tileheight + self.height),
			(render_x + self.parent.tilewidth, render_y + self.parent.tileheight + self.height)
		]



	def render(self, win, hover):
		render_x = self.parent.origin[0] - (self.x * self.parent.tilewidth) + (self.y * self.parent.tilewidth)
		render_y = self.parent.origin[1] + (self.x * self.parent.tileheight) + ((self.y) * self.parent.tileheight)

		if hover:
			self.colour = (128, 40, 40)
		else:
			self.colour = (128,128,128)

		# render top
		Renderer.polygon(win, self.colour, self.top_points)
		self.render_sides(win, render_x, render_y)


	def render_sides(self, win, render_x, render_y):
		# render left side
		Renderer.polygon(win, Global.add(self.colour, (20, 20, 20)), [
			(render_x - self.parent.tilewidth, render_y + self.parent.tileheight + self.height),
			(render_x, render_y + 2 * self.parent.tileheight + self.height),
			(render_x, render_y + 2 * self.parent.tileheight + self.tileheight + self.height),
			(render_x - self.parent.tilewidth, render_y + self.parent.tileheight + self.tileheight + self.height)
		])

		# render right side
		Renderer.polygon(win, Global.add(self.colour, (-20, -20, -20)), [
			(render_x + self.parent.tilewidth, render_y + self.parent.tileheight + self.height),
			(render_x, render_y + 2 * self.parent.tileheight + self.height),
			(render_x, render_y + 2 * self.parent.tileheight + self.tileheight + self.height),
			(render_x + self.parent.tilewidth, render_y + self.parent.tileheight + self.tileheight + self.height)
		])



