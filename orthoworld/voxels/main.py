import pygame
from Grid import Grid
import Global
import random
import time

win = pygame.display.set_mode((Global.WIDTH, Global.HEIGHT))
pygame.display.set_caption("kjasdfn")


def update(grid, mousepos):
	win.fill((240,240,240))

	grid.render(win, mousepos)

	pygame.display.flip()


def main():
	seed = random.random()
	grid = Grid(6, seed)

	run = True
	while run:
		mousepos = pygame.mouse.get_pos()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		update(grid, mousepos)


if __name__ == "__main__":
	main()

pygame.quit()
