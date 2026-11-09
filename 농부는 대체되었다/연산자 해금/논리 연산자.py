while True:
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if not can_harvest():
				print("아직 수확 불가")
			else:
				harvest()

			plant(Entities.Bush)
			move(North)
		move(East)