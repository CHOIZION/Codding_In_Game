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

def prepare_soil(x0, y0):
    for x in range(x0, x0 + HALF):
        for y in range(y0, y0 + HALF):
            go_to(x, y)
            if get_ground_type() != Grounds.Soil:
                till()

def forest():
    soil = {}
    requests = {}

    while True:
        new_requests = {}

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
                    if pos not in soil:
                        if get_ground_type() != Grounds.Soil:
                            till()
                        soil[pos] = True
                else:
                    if pos in soil:
                        if get_ground_type() == Grounds.Soil:
                            till()
                        soil.pop(pos)

                if can_harvest():
                    harvest()

                if get_entity_type() != crop:
                    plant(crop)

                companion = get_companion()

                if companion != None:
                    wanted, target = companion
                    tx, ty = target

                    if tx < HALF and ty < HALF:
                        if target not in new_requests:
                            new_requests[target] = wanted

                water()

        requests = new_requests

def carrots():
    prepare_soil(HALF, 0)

    while True:
        for x in range(HALF, SIZE):
            for y in range(HALF):
                go_to(x, y)

                if can_harvest():
                    harvest()

                if get_entity_type() != Entities.Carrot:
                    plant(Entities.Carrot)

                water()

def pumpkins():
    prepare_soil(HALF, HALF)

    while True:
        ready = True

        for x in range(HALF, SIZE):
            for y in range(HALF, SIZE):
                go_to(x, y)

                entity = get_entity_type()

                if entity != Entities.Pumpkin:
                    plant(Entities.Pumpkin)
                    ready = False

                elif not can_harvest():
                    ready = False

                water()

        if ready:
            go_to(HALF, HALF)
            if can_harvest():
                harvest()

def cactus_sort_rows():
    for y in range(HALF, SIZE):
        for end in range(HALF - 1, 0, -1):
            for x in range(end):
                go_to(x, y)

                a = measure()
                b = measure(East)

                if a != None and b != None:
                    if a > b:
                        swap(East)

def cactus_sort_columns():
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
    prepare_soil(0, HALF)

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
            cactus_sort_rows()
            cactus_sort_columns()

            go_to(0, HALF)

            if can_harvest():
                harvest()

spawn_drone(forest)
spawn_drone(carrots)
spawn_drone(cactus)

pumpkins()