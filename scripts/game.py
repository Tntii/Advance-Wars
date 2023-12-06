import pyxel, data, menu

troupe = []

'''pos_x, pos_y, color, etape de capture'''
build = []

collision = ()

tour = 0
pos = [120, 80]
select_perso = None
action = ""
current_map = ""


def init_game():
    global collision, build, troupe, current_map, pos

    pos = [120, 80]
    data.load_texture(data.current_map)
    build = data.map[data.current_map]["build"][:]
    troupe = data.map[data.current_map]["troupe"][:]

    for i in range(2):
        for unite in range(len(troupe[i])):
            troupe[i][unite][3] = data.troupe_stats[troupe[i][unite][0]]["pv"]

    collision = data.map[data.current_map]["collision"]
    sort_troupe()
    return "in game"


def is_correct(cases, startPoint, endPoint, rayon):
    node = [(startPoint, 0, get_arround(cases, startPoint))]

    if endPoint in get_arround(cases, startPoint):
        return True

    while node:
        current_point = node[-1]
        while current_point[2]:
            dist = current_point[1]
            while dist <= rayon:
                if node[-1][0] == endPoint:
                    return True
                dist += 1
                if current_point[2]:
                    node.append((current_point[2][0], dist, get_arround(cases, current_point[2][0])))
                current_point = node[-1]
            node.pop(-1)
            if node and node[-1][2]:
                node[-1][2].pop(0)
            elif not node:
                return False
        if node:
            node.pop(-1)
    return False


def get_arround(cases, point):
    arround = []

    if (point[0] + 16, point[1]) in cases:
        arround.append((point[0] + 16, point[1]))
    if (point[0] - 16, point[1]) in cases:
        arround.append((point[0] - 16, point[1]))
    if (point[0], point[1] + 16) in cases:
        arround.append((point[0], point[1] + 16))
    if (point[0], point[1] - 16) in cases:
        arround.append((point[0], point[1] - 16))
    return arround


