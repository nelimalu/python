import pygame
import pygame.gfxdraw
import math

WIDTH = 640
HEIGHT = 480
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("pendulum")
clock = pygame.time.Clock()

GRAVITY = 0.5
ORIGIN_X = WIDTH // 2
ORIGIN_Y = 0


class Energy:
	def __init__(self, mass, height):
		self.mass = mass
		self.height = height
		self.total = mass * GRAVITY * height
		self.potential = self.total
		self.kinetic = 0

	def update(self, height):
		self.potential = self.mass * GRAVITY * (self.height if height > self.height else height)
		self.kinetic = self.total - self.potential

	def get_velocity(self):
		return math.sqrt((self.kinetic * 2) / self.mass)


class Pendulum:
	DIRECTION_OFFSET =  -math.radians(90)

	def __init__(self, length, start_angle, mass):
		self.length = length
		self.mass = mass
		self.angle = start_angle
		self.x = ORIGIN_X + math.cos(self.angle) * length
		self.y = ORIGIN_Y + math.sin(self.angle) * length
		self.energy = Energy(mass, ORIGIN_Y + self.length - self.y)

	def update(self):
		applied_magnitude = self.mass * GRAVITY * math.sin(self.angle)
		self.move(applied_magnitude, self.angle + self.DIRECTION_OFFSET)
		height = ORIGIN_Y + self.length - self.y
		if height > self.energy.height:
			self.DIRECTION_OFFSET *= -1
			self.energy = Energy(self.mass, ORIGIN_Y + self.length - self.y)

		self.energy.update(height)
		self.move(self.energy.get_velocity(), self.angle + self.DIRECTION_OFFSET)

		self.x = ORIGIN_X + math.cos(self.angle) * self.length
		self.y = ORIGIN_Y + math.sin(self.angle) * self.length


	def move(self, magnitude, angle):
		self.x += math.cos(angle) * magnitude
		self.y += math.sin(angle) * magnitude
		self.recalc_angle()

	def recalc_angle(self):
		self.angle = math.atan2(self.y - ORIGIN_Y, self.x - ORIGIN_X)

	def draw(self):
		pygame.draw.aaline(win, (32,32,32), (ORIGIN_X, ORIGIN_Y), (self.x, self.y), 3)
		pygame.gfxdraw.filled_circle(win, int(self.x), int(self.y), 10, (70, 76, 77))
		pygame.gfxdraw.aacircle(win, int(self.x), int(self.y), 10, (70, 76, 77))


def distance(x1, y1, x2, y2):
	return math.sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2)


def update(pendulums):
	win.fill((240,240,240))

	for pendulum in pendulums:
		pendulum.draw()

	pygame.display.flip()


def main():
	pendulums = [
		#Pendulum(300, -40, 0.1)
	]

	run = True
	while run:
		clock.tick(60)
		mousepos = pygame.mouse.get_pos()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				print(f"[INFO] Created pendulum at ({mousepos[0]}, {mousepos[1]})")
				pendulums.append(Pendulum(
					distance(ORIGIN_X, ORIGIN_Y, *mousepos),
					math.atan2(mousepos[1] - ORIGIN_Y, mousepos[0] - ORIGIN_X),
					0.1
				))
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_BACKSPACE:
					print(f"[INFO] Cleared board!")
					pendulums = []



		for pendulum in pendulums:
			pendulum.update()

		update(pendulums)


if __name__ == "__main__":
	main()

pygame.quit()

