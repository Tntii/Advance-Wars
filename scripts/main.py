import pyxel
import menu, game, data

step = "main menu"


def update():
    global step

    if pyxel.frame_count % 9000 == 0 and data.main_volume == "ON":
        data.next_music()

    if step in ("main menu", "settings", "key", "choice map", "Credits") or step[:10] == "wait entry":
        step = menu.update_menu(step)
    elif step[:5] == "map: ":
        step = game.init_game()
    elif step == "in game":
        step = game.update_game()


def draw_credits():
    y = 20
    data.credit.seek(0)
    for line in data.credit:
        pyxel.text(20, y, line, 7)
        y += 10


def draw():
    global step
    pyxel.cls(0)

    if step in ("main menu", "settings", "key", "choice map", "Credits") or step[:10] == "wait entry" or step[:1] == "w":
        menu.draw_menu()
    elif step == "in game":
        game.draw_game()
    if step[0] == "w" and len(step) == 2:
        step = game.draw_win_screen(step[1])
    elif step == "Credits":
        draw_credits()


pyxel.init(240, 160, fps=60)
pyxel.mouse(True)
data.load_music()
pyxel.run(update, draw)