def menu_action(action):
    global tour, select_perso

    if action == "action":
        action = menu.action(can_capture(troupe[tour][select_perso[3]], tour), can_attack())

        if action == "Wait":
            troupe[tour][select_perso[3]][4] = False
            select_perso = None
            sort_troupe()
            return ""
        elif action == "Cancel":
            troupe[tour][select_perso[3]][1] = select_perso[1][1]
            troupe[tour][select_perso[3]][2] = select_perso[1][2]
            select_perso = None
            return ""
    elif action == "r action":
        action = menu.r_action()

        if action == "Menu":
            return "main menu ig"
        elif action == "End":
            for unite in troupe[tour]:
                unite[4] = True
            tour += 1
            if tour > 1:
                tour = 0
            heal()
            return ""
    elif action == "Attack":
        action = menu.attack()

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

            correct = True
            for col in range(5, data.troupe_stats[select_perso[1][0]]["collide lvl"], -1):
                if (case_x//16, case_y//16) in collision[col]:
                    correct = False
                    break

            for color in range(len(troupe)):
                if not correct:
                    break
                for unite in troupe[color]:
                    if (case_x, case_y) == (unite[1], unite[2]):
                        correct = False
                        break

            if correct:
                select_perso[2].append((case_x, case_y))
        cote -= 1

        if cote == 0:
            facing += 1
            cote = data.troupe_stats[select_perso[1][0]]["r_deplacement"]

    # vérifie si il est possible d'y aller
    if not get_arround(select_perso[2], (select_perso[1][1], select_perso[1][2])):
        select_perso[2] = []

    for case in select_perso[2]:
        if is_correct(select_perso[2], (select_perso[1][1], select_perso[1][2]), case, data.troupe_stats[select_perso[1][0]]["r_deplacement"]):
            select_perso[2].remove(case)

    select_perso[2].append((select_perso[1][1], select_perso[1][2]))


def camera_movement():
    global pos

    if pyxel.btn(data.command["up"][0]) and pos[1] - pyxel.height / 2 > 0:
        pos[1] -= 1
    elif pyxel.btn(data.command["down"][0]) and pos[1] + pyxel.height / 2 < data.map[data.current_map]["src"][1]:
        pos[1] += 1
    elif pyxel.btn(data.command["left"][0]) and pos[0] - pyxel.width / 2 > 0:
        pos[0] -= 1
    elif pyxel.btn(data.command["right"][0]) and pos[0] + pyxel.width / 2 < data.map[data.current_map]["src"][0]:
        pos[0] += 1


def get_ennemi_index(ally_index):
    if ally_index == 1:
        return 0
    return 1


def can_attack():
    target = []
    for unite in troupe[get_ennemi_index(tour)]:
        if data.troupe_stats[select_perso[1][0]]["r_cant_attack"] * 16 <= abs(unite[1] - troupe[tour][select_perso[3]][1]) + abs(unite[2] - troupe[tour][select_perso[3]][2]) <= data.troupe_stats[troupe[tour][select_perso[3]][0]]["r_attack"] * 16:
            target.append((unite[1], unite[2]))
    return target


def attack_func(atk, deff):
    global tour, select_perso
    ennemi = get_ennemi_index(tour)
    deff = troupe[ennemi].index(deff)
    print(round(data.troupe_stats[troupe[tour][atk][0]]["attack"] * (troupe[tour][atk][3] / data.troupe_stats[troupe[tour][atk][0]]["pv"]), 2))
    print(troupe[ennemi][deff][3] - round(data.troupe_stats[troupe[tour][atk][0]]["attack"] * (troupe[tour][atk][3] / data.troupe_stats[troupe[tour][atk][0]]["pv"]), 2))

    troupe[ennemi][deff][3] -= round(data.troupe_stats[troupe[tour][atk][0]]["attack"] * (troupe[tour][atk][3] / data.troupe_stats[troupe[tour][atk][0]]["pv"]), 2)

    if troupe[ennemi][deff][3] > 0 and data.troupe_stats[troupe[ennemi][deff][0]]["r_cant_attack"] * 16 <= abs(troupe[tour][atk][1] - troupe[ennemi][deff][1]) + abs(troupe[tour][atk][2] - troupe[ennemi][deff][2]) <= data.troupe_stats[troupe[ennemi][deff][0]]["r_attack"] * 16:
        troupe[tour][atk][3] -= round(data.troupe_stats[troupe[ennemi][deff][0]]["attack"] * (troupe[ennemi][deff][3] / data.troupe_stats[troupe[ennemi][deff][0]]["pv"]), 2)
    elif troupe[ennemi][deff][3] < 0:
        troupe[ennemi].pop(deff)

    if troupe[tour][atk][3] <= 0:
        troupe[tour].pop(atk)


def can_capture(atk, tour):
    if atk[0] in ("infantry", "heavy infantry"):
        for type in build:
            for bat in type:
                if (atk[1], atk[2]) == (bat[0], bat[1]) and (bat[2] != tour or bat[3] > 0):
                    return type, bat
    return False


def capture(atk, tour):
    indexs = can_capture(atk, tour)
    type = build.index(indexs[0])
    bat = build[type].index(indexs[1])

    if build[type][bat][2] == tour:
        build[type][bat][3] -= 1
    else:
        build[type][bat][3] += 1
        key = tuple(data.build_stats.keys())

        if build[type][bat][3] >= data.build_stats[key[type]]["nb_steps"]:
            if type == 0:
                win(tour)
            else:
                build[type][bat][2] = tour
                build[type][bat][3] = 0


def heal():
    for color in range(2):
        for unite in troupe[color]:
            for type in range(2):
                for b in build[type]:
                    if (b[0], b[1]) == (unite[1], unite[2]) and b[2] == color and unite[3] < data.troupe_stats[unite[0]]["pv"]:
                        unite[3] += round(data.troupe_stats[unite[0]]["pv"] / 4, 2)

                        if unite[3] > data.troupe_stats[unite[0]]["pv"]:
                            unite[3] = data.troupe_stats[unite[0]]["pv"]


def have_win():
    player = 0
    for i in troupe:
        if not i:
            win(get_ennemi_index(player))
        player += 1


def win(player):
    global action

    action = "w" + str(player)


def sort_troupe():
    global troupe
    s_troupe = []
    for i in range(2):
        s_troupe.append([])
        for unite in troupe[i]:
            for s_unite in range(len(s_troupe[i])):
                if s_troupe[i] and unite[2] < s_troupe[i][s_unite][2]:
                    s_troupe[i].insert(s_unite, unite)
                    break
                elif not s_troupe[i]:
                    s_troupe[i].append(unite)
                    break
            if unite not in s_troupe[i]:
                s_troupe[i].append(unite)
    troupe = s_troupe[:]


def update_game():
    global troupe, pos, select_perso, tour, collision, action

    action = menu_action(action)
    have_win()

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
            if not onCase and action == "":
                select_perso = None

        elif action == "Attack":
            for unite in troupe[get_ennemi_index(tour)]:
                if on_case(pos, (unite[1], unite[2])) and abs(unite[1] - troupe[tour][select_perso[3]][1]) + abs(unite[2] - troupe[tour][select_perso[3]][2]) <= data.troupe_stats[troupe[tour][select_perso[3]][0]]["r_attack"]*16:
                    attack_func(select_perso[3], unite)
                    action = ""
                    troupe[tour][select_perso[3]][4] = False
                    select_perso = None

        elif action == "Capture":
            capture(troupe[tour][select_perso[3]], tour)
            action = ""
            troupe[tour][select_perso[3]][4] = False
            select_perso = None

        elif action != "action":
            select_perso = None

    elif pyxel.btnr(pyxel.MOUSE_BUTTON_RIGHT):
        action = "r action"

    else:
        camera_movement()

    if action == "main menu":
        action = ""
        return "main menu"

    elif action == "main menu ig":
        action = ""
        return "main menu ig"

    elif action != "" and action[0] == "w":
        return action

    elif action == "Give up":
        win(get_ennemi_index(tour))

    return "in game"


def draw_entity(liste, index_x, index_y, type="", texture=("square", 0)):
    global pos

    for entity in liste:
        if entity[index_x] - pyxel.width / 2 <= pos[0] <= entity[index_x] + pyxel.width / 2 + 16 and entity[index_y] - pyxel.height / 2 - 16 <= pos[1] <= entity[index_y] + pyxel.height / 2 + 16:
            pos_x = pyxel.width//2+(entity[index_x]-pos[0])
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
                    t_name = "idle"

                    if not entity[4]:
                        t_name = "have move"

                    src = data.troupe_stats[entity[0]]["animation"][t_name][texture[1]][pyxel.frame_count//16%3]
                    pyxel.blt(pos_x, pos_y, data.texture[type], src[0], src[1], 16, 16, 14)

                elif type == "build":
                    src = data.build_stats[name_init]["animation"][entity[2]][pyxel.frame_count//32%2]
                    pyxel.blt(pos_x, pos_y - 16, data.texture[type], src[0], src[1], 15, 31, 0)

                elif type in ("case", "target"):
                    pyxel.blt(pos_x, pos_y, data.texture[type], 0, 0, 16, 16, 13)


def draw_stats(liste, index_x, index_y, type):

    for entity in liste:

        if type == "unite" and select_perso is None and on_case(pos, (entity[index_x], entity[index_y])):
            pyxel.rect(pyxel.width - 65, pyxel.height - 50, 65, 50, 0)
            pyxel.text(pyxel.width - 60, pyxel.height - 45, f"{data.traducteur(entity[0])}\n\n"
                                                            f"{data.traducteur('hp')}: {entity[3]}/{data.troupe_stats[entity[0]]['pv']}\n"
                                                            f"{data.traducteur('damage')}: {data.troupe_stats[entity[0]]['attack']}\n"
                                                            f"{data.traducteur('reach')}: {data.troupe_stats[entity[0]]['r_cant_attack']}-{data.troupe_stats[entity[0]]['r_attack']}\n"
                                                            f"{data.traducteur('col lvl')}: {data.troupe_stats[entity[0]]['collide lvl']}", 7)

        elif type[:5] == "build" and select_perso is None and on_case(pos, (entity[index_x], entity[index_y])):
            pyxel.rect(pyxel.width - 65, pyxel.height - 50, 65, 50, 0)
            pyxel.text(pyxel.width - 60, pyxel.height - 45, f"{data.traducteur(type[6:])}\n\ncapture: {entity[3]}/{data.build_stats[type[6:]]['nb_steps']}", 7)


def draw_game():
    global troupe, tour, pos, select_perso, action

    pyxel.blt(0, 0, data.texture["map"], pos[0]-pyxel.width/2, pos[1]-pyxel.height/2, pyxel.width+6, pyxel.height+6)

    for b in range(len(build)):
        draw_entity(build[b], 0, 1, "build", ("sprite", b))

    for unite in range(len(troupe)):
        draw_entity(troupe[unite], 1, 2, "unite", ("sprite", unite))

    if not pyxel.btn(data.command["hide stats"][0]) and select_perso is None:
        draw_stats(build[0], 0, 1, "build HQ")
        draw_stats(build[1], 0, 1, "build city")

        for unite in range(len(troupe)):
            draw_stats(troupe[unite], 1, 2, "unite")

    if select_perso is not None:
        if action == "":
            draw_entity(select_perso[2], 0, 1, "case", ("sprite"))

        if not pyxel.btn(data.command["hide stats"][0]):
            pyxel.rect(pyxel.width - 65, pyxel.height - 50, 65, 50, 0)
            pyxel.text(pyxel.width - 60, pyxel.height - 45, f"{data.traducteur(select_perso[1][0])}\n\n{select_perso[1][3]}", 7)

    if action in ("action", "r action", "Attack"):
        if not pyxel.btn(data.command["hide stats"][0]):
            menu.draw_menu()
        if action == "Attack":
            draw_entity(can_attack(), 0, 1, "target", ("sprite"))


def draw_win_screen(player):
    pyxel.text(100, 80, data.traducteur(player), 7)
    return menu.game_over(player)
