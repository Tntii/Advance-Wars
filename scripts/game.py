import pyxel, data, menu, csv

troupe = [
        [["soldier", 80, 80, 50], ["soldier", 96, 96, 70]],
        []
        ]

tour = 0
pos = [250, 250]
haveMove = True


def update_game():
    global troupe, pos, haveMove

    if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
        for unite in troupe[tour]:
            if unite[1] <= pyxel.mouse_x <= unite[1] + 16 and unite[2] <= pyxel.mouse_y <= unite[2] + 16:
                troupe[1].append(unite)
    elif pyxel.btn(pyxel.KEY_Z):
        pos[1] -= 2
        haveMove = True
    elif pyxel.btn(pyxel.KEY_S):
        pos[1] += 2
        haveMove = True
    elif pyxel.btn(pyxel.KEY_Q):
        pos[0] -= 2
        haveMove = True
    elif pyxel.btn(pyxel.KEY_D):
        pos[0] += 2
        haveMove = True
    else:
        haveMove = False


def draw_game():
    global troupe, tour, pos, haveMove

    team_color = 0
    img = pyxel.Image(pyxel.width, pyxel.height)
    img.load(0, 0, "../texture/img.png")
    pyxel.blt(0, 0, img, pos[0]-pyxel.width//2, pos[1]-pyxel.height//2, pyxel.width, pyxel.height)

    for i in troupe:
        for unite in i:
            if team_color == 0:
                pyxel.rect(unite[1], unite[2], 16, 16, 3)
            else:
                pyxel.rect(unite[1], unite[2], 16, 16, 5)

            if unite[1] <= pyxel.mouse_x <= unite[1] + 16 and unite[2] <= pyxel.mouse_y <= unite[2] + 16:
                pyxel.rect(pyxel.width - 50, pyxel.height - 50, 50, 50, 0)
                try:
                    name = data.trad[data.lang][unite[0]]
                except KeyError:
                    name = unite[0]
                pyxel.text(pyxel.width - 45, pyxel.height - 45, f"{name}\n\n{unite[3]}", 7)
        team_color += 1