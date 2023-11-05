import pyxel, data, menu
from Dijkstra import Dijkstra as D

troupe = [
        [
            ["soldier", 80, 80, 10, True]
        ],
        [
            ["soldier", 96, 80, 10, True]
        ]
        ]

'''pos_x, pos_y, color, etape de capture'''
build = [
    [
        [16, 16, 0, 0],
        [32, 16, 1, 0]
    ],
    [
    ]
]

collision = ((80, 96), (96, 96), (64, 96))

tour = 0
pos = [0, 0]
select_perso = None
action = ""




'''def Dijkstra(map, startPoint1, endPoint):
    startPoint = startPoint1
    isSmalest = False
    dist = 0
    table = []
    blackList = []
    road = []

    #isSmalest est la variable qui dit si le point d'arriver est le plus petit
    while not isSmalest:
        currentIndex = 0
        minIndex = None
        isBL = False
        min = None
        dist = 0

        # on cherche actuellement la route la plus petite
        for i in table:
            if min is None or min > i[1]:
                for bl in blackList:
                    if bl == i[2]:
                        isBL = True
                        break
                if not isBL:
                    min = i[1]
                    minIndex = currentIndex

            isBL = False
            currentIndex += 1

        if len(table) > 0 and minIndex is not None:
            startPoint = table[minIndex][2]
            dist = table[minIndex][1]

            if startPoint == endPoint:
                isSmalest = True


        # on ajoute tout les nouveaux point accessible à partir du startpoint
        if not isSmalest:
            for i in map.get(startPoint).keys():
                for bl in blackList:

                    if bl == i:
                        isBL = True
                        break

                if not isBL and map.get(startPoint).get(i) is not None:
                    table.append((startPoint, dist + map.get(startPoint).get(i), i))
                    blackList.append(startPoint)

                    isBL = False

        road = [startPoint]

        while startPoint != startPoint1:
            currentIndex = 0
            minIndex = None
            min = None

            for i in table:
                if i[2] == startPoint and (min is None or i[1] <= min):
                    min = table[currentIndex][1]
                    minIndex = currentIndex

                currentIndex += 1

            startPoint = table[minIndex][0]
            dist += map.get(table[minIndex][0]).get(table[minIndex][2])
            road.insert(0, startPoint)
    return dist'''


def menu_action(action):
    global tour, select_perso

    if action == "action":
        action = menu.action()

        if action == "Wait":
            troupe[tour][select_perso[3]][4] = False
            select_perso = None
            return ""
        elif action == "Cancel":
            troupe[tour][select_perso[3]][1] = select_perso[1][1]
            troupe[tour][select_perso[3]][2] = select_perso[1][2]
            select_perso = None
            return ""
    elif action == "r action":
        action = menu.r_action()

        if action == "Menu":
            return "main menu"
        elif action == "End":
            for unite in troupe[tour]:
                unite[4] = True
            tour += 1
            if tour > 1:
                tour = 0
            return ""
    return action


def on_case(pos, case):
    return pyxel.width / 2 + (case[0] - pos[0]) <= pyxel.mouse_x <= pyxel.width / 2 + (case[0] - pos[0]) + 16 and pyxel.height / 2 + (case[1] - pos[1]) <= pyxel.mouse_y <= pyxel.height / 2 + (case[1] - pos[1]) + 16


def case_coord():
    global select_perso
    cote = data.troupe_stats[select_perso[1][0]]["r_deplacement"]
    facing = 0
    case_x = 0
    case_y = 0

    # ajout des cases théorique ou on peut aller
    for i in range(cote * 4):
        for case in range(cote):
            if facing == 0:
                case_x = select_perso[1][1] - case * 16
                case_y = select_perso[1][2] - (data.troupe_stats[select_perso[1][0]]["r_deplacement"] - cote + 1) * 16
            elif facing == 1:
                case_x = select_perso[1][1] - (data.troupe_stats[select_perso[1][0]]["r_deplacement"] - cote + 1) * 16
                case_y = select_perso[1][2] + case * 16
            elif facing == 2:
                case_x = select_perso[1][1] + case * 16
                case_y = select_perso[1][2] + (data.troupe_stats[select_perso[1][0]]["r_deplacement"] - cote + 1) * 16
            elif facing == 3:
                case_x = select_perso[1][1] + (data.troupe_stats[select_perso[1][0]]["r_deplacement"] - cote + 1) * 16
                case_y = select_perso[1][2] - case * 16

            if (case_x, case_y) not in collision:
                onEnnemie = False
                if tour == 0:
                    color = 1
                else:
                    color = 0

                for i in troupe[color]:
                    if (case_x, case_y) == (i[1], i[2]):
                        onEnnemie = True

                if not onEnnemie:
                    select_perso[2].append((case_x, case_y))
        cote -= 1

        if cote == 0:
            facing += 1
            cote = data.troupe_stats[select_perso[1][0]]["r_deplacement"]

    map = {}
    for case in select_perso[2] + [(select_perso[1][1], select_perso[1][2])]:
        chemin = {}
        if (case[0] + 16, case[1]) in select_perso[2]:
            chemin[str((case[0] + 16, case[1]))] = 16
        if (case[0] - 16, case[1]) in select_perso[2]:
            chemin[str((case[0] - 16, case[1]))] = 16
        if (case[0], case[1] + 16) in select_perso[2]:
            chemin[str((case[0], case[1] + 16))] = 16
        if (case[0], case[1] - 16) in select_perso[2]:
            chemin[str((case[0], case[1] - 16))] = 16
        map[str(case)] = chemin

    # vérifie si il est possible d'y aller
    for case in select_perso[2]:
        D1 = D(map, str((select_perso[1][1], select_perso[1][2])), str(case))
        dist = D1.Dijkstra()

        if data.troupe_stats[select_perso[1][0]]["r_deplacement"] * 16 < dist:
            select_perso[2].remove(case)


