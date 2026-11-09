for i in range(get_world_size()):
    for j in range(get_world_size()):
        if i >= 4:
            till()
        move(North)
    move(East)

while True:
    for i in range(get_world_size()):
        for j in range(get_world_size()):
            if can_harvest():
                harvest()

                if i < 2:
                    pass

                if i >= 2 and i < 4:
                    plant(Entities.Bush)

                if i >= 4:
                    plant(Entities.Carrot)

            if i >= 2 and i < 4:
                plant(Entities.Bush)

            if i >= 4:
                plant(Entities.Carrot)

            move(North)
        move(East)