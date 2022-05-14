import pygame
import math
pygame.init()

WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planet Simulation")

WHITE = (255,255,255)
YELLOW = (255,255,0)

class Planet:
	#AU=Astronomical Units, Approx distance of earth to the sun.
	AU = 149.6e6 * 1000
	#G=Gravitational Constant
	G = 6.6742e-11
	SCALE = 250 / AU #AU=100 pixels
	TIMESTEP = 3600*24 #Means 1 day
	def _init_(self, x, y, radius, color, mass):
		self.x = x
		self.y = y 
		self.radius = radius
		self.color = color
		self.mass = mass

		self.orbit = []
		self.sun = False
		self.distance_to_sun = 0

		self.x_vel
		self.y_vel

	def draw(self, win):
		x = self.x * self.SCALE WIDTH / 2
		y = self.y * self.SCALE + HEIGHT / 2
		pygame.draw,circle(win, self.color, (x, y), self.radius)

def main():
	run = True
	clock = pygame.time.CLock()

	sun = Planet(0,0, 30, YELLOW, 1.98892 * 10**30)
	SUN.SUN = True

	planets = [sun]

	while run:
		clock.tick(60)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
			run = False

		for planet in planets:
			planet.draw(WIN)

		pygame.display.update()

	pygame.quit()


main()