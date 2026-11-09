directions = [North, East, South, West]
opposite = [South, West, North, East]

amount = get_world_size() * 2 ** (num_unlocked(Unlocks.Mazes) - 1)

def find_treasure():
    visited = set()
    visited.add((get_pos_x(), get_pos_y()))
    stack = [[0, -1]]

    while get_entity_type() != Entities.Treasure:
        if stack[-1][0] == 4:
            back = stack[-1][1]
            stack.pop()
            if back != -1:
                move(opposite[back])
        else:
            d = stack[-1][0]
            stack[-1][0] += 1

            if can_move(directions[d]):
                x = get_pos_x()
                y = get_pos_y()

                if d == 0:
                    y = (y + 1) % get_world_size()
                elif d == 1:
                    x = (x + 1) % get_world_size()
                elif d == 2:
                    y = (y - 1) % get_world_size()
                else:
                    x = (x - 1) % get_world_size()

                if (x, y) not in visited:
                    move(directions[d])
                    visited.add((x, y))
                    stack.append([0, d])

while True:
    clear()
    plant(Entities.Bush)

    if not use_item(Items.Weird_Substance, amount):
        break

    for n in range(300):
        find_treasure()

        if not use_item(Items.Weird_Substance, amount):
            break

    find_treasure()
    harvest()