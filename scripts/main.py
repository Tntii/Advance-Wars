import pyxel
import menu, game

step = "main menu"


def update():
    global step

    if step == "main menu" or step == "settings":
        step = menu.update_menu(step)
    elif step == "in game":
        step = game.update_game()


def draw():
    global step
    pyxel.cls(0)

    if step == "main menu" or step == "settings":
        menu.draw_menu()
    elif step == "in game":
        game.draw_game()


pyxel.init(512, 512)
pyxel.mouse(True)

pyxel.run(update, draw)