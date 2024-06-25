from block import Block
from Global import *
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

class World:
	def __init__(self, blocks):
		self.blocks = self.sortblocks(blocks)
		self.selected_block = None

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
		closest_block = None

		for x_plane in self.blocks:
			for y_plane in x_plane:
				for block in y_plane:
					if block is not None:
						if block == self.selected_block:
							block.colour = Colour(148, 148, 148)
						block.draw(win)
						block.colour = Colour(128, 128, 128)

		if closest_block is not None:
			closest_block

	def delete(self, block):
		self.blocks[block.x][block.y][block.z] = None

	def get(self, x, y, z):
		return self.blocks[x][y][z]

	def place(self, x, y, z):
		if y + 1 < WORLDSIZE and self.selected_block.active_side == "TOP":
			self.blocks[x][y + 1][z] = Block(x, y + 1, z)
		elif x + 1 < WORLDSIZE and self.selected_block.active_side == "LEFT":
			self.blocks[x + 1][y][z] = Block(x + 1, y, z)
		elif z + 1 < WORLDSIZE and self.selected_block.active_side == "RIGHT":
			self.blocks[x][y][z + 1] = Block(x, y, z + 1)


	def get_active_side(self, block, mousepoint):
		top = Polygon([
			block.points.origin.get(),
			block.points.surface_left.get(),
			block.points.surface_front.get(),
			block.points.surface_right.get(),
		])
		left = Polygon([
			block.points.surface_left.get(),
			block.points.side_left.get(),
			block.points.side_center.get(),
			block.points.surface_front.get()
		])
		# don't need right because it's the else case

		if top.contains(mousepoint):
			return "TOP"
		elif left.contains(mousepoint):
			return "LEFT"
		return "RIGHT"


	def raycast(self, mousepos):
		mousepoint = Point(*mousepos)

		collisions = []
		for x_plane in self.blocks:
			for y_plane in x_plane:
				for block in y_plane:
					if block is not None:
						polygon = Polygon([
							block.points.origin.get(),
							block.points.surface_left.get(),
							block.points.side_left.get(), 
							block.points.side_center.get(),
							block.points.side_right.get(),
							block.points.surface_right.get()
						])
						if polygon.contains(mousepoint):
							collisions.append(block)

		if len(collisions) == 0:
			self.selected_block = None
		else:
			self.selected_block = collisions[-1]
			self.selected_block.active_side = self.get_active_side(self.selected_block, mousepoint)
