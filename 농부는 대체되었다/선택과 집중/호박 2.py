clear()

SIZE = get_world_size()

def go_to(x, y):
    while get_pos_x() != x:
        move(East)
    while get_pos_y() != y:
        move(North)

def repair_column(x):
    for y in range(SIZE):
        go_to(x, y)

        if get_ground_type() != Grounds.Soil:
            till()

        if get_entity_type() != Entities.Pumpkin:
            plant(Entities.Pumpkin)

        if get_water() < 0.5:
            if num_items(Items.Water) > 0:
                use_item(Items.Water)

def worker(x0, x1):
    while True:
        for x in range(x0, x1):
            repair_column(x)

def make_worker(x0, x1):
    def run():
        worker(x0, x1)
    return run

# 15개 작업 드론
for i in range(15):
    x0 = i * SIZE // 15
    x1 = (i + 1) * SIZE // 15

    spawn_drone(make_worker(x0, x1))

# 메인 드론: 전체 호박 합체 확인 및 수확
while True:
    go_to(0, 0)

    if get_entity_type() == Entities.Pumpkin:
        if can_harvest():
            first = measure()

            go_to(SIZE - 1, SIZE - 1)

            if get_entity_type() == Entities.Pumpkin:
                if can_harvest():
                    if measure() == first:
                        harvest()