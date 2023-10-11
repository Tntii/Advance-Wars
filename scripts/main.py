import pyxel
import menu

step = "main menu"


def update():
    global step

    step = menu.update_menu(step)


def draw():
    global step
    pyxel.cls(0)

    menu.draw_menu()


pyxel.init(500, 500)
pyxel.mouse(True)
pyxel.run(update, draw)