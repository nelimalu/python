import pygame
import pygame.gfxdraw


def polygon(win, colour: tuple[int, int, int], points: tuple):
	pygame.gfxdraw.aapolygon(win, points, colour)
	pygame.gfxdraw.filled_polygon(win, points, colour)

def colour_depth(colour, noise_value):
	r = colour[0] + (noise_value * 50)
	g = colour[1] + (noise_value * 50)
	b = colour[2] + (noise_value * 50)
	return r, g, b
