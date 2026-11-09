clear()

SIZE = get_world_size()

DIRECTIONS = [North, East, South, West]
OPPOSITE = [South, West, North, East]

DX = [0, 1, 0, -1]
DY = [1, 0, -1, 0]

AMOUNT = SIZE * 2 ** (num_unlocked(Unlocks.Mazes) - 1)


# 미로 전체를 한 번 탐색해 경로 기록
def map_maze():
    root = (get_pos_x(), get_pos_y())

    parent = {}
    parent[root] = None

    stack = [[root, 0, -1]]

    while len(stack) > 0:
        current = stack[-1]
        pos = current[0]

        if current[1] == 4:
            back = current[2]
            stack.pop()

            if back != -1:
                move(OPPOSITE[back])

            continue

        d = current[1]
        current[1] += 1

        if not can_move(DIRECTIONS[d]):
            continue

        nx = (pos[0] + DX[d]) % SIZE
        ny = (pos[1] + DY[d]) % SIZE

        next_pos = (nx, ny)

        if next_pos in parent:
            continue

        if move(DIRECTIONS[d]):
            parent[next_pos] = (pos, d)
            stack.append([next_pos, 0, d])

    return parent


# 기록된 경로로 보물까지 이동
def go_treasure(parent):
    target = measure()

    if target == None:
        return False

    current = (get_pos_x(), get_pos_y())

    if current == target:
        return True

    ancestors = set()

    p = current

    while p != None:
        ancestors.add(p)

        if parent[p] == None:
            break

        p = parent[p][0]

    path = []
    p = target

    while p not in ancestors:
        if p not in parent:
            return False

        info = parent[p]

        if info == None:
            return False

        path.append(info[1])
        p = info[0]

    common = p

    p = current

    while p != common:
        info = parent[p]

        if not move(OPPOSITE[info[1]]):
            return False

        p = info[0]

    for i in range(len(path) - 1, -1, -1):
        if not move(DIRECTIONS[path[i]]):
            return False

    return get_entity_type() == Entities.Treasure


# 미로 생성
def create_maze():
    clear()

    plant(Entities.Bush)

    if not use_item(Items.Weird_Substance, AMOUNT):
        return False

    return get_entity_type() == Entities.Hedge or get_entity_type() == Entities.Treasure


# 골드 무한 파밍
while True:

    if num_items(Items.Weird_Substance) < AMOUNT:
        break

    if not create_maze():
        break

    parent = map_maze()

    success = True

    for i in range(300):

        if not go_treasure(parent):
            success = False
            break

        if num_items(Items.Weird_Substance) < AMOUNT:
            break

        if not use_item(Items.Weird_Substance, AMOUNT):
            break

    if success:
        if go_treasure(parent):
            harvest()
        else:
            break
    else:
        break