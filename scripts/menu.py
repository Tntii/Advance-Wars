import pyxel
import data
btn = ()


def update_menu(step):
    if step == "main menu":
        return main_menu()
    elif step == "settings":
        return settings()
    return step


def draw_menu(bg=None):
    global btn

    if bg is not None:
        img = pyxel.Image(1000, 1000)
        img.load(0, 0, bg)
        pyxel.blt(-6, -6, img, 0, 0, pyxel.width + 6, pyxel.height + 6)

    for i in btn:

        try:
            name = data.trad[data.lang][i[0]]
        except KeyError:
            name = i[0]

        if i[1] <= pyxel.mouse_x <= i[1] + i[3] and i[2] <= pyxel.mouse_y <= i[2] + i[4]:
            pyxel.rect(i[1], i[2], i[3], i[4], i[5][1])
            pyxel.text(i[1] + i[3] / 2 - 1.75*len(name), i[2] + i[4] / 2 - 2, name, i[6][1])
        else:
            pyxel.rect(i[1], i[2], i[3], i[4], i[5][0])
            pyxel.text(i[1] + i[3] / 2 - 1.75*len(name), i[2] + i[4] / 2 - 2, name, i[6][0])


def main_menu():
    global btn

    btn = (
        ("PLAY", 90, 20, 60, 20, (11, 3), (7, 7)),
        ("SETTINGS", 90, 70, 60, 20, (13, 1), (7, 7)),
        ("QUIT", 90, 120, 60, 20, (8, 4), (7, 7))
    )

    for i in btn:
        if i[1] <= pyxel.mouse_x <= i[1] + i[3] and i[2] <= pyxel.mouse_y <= i[2] + i[4] and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            if i[0] == "PLAY":
                return "in game"
            elif i[0] == "QUIT":
                pyxel.quit()
            elif i[0] == "SETTINGS":
                return "settings"
    return "main menu"


def settings():
    global btn

    btn = (
        ("LANGUAGE", 150, 105, 200, 50, (1, 2), (7, 8)),
        ("-", 200, 225, 25, 25, (1, 2), (7, 8)),
        (str(data.main_volume), 238, 225, 25, 25, (1, 1), (7, 7)),
        ("+", 276, 225, 25, 25, (1, 2), (7, 8)),
        ("BACK", 150, 300, 200, 50, (1, 2), (7, 8))
    )

    for i in btn:
        if i[1] <= pyxel.mouse_x <= i[1] + i[3] and i[2] <= pyxel.mouse_y <= i[2] + i[4] and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            if i[0] == "BACK":
                return "main menu"

            elif i[0] == "LANGUAGE":
                keys = list(data.trad.keys())
                index = keys.index(data.lang)
                if index + 1 < len(data.trad):
                    index += 1
                else:
                    index = 0
                data.lang = keys[index]

            elif i[0] == "-" and data.main_volume >= 5:
                data.main_volume -= 5

            elif i[0] == "+" and data.main_volume <= 95:
                data.main_volume += 5
    return "settings"


def action():
    global btn
    btn = (
        ("Wait", pyxel.width - 50, 20, 50, 25, (1, 2), (7, 8)),
        ("Attack", pyxel.width - 50, 50, 50, 25, (1, 2), (7, 8)),
        ("Cancel", pyxel.width - 50, 80, 50, 25, (1, 2), (7, 8))
    )
    for i in btn:
        if i[1] <= pyxel.mouse_x <= i[1] + i[3] and i[2] <= pyxel.mouse_y <= i[2] + i[4] and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            return i[0]
    return "action"


def r_action():
    global btn
    btn = (
        ("End", pyxel.width - 50, 50, 50, 25, (1, 2), (7, 8)),
        ("Give up", pyxel.width - 50, 110, 50, 25, (1, 2), (7, 8)),
        ("Menu", pyxel.width - 50, 80, 50, 25, (1, 2), (7, 8)),
    )
    for i in btn:
        if i[1] <= pyxel.mouse_x <= i[1] + i[3] and i[2] <= pyxel.mouse_y <= i[2] + i[4] and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            return i[0]
    return "r action"
