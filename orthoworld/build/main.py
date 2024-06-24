import pygame
import Global
from block import Block

win = pygame.display.set_mode((Global.WIDTH, Global.HEIGHT))
pygame.display.set_caption("orthographic build")
clock = pygame.time.Clock()


def update(blocks):
	win.fill((240,240,240))

	for block in blocks:
		block.draw(win)

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
		#Block(1, 1, 1),

		Block(1, 2, 0),
		Block(0, 2, 1),
		Block(1, 2, 1),
		Block(2, 2, 1),
		Block(1, 2, 2),
	]

	# blocks = [
	# 	Block(1, 0, 1),
	# 	Block(1, 1, 1)
	# ]

	run = True
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		update(blocks)


main()
pygame.quit()


