import pygame
import particle

background_color = (255, 255, 255)
(width, height) = (300, 200)

def main():
	screen = pygame.display.set_mode((width, height))
	pygame.display.set_caption("Tutorial 2")
	screen.fill(background_color)

	myparticle = particle.Particle(screen, (150, 100), 15)
	myparticle.display()

	pygame.display.flip()

	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

if __name__ == '__main__':
	main()