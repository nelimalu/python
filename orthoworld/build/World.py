from block import Block
from Global import *

class World:
	def __init__(self, blocks):
		self.blocks = self.sortblocks(blocks)

	@staticmethod
	def sortblocks(blocks):
		new_blocks = [
			[
				[
					None for z in range(WORLDSIZE)  # z planes
				] for y in range(WORLDSIZE)  # y planes
			] for x in range(WORLDSIZE)  # x planes
		]

		for block in blocks:
			new_blocks[block.x][block.y][block.z] = block

		return new_blocks

	def draw(self, win):
		for x_plane in self.blocks:
			for y_plane in x_plane:
				for block in y_plane:
					if block is not None:
						block.draw(win)

