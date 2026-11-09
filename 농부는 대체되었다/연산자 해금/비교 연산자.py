while True:
    for i in range(get_world_size()):
        for j in range(get_world_size()):
            if i == 0:
                print("첫 번째 열")

            if can_harvest():
                harvest()

            plant(Entities.Bush)
            move(North)
        move(East)