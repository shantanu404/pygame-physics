import math
import random
import pygame
import particle


background_color = (255, 255, 255)
(width, height) = (600, 400)

def main():
	screen = pygame.display.set_mode((width, height))
	pygame.display.set_caption("Tutorial 5")

	num_particles = 10;
	my_particles = []

	for n in range(num_particles):
		size = random.randint(10, 20)
		x = random.randint(size, width-size)
		y = random.randint(size, height-size)

		my_particle = particle.Particle(screen, (x, y), size)
		my_particle.speed = random.random()
		my_particle.angle = random.uniform(0, math.pi*4)
		
		my_particles.append(my_particle)

	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		screen.fill(background_color)

		for my_particle in my_particles:
			my_particle.move()
			my_particle.display()
		pygame.display.flip()

	return


if __name__ == '__main__':
	main()