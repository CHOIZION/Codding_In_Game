clear()

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
    if crop == Entities.Carrot:
        if get_entity_type() != Entities.Carrot:
            plant(Entities.Carrot)
    elif crop == Entities.Tree:
        if get_entity_type() != Entities.Tree:
            plant(Entities.Tree)
    elif crop == Entities.Bush:
        if get_entity_type() != Entities.Bush:
            plant(Entities.Bush)
    elif crop == Entities.Grass:
        if get_entity_type() != Entities.Grass:
            plant(Entities.Grass)

def forest(y_start):
    soil = {}
    wishes = {}

    while True:
        wishes = {}

        for x in range(4):
            for y in range(y_start, y_start + 4):
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

                    if tx < 4:
                        if ty >= y_start and ty < y_start + 4:
                            if target not in wishes:
                                wishes[target] = wanted

                water()

        for x in range(4):
            for y in range(y_start, y_start + 4):
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

        for x in range(4):
            for y in range(y_start, y_start + 4):
                go_to(x, y)

                if can_harvest():
                    harvest()

                water()

def forest_top():
    forest(0)

def forest_bottom():
    forest(4)

def carrots():
    for x in range(4, 8):
        for y in range(4):
            go_to(x, y)
            till()

    while True:
        for x in range(4, 8):
            for y in range(4):
                go_to(x, y)

                if can_harvest():
                    harvest()

                if get_entity_type() != Entities.Carrot:
                    plant(Entities.Carrot)

                water()

def pumpkins():
    for x in range(4, 8):
        for y in range(4, 8):
            go_to(x, y)
            till()

    while True:
        ready = True
        pumpkin_id = None

        for x in range(4, 8):
            for y in range(4, 8):
                go_to(x, y)

                if get_entity_type() != Entities.Pumpkin:
                    plant(Entities.Pumpkin)
                    ready = False

                if not can_harvest():
                    ready = False
                else:
                    current_id = measure()

                    if pumpkin_id == None:
                        pumpkin_id = current_id
                    elif current_id != pumpkin_id:
                        ready = False

                water()

        if ready and pumpkin_id != None:
            go_to(4, 4)
            if can_harvest():
                harvest()

spawn_drone(forest_top)
spawn_drone(forest_bottom)
spawn_drone(carrots)

pumpkins()