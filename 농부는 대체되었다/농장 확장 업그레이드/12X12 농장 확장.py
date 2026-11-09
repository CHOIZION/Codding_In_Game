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

def grow(crop):
    if get_entity_type() != crop:
        plant(crop)

def forest(y_start):
    soil = {}
    wishes = {}

    while True:
        wishes = {}

        for x in range(HALF):
            for y in range(y_start, y_start + HALF):
                go_to(x, y)

                if (x + y) % 2 == 0:
                    crop = Entities.Tree
                else:
                    crop = Entities.Grass

                if get_entity_type() != crop:
                    if can_harvest():
                        harvest()
                    grow(crop)

                companion = get_companion()

                if companion != None:
                    wanted, target = companion
                    tx, ty = target

                    if tx < HALF:
                        if ty >= y_start and ty < y_start + HALF:
                            if target not in wishes:
                                wishes[target] = wanted

                water()

        for x in range(HALF):
            for y in range(y_start, y_start + HALF):
                go_to(x, y)

                pos = (x, y)

                if pos in wishes:
                    crop = wishes[pos]
                elif (x + y) % 2 == 0:
                    crop = Entities.Tree
                else:
                    crop = Entities.Grass

                if crop == Entities.Carrot:
                    if pos not in soil:
                        till()
                        soil[pos] = True
                else:
                    if pos in soil:
                        till()
                        soil.pop(pos)

                if get_entity_type() != crop:
                    if can_harvest():
                        harvest()
                    grow(crop)

                water()

        for x in range(HALF):
            for y in range(y_start, y_start + HALF):
                go_to(x, y)

                if can_harvest():
                    harvest()

                water()

def forest_top():
    forest(0)

def forest_bottom():
    forest(HALF)

def carrots():
    for x in range(HALF, SIZE):
        for y in range(HALF):
            go_to(x, y)
            till()

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
    for x in range(HALF, SIZE):
        for y in range(HALF, SIZE):
            go_to(x, y)
            till()

    while True:
        ready = True

        for x in range(HALF, SIZE):
            for y in range(HALF, SIZE):
                go_to(x, y)

                entity = get_entity_type()

                if entity == Entities.Dead_Pumpkin:
                    plant(Entities.Pumpkin)
                    ready = False

                elif entity != Entities.Pumpkin:
                    plant(Entities.Pumpkin)
                    ready = False

                elif not can_harvest():
                    ready = False

                water()

        if ready:
            go_to(HALF, HALF)
            if can_harvest():
                harvest()

spawn_drone(forest_top)
spawn_drone(forest_bottom)
spawn_drone(carrots)

pumpkins()