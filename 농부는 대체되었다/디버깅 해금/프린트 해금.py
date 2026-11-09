while True:
	# 농장 가로 세로 크기 자동 인식
	for i in range(get_world_size()):
		for j in range(get_world_size()):

			if can_harvest():
				harvest()
				print("수확 완료")  # 디버깅용 출력

			plant(Entities.Bush)
			move(North)
		move(East)