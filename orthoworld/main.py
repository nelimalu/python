import pygame
from Grid import Grid
import Global
import random
import time

win = pygame.display.set_mode((Global.WIDTH, Global.HEIGHT))
pygame.display.set_caption("kjasdfn")


def update(grid):
	win.fill((240,240,240))

	grid.render(win)

	pygame.display.flip()


def main():
	seed = random.random()

	run = True
	count = 1
	while run:
		# time.sleep(0.01)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		grid = Grid(32, seed, count)
		count += 1

		update(grid)


if __name__ == "__main__":
	main()

pygame.quit()
