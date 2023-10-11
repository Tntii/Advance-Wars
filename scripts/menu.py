import pyxel
import data
btn = ()


def update_menu(step):
    if step == "main menu":
        return main_menu()
    elif step == "settings":
        return settings()
    return step


def draw_menu():
    global btn

    for i in btn:

        try:
            name = data.trad[data.lang][i[0]]
        except KeyError:
            name = i[0]

        if i[1] <= pyxel.mouse_x <= i[1] + i[3] and i[2] <= pyxel.mouse_y <= i[2] + i[4]:
            pyxel.rect(i[1], i[2], i[3], i[4], i[5][1])
            pyxel.text(i[1] + i[3] / 2 - 1.75*len(name), i[2] + i[4] / 2, name, i[6][1])
        else:
            pyxel.rect(i[1], i[2], i[3], i[4], i[5][0])
            pyxel.text(i[1] + i[3] / 2 - 1.75*len(name), i[2] + i[4] / 2, name, i[6][0])


def main_menu():
    global btn

    btn = (
        ("PLAY", 150, 150, 200, 50, (1, 2), (7, 8)),
        ("SETTINGS", 150, 225, 200, 50, (1, 2), (7, 8)),
        ("QUIT", 150, 300, 200, 50, (1, 2), (7, 8))
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
        ("BACK", 150, 225, 200, 50, (1, 2), (7, 8))
    )

    for i in btn:
        if i[1] <= pyxel.mouse_x <= i[1] + i[3] and i[2] <= pyxel.mouse_y <= i[2] + i[4] and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            if i[0] == "BACK":
                return "main menu"
            elif i[0] == "LANGUAGE":
                if data.lang == "Francais":
                    data.lang = "English"
                else:
                    data.lang = "Francais"
    return "settings"
