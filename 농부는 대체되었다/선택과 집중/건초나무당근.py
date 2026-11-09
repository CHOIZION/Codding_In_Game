clear()

SIZE = get_world_size()
HALF = SIZE // 2

def go_to(x, y):
    while get_pos_x() != x:
        move(East)
    while get_pos_y() != y:
        move(North)

def water():
    if get_water() < 0.5:
        if num_items(Items.Water) > 0:
            use_item(Items.Water)

def base_crop(x, y):
    # 나무 25%, 당근 25%, 건초 50%
    if (x + y) % 4 == 0:
        return Entities.Tree
    if (x + y) % 4 == 2:
        return Entities.Carrot
    return Entities.Grass

def set_crop(crop):
    if crop == Entities.Carrot:
        if get_ground_type() != Grounds.Soil:
            till()
    else:
        if get_ground_type() != Grounds.Grassland:
            till()

    if crop == Entities.Grass:
        if get_entity_type() != Entities.Grass:
            plant(Entities.Grass)
    elif get_entity_type() != crop:
        plant(crop)

def farm(x0, y0):
    requests = {}

    while True:
        next_requests = {}

        # 1단계: 작물 관리 및 동반 작물 요청 수집
        for x in range(x0, x0 + HALF):
            for y in range(y0, y0 + HALF):
                go_to(x, y)

                pos = (x, y)

                if pos in requests:
                    crop = requests[pos]
                else:
                    crop = base_crop(x, y)

                if can_harvest():
                    harvest()

                set_crop(crop)

                companion = get_companion()

                if companion != None:
                    wanted, target = companion
                    tx, ty = target

                    if tx >= x0 and tx < x0 + HALF:
                        if ty >= y0 and ty < y0 + HALF:
                            if target not in next_requests:
                                next_requests[target] = wanted

                water()

        # 2단계: 동반 작물 배치
        for pos in next_requests:
            x, y = pos
            go_to(x, y)

            wanted = next_requests[pos]

            if get_entity_type() != wanted:
                if can_harvest():
                    harvest()
                set_crop(wanted)

        # 3단계: 동반 작물이 배치된 상태에서 수확
        for x in range(x0, x0 + HALF):
            for y in range(y0, y0 + HALF):
                go_to(x, y)

                if can_harvest():
                    harvest()

                water()

        requests = next_requests

def worker1():
    farm(0, 0)

def worker2():
    farm(HALF, 0)

def worker3():
    farm(0, HALF)

spawn_drone(worker1)
spawn_drone(worker2)
spawn_drone(worker3)

farm(HALF, HALF)