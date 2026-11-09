clear()

for i in range(get_world_size()):
	for j in range(get_world_size()):
		if i >= 3 and j >= 3:
			till()
		elif i >= 4:
			till()

		move(North)
	move(East)

while True:
	for i in range(get_world_size()):
		for j in range(get_world_size()):

			if i >= 3 and j >= 3:
				if can_harvest():
					harvest()
				plant(Entities.Pumpkin)

			elif i >= 4:
				if can_harvest():
					harvest()
				plant(Entities.Carrot)

			elif (i + j) % 2 == 0:
				if can_harvest():
					harvest()
				plant(Entities.Tree)

			else:
				if can_harvest():
					harvest()

			if get_water() < 0.5:
				use_item(Items.Water)

			if not can_harvest():
				use_item(Items.Fertilizer)

			move(North)
		move(East)