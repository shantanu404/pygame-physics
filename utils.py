import math

import force

def add_vectors(vector1, vector2):
	#Note the vectors are tuple (angle, magnitude)
	x = math.sin(vector1[0]) * vector1[1] + math.sin(vector2[0]) * vector2[1]
	y = math.cos(vector1[0]) * vector1[1] + math.cos(vector2[0]) * vector2[1]
	mag = math.hypot(x, y)
	angle = (math.pi/2) - math.atan2(y, x)
	return (angle, mag)

def find_particle(particles, x, y):
	for p in particles:
		if math.hypot(p.x - x, p.y - y) <= p.size:
			return p
	return

def collide(p1, p2):
	dx = p1.x - p2.x
	dy = p1.y - p2.y

	dist = math.hypot(dx, dy)
	if dist < p1.size + p2.size:
		# print("Bang!")
		tangent = math.atan2(dy, dx)
		angle = 0.5 * math.pi + tangent

		angle1 = 2*tangent - p1.angle
		angle2 = 2*tangent - p2.angle
		speed1 = p2.speed*force.ELASTICITY
		speed2 = p1.speed*force.ELASTICITY

		(p1.angle, p1.speed) = (angle1, speed1)
		(p2.angle, p2.speed) = (angle2, speed2)

		angle = 0.5 * math.pi + tangent
		p1.x += math.sin(angle)
		p1.y -= math.cos(angle)
		p2.x -= math.sin(angle)
		p2.y += math.cos(angle)
