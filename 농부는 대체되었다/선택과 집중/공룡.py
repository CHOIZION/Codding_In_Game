clear()

SIZE = get_world_size()

# 32x32 전용
# 시작 위치 (0, 0)

def next_step():
    x = get_pos_x()
    y = get_pos_y()

    if x == 0:
        if y < SIZE - 1:
            return North
        return East

    if x % 2 == 1:
        if y > 1:
            return South
        if x < SIZE - 1:
            return East
        return South

    if y < SIZE - 1:
        return North

    if x < SIZE - 1:
        return East

    return South


def farm_bones():
    clear()
    change_hat(Hats.Dinosaur_Hat)

    steps = 0
    limit = SIZE * SIZE * SIZE

    while steps < limit:
        direction = next_step()

        if not move(direction):
            break

        steps += 1

    change_hat(Hats.Straw_Hat)


while True:
    if num_items(Items.Cactus) == 0:
        break

    farm_bones()