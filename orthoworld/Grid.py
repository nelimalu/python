from Tile import Tile
import pygame
import Global
from perlin_noise import PerlinNoise
import random

class Grid:
	def __init__(self, width: int, seed, dist):
		self.width: int = width
		self.seed = seed
		self.dist = dist
		self.origin: Tuple[int, int] = (Global.WIDTH // 2, 40)
		self.tileheight = (Global.HEIGHT - 80) / width / 2
		self.tilewidth = self.tileheight * 1.5
		self.perlin = self.generate_noise()
		self.tiles = self.generate_tiles()
		

	def generate_tiles(self):
		tiles = [
			[Tile(x, y, self.width, self.perlin[x][y]) for x in range(self.width)] for y in range(self.width)
		]

		return tiles

	def render(self, win):
		#pygame.draw.rect(win, (0, 0, 0), (*self.origin, 10, 10))

		for row in self.tiles:
			for tile in row:
				tile.render(win, self.origin, self.tilewidth, self.tileheight)

	def generate_noise(self):
		noise = PerlinNoise(octaves=2, seed=self.seed)
		noisemap = [[
				noise([(i/self.width) - (self.dist / 32), j/self.width]) for j in range(self.width)] 
				for i in range(self.width)
			]

		return noisemap


