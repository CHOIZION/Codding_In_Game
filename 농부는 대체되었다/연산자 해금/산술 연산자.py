while True:
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if can_harvest():
				harvest()
				print(1 + 2)  # 산술 연산자 테스트

			plant(Entities.Bush)
			move(North)
		move(East)