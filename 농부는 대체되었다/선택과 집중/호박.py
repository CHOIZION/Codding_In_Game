clear()

SIZE = get_world_size()
HALF = SIZE // 2

def go_to(x, y):
    while get_pos_x() != x:
        if get_pos_x() < x:
            move(East)
        else:
            move(West)

    while get_pos_y() != y:
        if get_pos_y() < y:
            move(North)
        else:
            move(South)

def pumpkin_farm(x0, y0):
    # 구역 경작
    for x in range(x0, x0 + HALF):
        for y in range(y0, y0 + HALF):
            go_to(x, y)

            if get_ground_type() != Grounds.Soil:
                till()

            plant(Entities.Pumpkin)

    while True:
        ready = True

        # 죽은 호박 교체 및 성장 확인
        for x in range(x0, x0 + HALF):
            for y in range(y0, y0 + HALF):
                go_to(x, y)

                if get_entity_type() != Entities.Pumpkin:
                    plant(Entities.Pumpkin)
                    ready = False

                elif not can_harvest():
                    ready = False

                if get_water() < 0.5:
                    if num_items(Items.Water) > 0:
                        use_item(Items.Water)

        # 8×8 구역 전체가 준비되면 수확
        if ready:
            go_to(x0, y0)

            if can_harvest():
                harvest()

            # 수확 후 다시 심기
            for x in range(x0, x0 + HALF):
                for y in range(y0, y0 + HALF):
                    go_to(x, y)
                    plant(Entities.Pumpkin)

def worker_1():
    pumpkin_farm(0, 0)

def worker_2():
    pumpkin_farm(HALF, 0)

def worker_3():
    pumpkin_farm(0, HALF)

spawn_drone(worker_1)
spawn_drone(worker_2)
spawn_drone(worker_3)

pumpkin_farm(HALF, HALF)