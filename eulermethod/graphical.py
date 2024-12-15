import pygame
import math

WIDTH = 800
HEIGHT = 800
win = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

SAMPLE_WIDTH = 25
SAMPLE_HEIGHT = SAMPLE_WIDTH


class Particle:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def draw(self):
		pygame.draw.circle(win, (0,0,0), (conv(self.x * SAMPLE_WIDTH), conv(self.y * SAMPLE_WIDTH)), 10)

	def move(self):
		h = 0.05
		self.x = self.x + h
		self.y = self.y + h * F(self.x, self.y)


def F(x, y):
	try:
		return x + y
	except:
		return 0


def conv(value):
	return WIDTH // 2 + value * (WIDTH / (SAMPLE_WIDTH ** 2))


def update(particle):
	win.fill((240,240,240))

	pygame.draw.line(win, (200,200,200), (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))
	pygame.draw.line(win, (200,200,200), (0, HEIGHT // 2), (WIDTH, HEIGHT // 2))

	for x in range(-SAMPLE_WIDTH, SAMPLE_WIDTH):
		for y in range(-SAMPLE_HEIGHT, SAMPLE_HEIGHT):
			# pygame.draw.circle(win, (0,0,0), (conv(x * SAMPLE_WIDTH), conv(y * SAMPLE_HEIGHT)), 1)
			slope = F(x, y)
			left_x = conv(x * SAMPLE_WIDTH) - 3
			right_x = conv(x * SAMPLE_WIDTH) + 3
			left_y = conv(y * SAMPLE_HEIGHT) - 3 * slope
			right_y = conv(y * SAMPLE_HEIGHT) + 3 * slope
			pygame.draw.line(win, (0,0,0), (left_x, left_y), (right_x, right_y))

	particle.draw()

	pygame.display.flip()


def main():
	particle = Particle(-1,1)

	run = True
	while run:
		clock.tick(30)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		particle.move()
		update(particle)


main()



