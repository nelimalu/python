import pygame.gfxdraw

# width and height of the window
WIDTH = 640
HEIGHT = 480

# pixel coordinate of (0, 0, 0)
ORIGIN_X = WIDTH // 2
ORIGIN_Y = HEIGHT // 3

WORLDSIZE = 3

def draw_polygon(surf, coords, colour):
	pygame.gfxdraw.filled_polygon(surf, coords, colour)
	pygame.gfxdraw.aapolygon(surf, coords, (100, 100, 100))

