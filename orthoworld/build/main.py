import pygame
import Global
from block import Block
from World import World

win = pygame.display.set_mode((Global.WIDTH, Global.HEIGHT))
pygame.display.set_caption("orthographic build")
clock = pygame.time.Clock()


def update(world):
	win.fill((240,240,240))

	world.draw(win)

	pygame.display.flip()


def main():
	blocks = [  # nether reactor core
		Block(0, 0, 0),
		Block(1, 0, 0),
		Block(2, 0, 0),
		Block(0, 0, 1),
		Block(1, 0, 1),
		Block(2, 0, 1),
		Block(0, 0, 2),
		Block(1, 0, 2),
		Block(2, 0, 2),

		Block(0, 1, 0),
		Block(0, 1, 2),
		Block(2, 1, 0),
		Block(2, 1, 2),
		Block(1, 1, 1),

		Block(1, 2, 0),
		Block(0, 2, 1),
		Block(1, 2, 1),
		Block(2, 2, 1),
		Block(1, 2, 2),

	]

	world = World(blocks)

	run = True
	while run:
		mousepos = pygame.mouse.get_pos()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			if world.selected_block is not None:
				if event.type == pygame.MOUSEBUTTONDOWN:
					if event.button == 1:  # left mouse button
						world.delete(world.selected_block)
					if event.button == 3:  # right mouse button
						world.place(*world.selected_block.get_coords())

		world.raycast(mousepos)

		update(world)


main()
pygame.quit()


