while True:
	for i in range(get_world_size()):
		for j in range(get_world_size()):

			if i >= 3 and j >= 3:
				if get_ground_type() != Grounds.Soil:
					till()

				if get_entity_type() != Entities.Pumpkin:
					if can_harvest():
						harvest()
					plant(Entities.Pumpkin)

			elif i >= 4:
				if can_harvest():
					harvest()

				if get_ground_type() != Grounds.Soil:
					till()

				plant(Entities.Carrot)

			elif (i + j) % 2 == 0:
				if can_harvest():
					harvest()

				if get_ground_type() != Grounds.Grassland:
					till()

				plant(Entities.Tree)

			else:
				if get_ground_type() != Grounds.Grassland:
					till()

				if can_harvest():
					harvest()

			if get_water() < 0.5:
				use_item(Items.Water)

			move(North)
		move(East)