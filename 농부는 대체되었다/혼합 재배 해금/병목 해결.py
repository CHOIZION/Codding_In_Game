clear()

soil = {}
requests = {}

for i in range(8):
	for j in range(8):
		if i >= 4:
			till()
		move(North)
	move(East)

while True:
	pumpkin_ready = True

	for i in range(8):
		for j in range(8):

			pos = (i, j)

			if i >= 4 and j >= 4:
				if get_entity_type() == Entities.Dead_Pumpkin:
					plant(Entities.Pumpkin)
					pumpkin_ready = False

				elif get_entity_type() != Entities.Pumpkin:
					plant(Entities.Pumpkin)
					pumpkin_ready = False

				elif not can_harvest():
					pumpkin_ready = False

			elif i >= 4:
				if can_harvest():
					harvest()

				if get_entity_type() == None:
					plant(Entities.Carrot)

			else:
				if pos in requests:
					crop = requests[pos]
					requests.pop(pos)
				elif (i + j) % 2 == 0:
					crop = Entities.Tree
				else:
					crop = Entities.Grass

				if crop == Entities.Carrot:
					if pos not in soil:
						till()
						soil[pos] = True
				else:
					if pos in soil:
						till()
						soil.pop(pos)

				if can_harvest():
					harvest()

				if crop == Entities.Grass:
					if get_entity_type() != Entities.Grass:
						plant(Entities.Grass)
				else:
					if get_entity_type() != crop:
						plant(crop)

				companion = get_companion()

				if companion != None:
					wanted, target = companion
					x, y = target

					if x < 4:
						if target not in requests:
							requests[target] = wanted

			if get_water() < 0.5:
				use_item(Items.Water)

			if i >= 4:
				if not can_harvest():
					use_item(Items.Fertilizer)

			move(North)
		move(East)

	if pumpkin_ready:
		for i in range(4):
			move(East)

		for j in range(4):
			move(North)

		if can_harvest():
			harvest()

		for i in range(4):
			move(West)

		for j in range(4):
			move(South)