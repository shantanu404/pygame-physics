import pygame

class Particle(object):
	"""docstring for Particle"""
	def __init__(self, screen, pos, size):
		(self.x, self.y) = pos
		self.size = size
		self.color = (10, 10, 10)
		self.thickness = 2
		self.screen = screen
	def display(self):
		pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.size, self.thickness)
		