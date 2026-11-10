clear()

SIZE = get_world_size()

def rice_worker():
    # 1. 점토층까지 수직으로 굴착
    while get_ground_type() != Grounds.Clay:
        dig()

    # 2. 한 열 전체를 담당
    while True:
        for y in range(SIZE):

            ground = get_ground_type()

            # 마른 논 제거
            if ground == Grounds.Dry_Rice_Terrace:
                dig()
                ground = get_ground_type()

            # 점토 위에 벼 심기
            if ground == Grounds.Clay:
                if get_entity_type() != Entities.Rice:
                    plant(Entities.Rice)

            # 벼가 자랐으면 수확
            if get_entity_type() == Entities.Rice:
                while not can_harvest():
                    pass

                harvest()

            move(North)

        # 한 열을 다 돌면 시작 위치로 돌아옴
        # 다음 순회에서 마른 논 제거 후 재배

        # 점토층이 끝난 경우 종료
        if get_ground_type() != Grounds.Clay and get_ground_type() != Grounds.Dry_Rice_Terrace:
            break


# 31대 드론 생성
drones = []

for x in range(SIZE - 1):
    d = spawn_drone(rice_worker)
    drones.append(d)
    move(East)

# 메인 드론도 작업
rice_worker()

for d in drones:
    wait_for(d)