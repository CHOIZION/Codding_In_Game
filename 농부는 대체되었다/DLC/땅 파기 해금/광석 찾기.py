SIZE = get_world_size()

def mine_column():
	while True:
		for y in range(SIZE):

			# 석탄이면 먼저 채굴
			if get_ground_type() == Grounds.Coal:
				dig()
				return True

			# 땅을 파서 아래층 확인
			dig()

			# 파낸 직후 석탄이 드러났으면 즉시 채굴
			if get_ground_type() == Grounds.Coal:
				dig()
				return True

			move(North)

		# 석탄이 없으면 같은 열을 다시 돌며 추가 채굴

drones = []

for x in range(SIZE - 1):
	d = spawn_drone(mine_column)
	drones.append(d)
	move(East)

mine_column()

for d in drones:
	wait_for(d)