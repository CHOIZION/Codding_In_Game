clear()

SIZE = get_world_size()
HALF = SIZE // 2

# ---------- 공통 기능 ----------

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

def water():
    if get_water() < 0.5:
        if num_items(Items.Water) > 0:
            use_item(Items.Water)

def soil():
    if get_ground_type() != Grounds.Soil:
        till()

def grassland():
    if get_ground_type() != Grounds.Grassland:
        till()

def prepare(x0, y0, width, height):
    for x in range(x0, x0 + width):
        for y in range(y0, y0 + height):
            go_to(x, y)
            soil()

# ---------- 드론 1: 나무 / 건초 / 혼합 재배 ----------

def forest():
    requests = {}

    while True:
        next_requests = {}

        for x in range(HALF):
            for y in range(HALF):
                go_to(x, y)

                pos = (x, y)

                if pos in requests:
                    crop = requests[pos]
                elif (x + y) % 2 == 0:
                    crop = Entities.Tree
                else:
                    crop = Entities.Grass

                if crop == Entities.Carrot:
                    soil()
                else:
                    grassland()

                if can_harvest():
                    harvest()

                    if num_items(Items.Fertilizer) > 0:
                        if (x + y) % 3 == 0:
                            use_item(Items.Fertilizer)

                if crop != Entities.Grass:
                    if get_entity_type() != crop:
                        plant(crop)

                companion = get_companion()

                if companion != None:
                    wanted, target = companion
                    tx, ty = target

                    if tx < HALF and ty < HALF:
                        next_requests[target] = wanted

                water()

        requests = next_requests

# ---------- 드론 2: 당근 / 호박 ----------

def vegetables():
    # 아래 8x4: 당근
    prepare(HALF, 0, HALF, 4)

    # 위 8x4 중 6x6 호박을 만들 수 없으므로
    # 오른쪽 아래 8x8 안에서 별도 재배하는 대신
    # 당근 8x2 + 호박 8x6 구성으로 운영

    prepare(HALF, 4, HALF, 4)

    while True:
        # 당근 8x4
        for x in range(HALF, SIZE):
            for y in range(4):
                go_to(x, y)

                if can_harvest():
                    harvest()

                if get_entity_type() != Entities.Carrot:
                    plant(Entities.Carrot)

                water()

        # 호박 8x4
        for x in range(HALF, SIZE):
            for y in range(4, HALF):
                go_to(x, y)

                if get_entity_type() != Entities.Pumpkin:
                    plant(Entities.Pumpkin)

                water()

        # 호박 영역 수확
        go_to(HALF, 4)

        if can_harvest():
            harvest()

# ---------- 드론 3: 선인장 ----------

def cactus_rows():
    for y in range(HALF, SIZE):
        for end in range(HALF - 1, 0, -1):
            for x in range(end):
                go_to(x, y)

                a = measure()
                b = measure(East)

                if a != None and b != None:
                    if a > b:
                        swap(East)

def cactus_columns():
    for x in range(HALF):
        for end in range(SIZE - 1, HALF, -1):
            for y in range(HALF, end):
                go_to(x, y)

                a = measure()
                b = measure(North)

                if a != None and b != None:
                    if a > b:
                        swap(North)

def cactus():
    prepare(0, HALF, HALF, HALF)

    while True:
        ready = True

        for x in range(HALF):
            for y in range(HALF, SIZE):
                go_to(x, y)

                if get_entity_type() != Entities.Cactus:
                    plant(Entities.Cactus)
                    ready = False

                elif not can_harvest():
                    ready = False

                water()

        if ready:
            cactus_rows()
            cactus_columns()

            go_to(0, HALF)

            if can_harvest():
                harvest()

# ---------- 메인 드론: 미로 ----------

DIRECTIONS = [North, East, South, West]
OPPOSITE = [South, West, North, East]

def find_treasure():
    visited = set()
    visited.add((get_pos_x(), get_pos_y()))

    stack = [[0, -1]]

    while get_entity_type() != Entities.Treasure:
        if len(stack) == 0:
            return False

        if stack[-1][0] == 4:
            back = stack[-1][1]
            stack.pop()

            if back != -1:
                move(OPPOSITE[back])

        else:
            d = stack[-1][0]
            stack[-1][0] += 1

            direction = DIRECTIONS[d]

            if can_move(direction):
                x = get_pos_x()
                y = get_pos_y()

                if d == 0:
                    y = (y + 1) % SIZE
                elif d == 1:
                    x = (x + 1) % SIZE
                elif d == 2:
                    y = (y - 1) % SIZE
                else:
                    x = (x - 1) % SIZE

                if (x, y) not in visited:
                    move(direction)
                    visited.add((x, y))
                    stack.append([0, d])

    return True

def maze():
    amount = HALF * 2 ** (num_unlocked(Unlocks.Mazes) - 1)

    while True:
        go_to(12, 12)

        if num_items(Items.Weird_Substance) < amount:
            continue

        plant(Entities.Bush)

        if not use_item(Items.Weird_Substance, amount):
            continue

        relocations = 0

        while relocations < 300:
            if not find_treasure():
                break

            if num_items(Items.Weird_Substance) < amount:
                break

            if not use_item(Items.Weird_Substance, amount):
                break

            relocations += 1

        if find_treasure():
            harvest()

# ---------- 실행 ----------

spawn_drone(forest)
spawn_drone(vegetables)
spawn_drone(cactus)

maze()