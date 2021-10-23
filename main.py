import renderer as gui
import particles as prt
import pygame
import sys


# Creates first pool object
pool = prt.pool(e = .96, g = 0.01)
pool.setdomain(((100, 200), (400, -200)))

# Creates second pool object
pool2 = prt.pool(e = 1, g = .001)
pool2.setdomain(((-400, 200), (-100, -200)))

# Initializes particles randomly
pool.random(6, 1, 15)
pool2.random(6, 200, 10)


pools = [pool, pool2]

i = 0
while True:
	i+= 1
	pygame.time.Clock().tick(70)

	for event in pygame.event.get():
	        if event.type == pygame.QUIT:
	            pygame.quit()
	            sys.exit()

	# After 300 frames, pool2 is merged with pool
	if i == 300:
		pool.merge(pool2)
		pool.setdomain(((-400,380), (400,-380)))
		pools.remove(pool2)

	# Updates and renders all pools
	for p in pools:
		p.update()
		print("pool temp: ", p.getmediantemp())   # Gets median 'temperature' (Velocity) of particles in pool
		gui.drawpool(p)

	gui.update() # Updates screen