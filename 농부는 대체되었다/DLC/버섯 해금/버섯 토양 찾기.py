SIZE = get_world_size()

def find_mushroom():
    while True:
        for y in range(SIZE):

            # 현재 위치가 버섯층인지 확인
            if get_ground_type() == Grounds.Mushroom:
                return True

            # 한 층 채굴
            dig()

            # 파낸 직후 버섯층이 드러났는지 확인
            if get_ground_type() == Grounds.Mushroom:
                return True

            move(North)

        # 한 열을 끝까지 돌았으면
        # 다음 반복에서 같은 열을 한 층 더 채굴


drones = []

# 보조 드론 31대
for x in range(SIZE - 1):
    d = spawn_drone(find_mushroom)
    drones.append(d)
    move(East)

# 메인 드론도 탐색
find_mushroom()

for d in drones:
    wait_for(d)