from Tile import Tile
import pygame
import Global
import random
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

class Grid:
	def __init__(self, width: int, seed):
		self.width: int = width
		self.seed = seed
		self.origin: Tuple[int, int] = (Global.WIDTH // 2, 220)
		self.tileheight = (Global.HEIGHT - 180) / width / 3
		self.tilewidth = self.tileheight * 1.5
		self.tiles = self.generate_tiles()
		

	def generate_tiles(self):
		tiles = [
			[Tile(x, y, self.width, self) for x in range(self.width)] for y in range(self.width)
		]

		return tiles

	def render(self, win, mousepos):
		#pygame.draw.rect(win, (0, 0, 0), (*self.origin, 10, 10))

		for row in self.tiles:
			for tile in row:
				tile.render(win, Polygon(tile.top_points).contains(Point(*mousepos)))



