import pyxel

class Menu:
    def __init__(self):
        self.colors = [1,2,4,5,6,8,9,10,12,13,14,15]
        self.col1_id = 3
        self.col2_id = 5

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btn(pyxel.KEY_SPACE):
            if self.col1_id == self.col2_id:
                pass
            else:
                Jeu(self.colors[self.col1_id])

        if pyxel.btnp(pyxel.KEY_RIGHT):
            if self.col1_id == 11:
                self.col1_id = 0
            else: self.col1_id += 1
        elif pyxel.btnp(pyxel.KEY_LEFT):
            if self.col1_id == 0:
                self.col1_id = 11
            else: self.col1_id -= 1

    def draw(self):
        pyxel.mouse(True)
        pyxel.cls(0)
        pyxel.text(5,6,"test",7)
        pyxel.circ(124,160,6,self.colors[self.col1_id])
        pyxel.circ(180, 160, 6, self.colors[self.col2_id])

class Jeu:
    def __init__(self, col1, col2):
        self.j1 = Joueur(0, self.col1)
        pyxel.run(self.update, self.draw)

    def update(self):
        self.j1.update()

    def draw(self):
        pyxel.cls(11)
        self.j1.draw()


class Joueur:
    def __init__(self, team, color):
        """
        :param team: équipe
        :param color: couleur
        """
        self.team = team
        self.x = 10
        self.y = 10
        self.size = 6
        self.points = 0
        self.speed = 3
        self.color = color

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

##############################################################

class App:
    """classe mère qui lance la fenêtre"""
    def __init__(self):
        pyxel.init(320, 180, title='test')
        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        Menu()

App()
