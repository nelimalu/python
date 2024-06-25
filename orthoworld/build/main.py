import pygame
from Global import *
from block import Block
from World import World
from Hotbar import Hotbar

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("orthographic build")
clock = pygame.time.Clock()


def update(world, hotbar):
	win.fill((240,240,240))

	world.draw(win)
	hotbar.draw(win)

	pygame.display.flip()


def main():
	# blocks = [  # nether reactor core
	# 	Block(0, 0, 0),
	# 	Block(1, 0, 0),
	# 	Block(2, 0, 0),
	# 	Block(0, 0, 1),
	# 	Block(1, 0, 1),
	# 	Block(2, 0, 1),
	# 	Block(0, 0, 2),
	# 	Block(1, 0, 2),
	# 	Block(2, 0, 2),

	# 	Block(0, 1, 0),
	# 	Block(0, 1, 2),
	# 	Block(2, 1, 0),
	# 	Block(2, 1, 2),
	# 	Block(1, 1, 1),

	# 	Block(1, 2, 0),
	# 	Block(0, 2, 1),
	# 	Block(1, 2, 1),
	# 	Block(2, 2, 1),
	# 	Block(1, 2, 2),
	# ]

	#blocks = [Block(x % WORLDSIZE, 0, x // WORLDSIZE) for x in range(WORLDSIZE ** 2)]
	blocks = [Block(0,0,0)]

	world = World(blocks)
	hotbar = Hotbar()

	run = True
	while run:
		mousepos = pygame.mouse.get_pos()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:  # left mouse button
					if world.selected_block is not None:
						world.delete(world.selected_block)

					colour = hotbar.get_colour(mousepos)
					if colour is not None:
						hotbar.selected_colour = Colour(*colour)

				if event.button == 3:  # right mouse button
					if world.selected_block is not None:
						world.place(*world.selected_block.get_coords(), colour=hotbar.selected_colour)
		world.raycast(mousepos)

		update(world, hotbar)


main()
pygame.quit()