def camera_movement():
    global pos

    if pyxel.btn(pyxel.KEY_Z):
        pos[1] -= 2
    elif pyxel.btn(pyxel.KEY_S):
        pos[1] += 2
    elif pyxel.btn(pyxel.KEY_Q):
        pos[0] -= 2
    elif pyxel.btn(pyxel.KEY_D):
        pos[0] += 2


def update_game():
    global troupe, pos, select_perso, tour, collision, action

    action = menu_action(action)

    if pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT):
        if select_perso is None:
            for i in range(2):
                for unite in troupe[i]:
                    if on_case(pos, (unite[1], unite[2])):
                        select_perso = [i, unite.copy(), [], troupe[i].index(unite)]
                        case_coord()

        elif select_perso[0] == tour and action == "" and select_perso[1][4]:
            onCase = False
            for case in select_perso[2]:
                if on_case(pos, case):
                    troupe[tour][select_perso[3]][1] = case[0]
                    troupe[tour][select_perso[3]][2] = case[1]
                    action = "action"
                    onCase = True
                    break
            if not onCase:
                select_perso = None
        else:
            select_perso = None

    elif pyxel.btnr(pyxel.MOUSE_BUTTON_RIGHT):
        action = "r action"

    else:
        camera_movement()

    if action == "main menu":
        action = ""
        return "main menu"
    return "in game"


def draw_entity(liste, index_x, index_y, type="", texture=("square", 0)):
    global pos

    for entity in liste:
        if entity[index_x] - pyxel.width // 2 <= pos[0] <= entity[index_x] + pyxel.width // 2 and entity[index_y] - pyxel.height // 2 <= pos[1] <= entity[index_y] + pyxel.height // 2:
            pos_x = pyxel.width/2+(entity[index_x]-pos[0])
            pos_y = pyxel.height//2+(entity[index_y]-pos[1])

            if type == "build":
                if texture[1] == 0:
                    name_init = "HQ"
                elif texture[1] == 1:
                    name_init = "city"

            if texture[0] == "square":
                pyxel.rect(pos_x, pos_y, 16, 16, texture[1])
            else:
                if type == "unite":
                    src = data.troupe_stats[entity[0]]["animation"]["idle"][texture[1]][pyxel.frame_count//8%3]
                    sprite = pyxel.Image(755, 1370)
                    sprite.load(0, 0, "../texture/spriteMap.png")
                    pyxel.blt(pos_x, pos_y, sprite, src[0], src[1], 16, 16, 14)
                elif type == "build":
                    src = data.build_stats[name_init]["animation"][entity[2]][pyxel.frame_count//16%2]
                    sprite = pyxel.Image(781, 1790)
                    sprite.load(0, 0, "../texture/tile.png")
                    pyxel.blt(pos_x, pos_y-16, sprite, src[0], src[1], 15, 31, 0)

        if type == "unite" and select_perso is None and on_case(pos, (entity[index_x], entity[index_y])):
            pyxel.rect(pyxel.width - 50, pyxel.height - 50, 50, 50, 0)
            try:
                name = data.trad[data.lang][entity[0]]
            except KeyError:
                    name = entity[0]
            pyxel.text(pyxel.width - 45, pyxel.height - 45, f"{name}\n\n{entity[3]}", 7)

        elif type == "build" and select_perso is None and on_case(pos, (entity[index_x], entity[index_y])):
            pyxel.rect(pyxel.width - 50, pyxel.height - 50, 50, 50, 0)

            try:
                name = data.trad[data.lang][name_init]
            except KeyError:
                name = name_init
            pyxel.text(pyxel.width - 45, pyxel.height - 45, f"{name}\n\n{entity[3]}", 7)


def draw_game():
    global troupe, tour, pos, select_perso, action

    img = pyxel.Image(1000, 1000)
    img.load(0, 0, "../map/test-color.png")
    #-/+6 pour par qu'il y'ai de bande noir
    pyxel.blt(-6, -6, img, pos[0]-pyxel.width/2, pos[1]-pyxel.height/2, pyxel.width+6, pyxel.height+6)

    draw_entity(troupe[0], 1, 2, "unite", ("sprite", 0))
    draw_entity(troupe[1], 1, 2, "unite", ("sprite", 1))
    draw_entity(build[0], 0, 1, "build", ("sprite", 0))

    if select_perso is not None:
        if action == "":
            draw_entity(select_perso[2], 0, 1)
        pyxel.rect(pyxel.width - 50, pyxel.height - 50, 50, 50, 0)
        try:
            name = data.trad[data.lang][select_perso[1][0]]
        except KeyError:
            name = select_perso[1][0]
        pyxel.text(pyxel.width - 45, pyxel.height - 45, f"{name}\n\n{select_perso[1][3]}", 7)
    if action in ("action", "r action"):
        menu.draw_menu()
