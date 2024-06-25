from Global import *
from Point import Point
from BlockPoints import BlockPoints
import pygame
import pygame.gfxdraw

class Block:
	DIAGONAL_LENGTH = 80  # diagonal distance along the top face of the block
	HALF_DIAG = DIAGONAL_LENGTH // 2
	QUARTER_DIAG = DIAGONAL_LENGTH // 4


	def __init__(self, x: int, y: int, z: int, colour=Colour(128,128,128)):
		self.x: int = x
		self.y: int = y
		self.z: int = z
		self.colour = colour
		self.default_colour = colour
		self.points: BlockPoints = self.get_key_points()
		self.active_side = None

	def get_coords(self):
		return self.x, self.y, self.z


	def get_origin(self):  # returns the location of the uppermost pixel
		x = ORIGIN_X
		y = ORIGIN_Y  # might need to deepcopy

		y -= self.y * self.HALF_DIAG
		y += (self.x + self.z) * (self.QUARTER_DIAG)
		x -= self.x * (self.HALF_DIAG)
		x += self.z * (self.HALF_DIAG)

		return Point(x, y)

	def get_key_points(self):
		origin = self.get_origin()  # basically surface back
		surface_front = Point(origin.x, origin.y + self.HALF_DIAG)
		surface_left = Point(origin.x - self.HALF_DIAG, origin.y + self.QUARTER_DIAG)
		surface_right = Point(origin.x + self.HALF_DIAG, origin.y + self.QUARTER_DIAG)
		side_left = Point(surface_left.x, surface_left.y + self.HALF_DIAG)
		side_center = Point(surface_front.x, surface_front.y + self.HALF_DIAG)
		side_right = Point(surface_right.x, surface_right.y + self.HALF_DIAG)

		return BlockPoints((origin, surface_front, surface_left, surface_right, side_left, side_center, side_right))


	def draw(self, win):
		# draw top of box
		draw_polygon(win, (
			self.points.origin.get(),
			self.points.surface_left.get(),
			self.points.surface_front.get(),
			self.points.surface_right.get()
		), self.colour.get())

		# draw left side of box
		draw_polygon(win, (
			self.points.surface_left.get(),
			self.points.surface_front.get(),
			self.points.side_center.get(),
			self.points.side_left.get()
		), self.colour.get_highlight())

		# draw right side of box
		draw_polygon(win, (
			self.points.surface_right.get(),
			self.points.surface_front.get(),
			self.points.side_center.get(),
			self.points.side_right.get()
		), self.colour.get_shadow())



