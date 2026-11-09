while True:
	for i in range(get_world_size()):
		for j in range(get_world_size()):

			if can_harvest():
				harvest()

			if i < 4:
				if (i + j) % 2 == 0:
					plant(Entities.Tree)

			if i >= 4:
				plant(Entities.Carrot)

			move(North)
		move(East)

		print(get_ground_type())