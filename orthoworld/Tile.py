import pygame.gfxdraw
from random import randint
import Renderer

class Tile:
	def __init__(self, x: int, y: int, gridsize: int, noise_value):
		self.x: int = x
		self.y: int = y
		self.is_left_edge = x == gridsize - 1
		self.is_right_edge = y == gridsize - 1
		self.height = -(noise_value * 100)
		self.colour = self.pick_colour(noise_value)

	def pick_colour(self, noise_value):
		if noise_value > 0.4:
			return Renderer.colour_depth((200, 200, 200), noise_value)
		if noise_value > 0.2:
			return Renderer.colour_depth((179, 179, 179), noise_value)
		elif noise_value > -0.02:
			return Renderer.colour_depth((96, 158, 108), noise_value)
		elif noise_value > -0.1:
			return Renderer.colour_depth((209, 205, 155), noise_value)
		else:
			self.height = 5
			return Renderer.colour_depth((126, 158, 207), noise_value)


	def render(self, win, origin: tuple[int, int], tilewidth: int, tileheight: int):
		render_x = origin[0] - (self.x * tilewidth) + (self.y * tilewidth)
		render_y = origin[1] + (self.x * tileheight) + ((self.y) * tileheight)

		points = [
			(render_x, render_y + self.height),
			(render_x - tilewidth, render_y + tileheight + self.height),
			(render_x, render_y + 2 * tileheight + self.height),
			(render_x + tilewidth, render_y + tileheight + self.height)
		]

		Renderer.polygon(win, self.colour, points)
		self.render_sides(win, render_x, render_y, tilewidth, tileheight)


	def render_sides(self, win, render_x, render_y, tilewidth, tileheight):
		Renderer.polygon(win, self.colour, [
			(render_x - tilewidth, render_y + tileheight + self.height),
			(render_x, render_y + 2 * tileheight + self.height),
			(render_x, render_y + 2 * tileheight + 30 + self.height),
			(render_x - tilewidth, render_y + tileheight + 30 + self.height)
		])

		Renderer.polygon(win, self.colour, [
			(render_x + tilewidth, render_y + tileheight + self.height),
			(render_x, render_y + 2 * tileheight + self.height),
			(render_x, render_y + 2 * tileheight + 30 + self.height),
			(render_x + tilewidth, render_y + tileheight + 30 + self.height)
		])



