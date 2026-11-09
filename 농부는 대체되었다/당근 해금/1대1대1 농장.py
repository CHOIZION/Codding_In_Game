for i in range(get_world_size()):
	for j in range(get_world_size()):
		if i == 2:
			till()
		move(North)
	move(East)

while True:
	for i in range(get_world_size()):
		for j in range(get_world_size()):

			if can_harvest():
				harvest()

			# 건초
			if i == 0:
				pass

			# 덤불
			if i == 1:
				plant(Entities.Bush)

			# 당근
			if i == 2:
				plant(Entities.Carrot)

			move(North)
		move(East)