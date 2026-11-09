clear()

SIZE = get_world_size()
HALF = SIZE // 2

def go_to(x, y):
    while get_pos_x() != x:
        move(East)
    while get_pos_y() != y:
        move(North)

def hay_farm(x0, y0):
    while True:
        for x in range(x0, x0 + HALF):
            for y in range(y0, y0 + HALF):
                go_to(x, y)

                if get_ground_type() != Grounds.Grassland:
                    till()

                if can_harvest():
                    harvest()

def worker1():
    hay_farm(0, 0)

def worker2():
    hay_farm(HALF, 0)

def worker3():
    hay_farm(0, HALF)

spawn_drone(worker1)
spawn_drone(worker2)
spawn_drone(worker3)

hay_farm(HALF, HALF)