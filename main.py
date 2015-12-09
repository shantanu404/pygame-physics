import math
import random
import pygame

import particle
import utils

background_color = (255, 255, 255)
(width, height) = (600, 400)

def main():
	screen = pygame.display.set_mode((width, height))
	pygame.display.set_caption("Tutorial 7")

	num_particles = 3;
	my_particles = []

	for n in range(num_particles):
		size = random.randint(10, 20)
		x = random.randint(size, width-size)
		y = random.randint(size, height-size)

		my_particle = particle.Particle(screen, (x, y), size)
		my_particle.speed = random.random()
		my_particle.angle = random.uniform(0, math.pi*4)
		
		my_particles.append(my_particle)

	selected = None
	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

			if event.type == pygame.MOUSEBUTTONDOWN:
				(mouseX, mouseY) = pygame.mouse.get_pos()
				selected = utils.find_particle(my_particles, mouseX, mouseY)
			
			if event.type == pygame.MOUSEBUTTONUP:
				selected = None;

		if selected:
			(mouseX, mouseY) = pygame.mouse.get_pos()
			dx = mouseX - selected.x
			dy = mouseY - selected.y
			selected.angle = math.atan2(dy, dx) + (math.pi/2)
			selected.speed = math.hypot(dx, dy) * 0.05

		screen.fill(background_color)

		for my_particle in my_particles:
			# if selected != my_particle:
			my_particle.move()
			my_particle.display()
		pygame.display.flip()

	return


if __name__ == '__main__':
	main()