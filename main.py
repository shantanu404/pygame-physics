import random
import pygame
import particle


background_color = (255, 255, 255)
(width, height) = (300, 200)

def main():
	screen = pygame.display.set_mode((width, height))
	pygame.display.set_caption("Tutorial 3")
	screen.fill(background_color)

	num_particles = 10;
	my_particles = []

	for n in range(num_particles):
		size = random.randint(10, 20)
		x = random.randint(size, width-size)
		y = random.randint(size, height-size)
		my_particles.append(particle.Particle(screen, (x, y), size))
	for my_particle in my_particles:
		my_particle.display()

	pygame.display.flip()

	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

if __name__ == '__main__':
	main()