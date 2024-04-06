import pyxel

class App:
    def __init__(self):
        pyxel.init(320, 180, title='test')
        self.j1 = Joueur('téliau', 0, 5)
        pyxel.run(self.update, self.draw)

    def update(self):
        self.j1.update()

    def draw(self):
        pyxel.cls(0)
        self.j1.draw()


class Joueur:
    def __init__(self, name, team, color):
        self.name = name
        self.team = team
        self.x = 10
        self.y = 10
        self.size = 6
        self.points = 0
        self.speed = 3
        self.color = color
        self.prev_color = self.color

    def update(self):
        if pyxel.btn(pyxel.KEY_Z):
            self.y = self.y - self.speed
        elif pyxel.btn(pyxel.KEY_S):
            self.y = self.y + self.speed
        elif pyxel.btn(pyxel.KEY_Q):
            self.x = self.x - self.speed
        elif pyxel.btn(pyxel.KEY_D):
            self.x = self.x + self.speed

    def draw(self):
        pyxel.circ(self.x, self.y, self.size, self.color)


App()
