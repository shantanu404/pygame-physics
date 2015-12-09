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
		angle = math.atan2(dy, dx) + math.pi/2
		total_mass = p1.mass + p2.mass

		(p1.angle, p1.speed) = add_vectors((p1.angle, p1.speed*(p1.mass-p2.mass)/total_mass),
											(angle+math.pi, 2*p1.speed/total_mass))

		overlap = 0.5*(p1.size + p2.size - dist+1)
		p1.x += math.sin(angle)*overlap
		p1.y -= math.cos(angle)*overlap
		p2.x -= math.sin(angle)*overlap
		p2.y += math.cos(angle)*overlap

		p1.speed *= force.ELASTICITY
		p2.speed *= force.ELASTICITY