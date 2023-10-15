import pyxel


class Camera:

    def __init__(self):
        self.color = {"(0, 0, 0, 255)": 0, "(255, 255, 255, 255)": 7, "(212, 24, 108, 255)": 8, "(118, 150, 222, 255)": 12, "(112, 198, 169, 255)": 11}

    def deplacement(self, pos, map, color_ban=()):
        for y in range(0, pyxel.height):
            for x in range(0, pyxel.width):
                color = map.getpixel((pos[0] - pyxel.width//2 + x, pos[1] - pyxel.height//2 + y))
                if color not in color_ban:
                    pyxel.pset(x, y, self.color[str(color)])

