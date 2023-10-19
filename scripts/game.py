import pyxel, data, menu

troupe = [
        [["soldier", 80, 80, 10, 5, 3, 0, 1, "terrestre", ("terrestre")]],
        [["soldier", 96, 80, 10, 5, 3, 0, 1, "terrestre", ("terrestre")]]
        ]

tour = 0
pos = [250, 250]
select_perso = None


def draw_entity(liste, index_x, index_y, type="", texture=("square", 0)):
    global pos

    for entity in liste:
        if entity[index_x] - pyxel.width // 2 <= pos[0] <= entity[index_x] + pyxel.width // 2 and entity[index_y] - pyxel.height // 2 <= pos[1] <= entity[index_y] + pyxel.height // 2:
            if texture[0] == "square":
                pyxel.rect(pyxel.width/2+(entity[index_x]-pos[0]), pyxel.height//2+(entity[index_y]-pos[1]), 16, 16, texture[1])

        if type == "unite" and select_perso is None and pyxel.width/2+(entity[index_x]-pos[0]) <= pyxel.mouse_x <= pyxel.width/2+(entity[index_x]-pos[0]) + 16 and pyxel.height/2+(entity[index_y]-pos[1]) <= pyxel.mouse_y <= pyxel.height/2+(entity[index_y]-pos[1]) + 16:
            pyxel.rect(pyxel.width - 50, pyxel.height - 50, 50, 50, 0)
            try:
                name = data.trad[data.lang][entity[0]]
            except KeyError:
                    name = entity[0]
            pyxel.text(pyxel.width - 45, pyxel.height - 45, f"{name}\n\n{entity[3]}", 7)


def update_game():
    global troupe, pos, select_perso, tour

    if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
        if select_perso is None:
            for i in range(2):
                for unite in troupe[i]:
                    if pyxel.width/2+(unite[1]-pos[0]) <= pyxel.mouse_x <= pyxel.width/2+(unite[1]-pos[0]) + 16 and pyxel.height/2+(unite[2]-pos[1]) <= pyxel.mouse_y <= pyxel.height/2+(unite[2]-pos[1]) + 16:
                        select_perso = [i, unite, []]
        elif select_perso[0] == tour:
            for case in select_perso[2]:
                if pyxel.width / 2 + (case[0] - pos[0]) <= pyxel.mouse_x <= pyxel.width / 2 + (case[0] - pos[0]) + 16 and pyxel.height / 2 + (case[1] - pos[1]) <= pyxel.mouse_y <= pyxel.height / 2 + (case[1] - pos[1]) + 16:
                    troupe[tour][troupe[tour].index(select_perso[1])][1] = case[0]
                    troupe[tour][troupe[tour].index(select_perso[1])][2] = case[1]
            select_perso = None
        else:
            select_perso = None


    elif pyxel.btn(pyxel.KEY_Z):
        pos[1] -= 2
    elif pyxel.btn(pyxel.KEY_S):
        pos[1] += 2
    elif pyxel.btn(pyxel.KEY_Q):
        pos[0] -= 2
    elif pyxel.btn(pyxel.KEY_D):
        pos[0] += 2

    if select_perso is not None:
        select_perso[2].clear()

        cote = select_perso[1][5]
        facing = 0
        case_x = 0
        case_y = 0

        for i in range(cote*4):
            for case in range(cote):
                if facing == 0:
                    case_x = select_perso[1][1] - (cote-1-case)*16
                    case_y = select_perso[1][2] - (select_perso[1][5] - cote + 1)*16
                elif facing == 1:
                    case_x = select_perso[1][1] - (select_perso[1][5] - cote + 1)*16
                    case_y = select_perso[1][2] + (cote-1-case)*16
                elif facing == 2:
                    case_x = select_perso[1][1] + (cote-1-case)*16
                    case_y = select_perso[1][2] + (select_perso[1][5] - cote + 1)*16
                elif facing == 3:
                    case_x = select_perso[1][1] + (select_perso[1][5] - cote + 1)*16
                    case_y = select_perso[1][2] - (cote-1-case)*16
                select_perso[2].append((case_x, case_y))
            cote -= 1

            if cote == 0:
                facing += 1
                cote = select_perso[1][5]


def draw_game():
    global troupe, tour, pos, select_perso

    img = pyxel.Image(pyxel.width, pyxel.height)
    img.load(0, 0, "../map/test.png")
    pyxel.blt(0, 0, img, pos[0]-pyxel.width//2, pos[1]-pyxel.height//2, pyxel.width, pyxel.height)

    draw_entity(troupe[0], 1, 2, "unite", ("square", 3))
    draw_entity(troupe[1], 1, 2, "unite", ("square", 8))

    if select_perso is not None:
        draw_entity(select_perso[2], 0, 1)
        pyxel.rect(pyxel.width - 50, pyxel.height - 50, 50, 50, 0)
        try:
            name = data.trad[data.lang][select_perso[1][0]]
        except KeyError:
            name = select_perso[1][0]
        pyxel.text(pyxel.width - 45, pyxel.height - 45, f"{name}\n\n{select_perso[1][3]}", 7)


