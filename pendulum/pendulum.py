import pygame
import math

win = pygame.display.set_mode((640,480))
pygame.display.set_caption("aojsdfasd")
clock = pygame.time.Clock()

GRAVITY = 0.1


class Vector:
	def __init__(self, angle: float, magnitude: float):
		self.angle = angle
		self.magnitude = magnitude

	def get_angle(self) -> float:
		return self.angle

	def get_magnitude(self) -> float:
		return self.magnitude

	def get_x(self) -> float:
		return math.cos(self.angle) * self.magnitude

	def get_y(self) -> float:
		return math.sin(self.angle) * self.magnitude

	def add(self, other):
		x_dist = self.get_x() + other.get_x()
		y_dist = self.get_y() + other.get_y()




class Pendulum:
	def __init__(self, center: tuple[int, int], start_angle: int, mass: int, length: int):
		self.center_x: int = center[0]
		self.center_y: int = center[1]
		self.center: tuple[int, int] = center
		self.prev_force: Vector = Vector(0, 0)
		self.mass: int = mass
		self.length: int = length
		self.gravity: Vector = self.calc_gravity()
		self.force: Vector = Vector(math.radians(start_angle - 90), 0)

	def calc_gforce(self):
		return Vector(270, self.mass * GRAVITY)

	def calc_applied_force(self):
		return Vector(-self.force.get_angle(), self.gravity * math.sin(self.force.get_angle()))

	def tick(self):
		self.prev_force = self.force
		self.force = self.calc_applied_force()

		new_x = math.cos(self.force.get_angle()) * self.force.get_magnitude()
		new_y = math.sin(self.force.get_angle()) * self.force.get_magnitude()


	def draw(self):
		pass



def update():
	win.fill((240,240,240))

	pygame.display.flip()


def main():
	run = True
	while run:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False


		update()


if __name__ == "__main__":
	main()

pygame.quit()
