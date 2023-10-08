import pyxel
from PIL import Image
from camera import Camera


class Map:

    def __init__(self, map_file):
        pyxel.init(20, 20)
        self.pos = [50, 50]
        self.map = Image.open(map_file)
        self.collision = Image.new("RGBA",(self.map.width, self.map.height), (255, 255, 255, 255) )
        self.camera = Camera()
        self.current_type = 0
        self.color_type = ((0, 0, 0, 255), (212, 24, 108, 255), (112, 198, 169, 255), (118, 150, 222, 255), (255, 255, 255, 255))
        self.color_palet = {"(0, 0, 0, 255)": 0, "(255, 255, 255, 255)": 7, "(212, 24, 108, 255)": 8, "(118, 150, 222, 255)": 12, "(112, 198, 169, 255)": 11}
        self.current_coord = []
        self.collision_visible = True
        self.entity = [[10, 0, 0]] #size, x, y

        pyxel.run(self.update, self.draw)

    def update(self):

        if pyxel.btn(pyxel.KEY_Z) and 0 + pyxel.height//2 <= self.pos[1] - 1 <= self.map.height - pyxel.height//2:
            self.pos[1] -= 1
        elif pyxel.btn(pyxel.KEY_S) and 0 + pyxel.height//2 <= self.pos[1] + 1 <= self.map.height - pyxel.height//2:
            self.pos[1] += 1
        elif pyxel.btn(pyxel.KEY_Q) and 0 + pyxel.width//2 <= self.pos[0] - 1 <= self.map.width - pyxel.width//2:
            self.pos[0] -= 1
        elif pyxel.btn(pyxel.KEY_D) and 0 + pyxel.width//2 <= self.pos[0] + 1 <= self.map.width - pyxel.width//2:
            self.pos[0] += 1
        if pyxel.btnp(pyxel.KEY_E):
            self.collision_visible = not self.collision_visible

        if pyxel.btnp(pyxel.KEY_UP):
            if self.current_type < len(self.color_type)-1:
                self.current_type += 1
            else:
                self.current_type = 0
        elif pyxel.btnp(pyxel.KEY_DOWN):
            if self.current_type > 0:
                self.current_type -= 1
            else:
                self.current_type = len(self.color_type)-1
        if pyxel.btnp(pyxel.KEY_BACKSPACE):
            self.current_type = 4

        self.setCollision()

    def draw(self):
        pyxel.cls(0)
        self.camera.deplacement(self.pos, self.map)

        if self.collision_visible:
            self.camera.deplacement(self.pos, self.collision, [(255, 255, 255, 255)])
        pyxel.pset(pyxel.mouse_x, pyxel.mouse_y, self.color_palet[str(self.color_type[self.current_type])])

    def setCollision(self):
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            self.current_coord.append((self.pos[0] - pyxel.width//2 + pyxel.mouse_x,self.pos[1] - pyxel.height//2 + pyxel.mouse_y))

        elif pyxel.btnp(pyxel.MOUSE_BUTTON_RIGHT):
            self.current_coord = []

        if len(self.current_coord) == 2:
            for y in range(0, max(self.current_coord[0][1], self.current_coord[1][1]) - min(self.current_coord[0][1], self.current_coord[1][1]) + 1):
                for x in range(0,  max(self.current_coord[0][0], self.current_coord[1][0]) - min(self.current_coord[0][0], self.current_coord[1][0]) + 1):
                    self.collision.putpixel((min(self.current_coord[0][0], self.current_coord[1][0]) + x, min(self.current_coord[1][1], self.current_coord[0][1]) + y), self.color_type[self.current_type])

            self.current_coord = []


Map("New Piskel (9)-1.png")