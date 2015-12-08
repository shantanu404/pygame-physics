import pygame
import math

class Particle(object):
	"""docstring for Particle"""
	def __init__(self, screen, pos, size):
		(self.x, self.y) = pos
		self.size = size
		self.color = (10, 10, 10)
		self.thickness = 1
		self.screen = screen
		self.speed = 0.01
		self.angle = math.pi/2
	def display(self):
		pygame.draw.circle(self.screen, self.color, (int(self.x), int(self.y)), self.size, self.thickness)
	def move(self):
			self.x += (math.sin(self.angle) * self.speed)
			self.y += (math.cos(self.angle) * self.speed)
