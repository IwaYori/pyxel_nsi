import pyxel

class Menu:
    def __init__(self):
        # initialisation de la liste des couleurs possibles
        self.colors = [1,2,4,5,8,9,10,12,13,14,15]
        # par défaut, joueur1 = colors[3] = 5 (bleu), joueur2 colors[4] = 8 (rouge)
        self.col1_id = 3
        self.col2_id = 4
        pyxel.run(self.update, self.draw)

    def update(self):

        # espace est la touche qui permet de lancer le jeu
        if pyxel.btn(pyxel.KEY_SPACE):
            # empêche de lancer le jeu si deux joueurs ont la même couleur et joue un son
            if self.col1_id == self.col2_id:
                pyxel.play(0,4)
            else:
                # lance le jeu avec comme paramètre les deux couleurs
                Jeu(self.colors[self.col1_id],self.colors[self.col2_id])

        # permet de changer la couleur du joueur 1 à l'aide:
        # de 'Q' ou 'D', ou d'un clique gauche ou droit sur le joueur 1
        if pyxel.btnp(pyxel.KEY_D):
            # pour éviter un dépassement d'indice:
            if self.col1_id == 10:
                self.col1_id = 0
            else: self.col1_id += 1
        elif pyxel.btnp(pyxel.KEY_Q):
            # pour éviter un dépassement d'indice:
            if self.col1_id == 0:
                self.col1_id = 10
            else: self.col1_id -= 1
        # vérification de la position de la souris sur le joueur 1
        elif 118 <= pyxel.mouse_x <= 130 and 166 >= pyxel.mouse_y >= 154:
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                if self.col1_id == 0:
                    self.col1_id = 11
                else:
                    self.col1_id -= 1
            if pyxel.btnp(pyxel.MOUSE_BUTTON_RIGHT):
                if self.col1_id == 11:
                    self.col1_id = 0
                else:
                    self.col1_id += 1

        ##############################################################
        # permet de changer la couleur du joueur 2 à l'aide:
        # de 'GAUCHE' ou 'DROITE', ou d'un clique gauche ou droit sur le joueur 2

        if pyxel.btnp(pyxel.KEY_RIGHT):
            if self.col2_id == 10:
                self.col2_id = 0
            else: self.col2_id += 1
        elif pyxel.btnp(pyxel.KEY_LEFT):
            if self.col2_id == 0:
                self.col2_id = 10
            else: self.col2_id -= 1
        #vérification de la position de la souris sur le joueur 2
        elif 174 <= pyxel.mouse_x <= 186 and 166 >= pyxel.mouse_y >= 154:
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                if self.col2_id == 0:
                    self.col2_id = 11
                else:
                    self.col2_id -= 1
            if pyxel.btnp(pyxel.MOUSE_BUTTON_RIGHT):
                if self.col2_id == 11:
                    self.col2_id = 0
                else:
                    self.col2_id += 1

    def draw(self):
        pyxel.mouse(True)
        pyxel.cls(0)
        pyxel.text(5,6,"HaxBoule",7)
        pyxel.circ(124,160,6,self.colors[self.col1_id])
        pyxel.circ(180, 160, 6, self.colors[self.col2_id])


class Jeu:
    def __init__(self, col1, col2):
        # associe à chaque couleur son nom
        self.color_name = {1:'Bleu foncé',2:'Magenta',4:'Sang',5:'Bleu',8:'Rouge',9:'Orange',
                           10:'Jaune',12:'Bleu ciel',13:'Gris',14:'Rose',15:'Beige'}
        self.j1 = Joueur1(0, col1, self.color_name[col1])
        self.j2 = Joueur2(0, col2, self.color_name[col2])
        pyxel.run(self.update, self.draw)

    def update(self):
        self.j1.update()
        self.j2.update()

        if pyxel.btnp(pyxel.KEY_P):
            pass # futur menu pause
        #la combinaison de touche R + O fait revenir au menu directement
        elif pyxel.btnp(pyxel.KEY_R):
            if pyxel.btnp(pyxel.KEY_O):
                Menu()

    def draw(self):
        pyxel.mouse(False)
        pyxel.cls(11)
        self.j1.draw()
        self.j2.draw()


class Joueur1:
    def __init__(self, team, color, name):
        self.team = team
        self.x = 10
        self.y = 10
        self.size = 6
        self.points = 0
        self.speed = 2
        self.color = color
        self.name = name

    def update(self):
        # permet le déplacement du joueur par rapport à la vitesse
        if pyxel.btn(pyxel.KEY_Z):
            self.y = self.y - self.speed
        if pyxel.btn(pyxel.KEY_S):
            self.y = self.y + self.speed
        if pyxel.btn(pyxel.KEY_Q):
            self.x = self.x - self.speed
        if pyxel.btn(pyxel.KEY_D):
            self.x = self.x + self.speed

    def draw(self):
        pyxel.circ(self.x, self.y, self.size, self.color)


class Joueur2:
    def __init__(self, team, color, name):
        self.team = team
        self.x = 120
        self.y = 120
        self.size = 6
        self.points = 0
        self.speed = 2
        self.color = color
        self.name = name

    def update(self):
        # permet le déplacement du joueur par rapport à la vitesse
        if pyxel.btn(pyxel.KEY_UP):
            self.y = self.y - self.speed
        if pyxel.btn(pyxel.KEY_DOWN):
            self.y = self.y + self.speed
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x = self.x - self.speed
        if pyxel.btn(pyxel.KEY_RIGHT):
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
        # appel de la classe Menu pour que le jeu se lance premièrement sur la fenêtre d'accueil
        Menu()

App()
