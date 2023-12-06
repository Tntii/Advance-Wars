import pyxel
import data
btn = ()


def update_menu(step):
    if step[:9] == "main menu":
        return main_menu(step)
    elif step == "settings":
        return settings()
    elif step == "key" or step[:10] == "wait entry":
        return key_setting(step)
    elif step == "choice map":
        return map_choice()
    return step


def draw_menu(bg=None):
    global btn

    if bg is not None:
        img = pyxel.Image(1000, 1000)
        img.load(0, 0, bg)
        pyxel.blt(-6, -6, img, 0, 0, pyxel.width + 6, pyxel.height + 6)

    for i in btn:
        name = data.traducteur(i[0])
        if i[1] <= pyxel.mouse_x <= i[1] + i[3] and i[2] <= pyxel.mouse_y <= i[2] + i[4]:
            pyxel.rect(i[1], i[2], i[3], i[4], i[5][1])
            pyxel.text(i[1] + i[3] / 2 - 1.75*len(name), i[2] + i[4] / 2 - 2, name, i[6][1])
        else:
            pyxel.rect(i[1], i[2], i[3], i[4], i[5][0])
            pyxel.text(i[1] + i[3] / 2 - 1.75*len(name), i[2] + i[4] / 2 - 2, name, i[6][0])


def interract(btn, no_click):
    for i in btn:
        if i[1] <= pyxel.mouse_x <= i[1] + i[3] and i[2] <= pyxel.mouse_y <= i[2] + i[4] and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            return i[0]
    return no_click


def main_menu(ig):
    global btn

    btn = (
        ("PLAY", 70, 20, 100, 30, (11, 3), (7, 11)),
        ("SETTINGS", 70, 70, 100, 30, (13, 5), (7, 13)),
        ("QUIT", 70, 120, 45, 20, (8, 4), (7, 8)),
        ("Credits", 125, 120, 45, 20, (12, 5), (7, 12))
    )

    event = interract(btn, ig)
    if event == "PLAY" and ig == "main menu":
        return "choice map"
    elif event == "PLAY" and ig == "main menu ig":
        return "in game"
    elif event == "QUIT":
        pyxel.quit()
    elif event == "SETTINGS":
        return "settings"
    return event


def map_choice():
    global btn

    btn = (("<", 70, 70, 10, 15, (13, 5), (7, 13)),
           (data.current_map, 80, 70, 80, 15, (13, 5), (7, 13)),
           (">", 160, 70, 10, 15, (13, 5), (7, 13))
           )

    event = interract(btn, "choice map")

    keys = list(data.map.keys())
    index = keys.index(data.current_map)

    if event == ">":
        if index + 1 < len(data.map):
            index += 1
        else:
            index = 0
        data.current_map = keys[index]

    elif event == "<":
        if index - 1 > 0:
            index -= 1
        else:
            index = len(data.map) - 1
        data.current_map = keys[index]

    elif event == data.current_map:
        return "map: " + data.current_map
    return "choice map"


def settings():
    global btn

    btn = (
        ("LANGUAGE", 70, 20, 100, 20, (12, 5), (7, 1)),
        ("off", 70, 50, 33, 20, (8, 4), (7, 8)),
        (str(data.main_volume), 103, 50, 33, 20, (1, 1), (7, 7)),
        ("on", 136, 50, 33, 20, (11, 3), (7, 11)),
        ("Key", 70, 80, 100, 20, (10, 9), (7, 10)),
        ("BACK", 5, 135, 40, 20, (5, 1), (7, 5))
    )

    event = interract(btn, "settings")

    if event == "BACK":
        return "main menu"

    elif event == "LANGUAGE":
        keys = list(data.trad.keys())
        index = keys.index(data.lang)
        if index + 1 < len(data.trad):
            index += 1
        else:
            index = 0
        data.lang = keys[index]

    elif event == "off":
        data.main_volume = "OFF"
        pyxel.stop()

    elif event == "on" and data.main_volume != "ON":
        data.main_volume = "ON"
        data.next_music()

    elif event == "Key":
        return "key"

    return "settings"


def key_setting(stade):
    global btn
    key = tuple(data.command.keys())
    b = [(key[i] + ":" + data.command[key[i]][1], 70, i*30 + 10, 100, 20, (13, 1), (7, 7)) for i in range(0, len(key))]
    b.append(("BACK", 5, 135, 40, 20, (5, 1), (7, 5)))
    btn = tuple(b)
    event = interract(btn, "key")

    if stade == "key":
        if event not in ("key", "BACK"):
            return f"wait entry {event[:-2]}"
        if event == "BACK":
            return "settings"

    elif pyxel.input_keys:
        data.command[stade[11:]] = (pyxel.input_keys[0], pyxel.input_text[0])
        return "key"
    return stade


def action(can_capture, can_attack):
    global btn
    b = [("Wait", pyxel.width - 32, 20, 32, 15, (5, 1), (7, 5))]

    if can_attack:
        b.append(("Attack", pyxel.width - 32, b[-1][2] + 15, 32, 15, (5, 1), (7, 5)))

    if can_capture:
        b.append(("Capture", pyxel.width - 32, b[-1][2] + 15, 32, 15, (5, 1), (7, 5)))
    b.append(("Cancel", pyxel.width - 32, b[-1][2] + 15, 32, 15, (5, 1), (7, 5)))
    btn = tuple(b)

    return interract(btn, "action")


def r_action():
    global btn
    btn = (
        ("End", pyxel.width - 43, 20, 43, 15, (5, 1), (7, 5)),
        ("Give up", pyxel.width - 43, 35, 43, 15, (5, 1), (7, 5)),
        ("Menu", pyxel.width - 43, 50, 43, 15, (5, 1), (7, 5)),
        ("Continue", pyxel.width - 43, 65, 43, 15, (5, 1), (7, 5)),
    )

    event = interract(btn, "r action")

    if event == "Continue":
        return ""
    return event


def attack():
    global btn

    btn = (("Cancel", pyxel.width - 32, 20, 32, 15, (5, 1), (7, 5)), ("Cancel", pyxel.width - 32, 20, 32, 15, (5, 1), (7, 5)))

    event = interract(btn, "Attack")

    if event == "Cancel":
        return "action"
    return event


def game_over(p):
    global btn

    btn = (("Back to menue", 10, 135, 65, 20, (5, 1), (7, 5)), ("", 0, 0, 0, 0, (0, 0), (0, 0)))

    event = interract(btn, "w"+p)

    if event == "Back to menue":
        return "main menu"

    return event
