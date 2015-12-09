import pygame
import math

import utils
import force

class Particle(object):
	"""docstring for Particle"""
	def __init__(self, screen, pos, size):
		self.x = pos[0]
		self.y = pos[1]
		self.size = size
		self.color = (10, 10, 10)
		self.thickness = 1
		self.screen = screen
		self.speed = 0.01
		self.angle = 0
		return
	
	def display(self):
		pygame.draw.circle(self.screen, self.color, (int(self.x), int(self.y)), self.size, self.thickness)
		return
	
	def move(self):
		(self.angle, self.speed) = utils.add_vectors((self.angle, self.speed), force.GRAVITY)
		self.speed *= (1 - force.DRAG)
		self.x += (math.sin(self.angle) * self.speed)
		self.y += (math.cos(self.angle) * self.speed)
		self.bounce()
		return

	def bounce(self):
		if self.x > self.screen.get_size()[0] - self.size:
			self.x = 2*(self.screen.get_size()[0]-self.size) - self.x
			self.angle = -self.angle
			self.speed *= force.ELASTICITY
		elif self.x < self.size:
			self.x = 2*self.size - self.x
			self.angle = -self.angle
			self.speed *= force.ELASTICITY

		if self.y > self.screen.get_size()[1] - self.size:
			self.y = 2*(self.screen.get_size()[1] - self.size) - self.y
			self.angle = math.pi - self.angle
			self.speed *= force.ELASTICITY

		elif self.y < self.size:
			self.y = 2*self.size - self.y
			self.angle = math.pi - self.angle
			self.speed *= force.ELASTICITY

		return