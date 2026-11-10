SIZE = get_world_size()

def normal_miner():
	while True:
		for y in range(SIZE):
			dig()
			move(North)


def explosive_miner():
	change_hat(Hats.Explosive_Drill)

	while True:
		for y in range(SIZE):
			for x in range(SIZE):
				dig()
				move(East)
			move(North)


# 폭발 드릴 드론 1대
spawn_drone(explosive_miner)

# 일반 채굴 드론 30대
move(East)

for x in range(30):
	spawn_drone(normal_miner)
	move(East)

# 메인 드론까지 총 32대
normal_miner()