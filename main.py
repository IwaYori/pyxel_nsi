import pyxel

class Menu:
    def __init__(self):
        # initialisation de la liste des couleurs possibles
        self.colors = [1,2,4,5,8,9,10,12,13,14,15]
        # par défaut, joueur1 = colors[3] = 5 (bleu), joueur2 colors[4] = 8 (rouge)
        self.col1_id = 3
        self.col2_id = 4
        self.titleText_id = 6
        pyxel.playm(0,0,True)
        pyxel.run(self.update, self.draw)

    def update(self):
        self.isGameLaunched() # vérifie si le jeu doit être lancé
        self.isColorChanged() # vérifie si un des joueurs essaie de changer sa couleur

        self.isTitleClicked() # vérifie si quelqu'un clique sur le titre (easter egg)

    def col1idPlus(self):
        if self.col1_id == 10:
            self.col1_id = 0
        else:
            self.col1_id += 1
    def col2idPlus(self):
        if self.col2_id == 10:
            self.col2_id = 0
        else:
            self.col2_id += 1
    def col1idMinus(self):
        if self.col1_id == 0:
            self.col1_id = 10
        else:
            self.col1_id -= 1
    def col2idMinus(self):
        if self.col2_id == 0:
            self.col2_id = 10
        else:
            self.col2_id -= 1

    def isColorChanged(self):
        # permet de changer la couleur du joueur 1 à l'aide:
        # de 'Q' ou 'D', ou d'un clique gauche ou droit sur le joueur 1
        if pyxel.btnp(pyxel.KEY_D):
            # pour éviter un dépassement d'indice:
            self.col1idPlus()
        elif pyxel.btnp(pyxel.KEY_Q):
            # pour éviter un dépassement d'indice:
            self.col1idMinus()
        # vérification de la position de la souris sur le joueur 1
        elif 118 <= pyxel.mouse_x <= 130 and 166 >= pyxel.mouse_y >= 154:
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                self.col1idMinus()
            if pyxel.btnp(pyxel.MOUSE_BUTTON_RIGHT):
                self.col1idPlus()

        ##############################################################
        # permet de changer la couleur du joueur 2 à l'aide:
        # de 'GAUCHE' ou 'DROITE', ou d'un clique gauche ou droit sur le joueur 2

        if pyxel.btnp(pyxel.KEY_RIGHT):
            self.col2idPlus()
        elif pyxel.btnp(pyxel.KEY_LEFT):
            self.col2idMinus()
        # vérification de la position de la souris sur le joueur 2
        elif 174 <= pyxel.mouse_x <= 186 and 166 >= pyxel.mouse_y >= 154:
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                self.col2idMinus()
            if pyxel.btnp(pyxel.MOUSE_BUTTON_RIGHT):
                self.col2idPlus()

    def isGameLaunched(self):
        # espace est la touche qui permet de lancer le jeu
        if pyxel.btn(pyxel.KEY_SPACE):
            # empêche de lancer le jeu si deux joueurs ont la même couleur et joue un son
            if self.col1_id == self.col2_id:
                pyxel.play(2, 4)
            else:
                pyxel.play(2,6)
                # lance le jeu avec comme paramètre les deux couleurs
                Jeu(self.colors[self.col1_id], self.colors[self.col2_id])
    def isTitleClicked(self): # easter egg
        if 142 <= pyxel.mouse_x <= 168 and 23 >= pyxel.mouse_y >= 18:
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                if self.titleText_id == 10:
                    self.titleText_id = 0
                else:
                    self.titleText_id += 1


    def draw(self):
        pyxel.mouse(True) # affiche la souris sur la fenêtre
        pyxel.cls(0)

        pyxel.circ(124,160,6,self.colors[self.col1_id])
        pyxel.circ(180, 160, 6, self.colors[self.col2_id])

        pyxel.text(142, 18, "HaxBall", self.colors[self.titleText_id])

        pyxel.text(2,173, "Roan / Loris", 13)
        pyxel.text(303, 173, "2024",13)


class Jeu:
    def __init__(self, col1, col2):
        # associe à chaque couleur son nom
        self.color_name = {1:'Bleu foncé',2:'Magenta',4:'Sang',5:'Bleu',8:'Rouge',9:'Orange',
                           10:'Jaune',12:'Bleu ciel',13:'Gris',14:'Rose',15:'Beige'}
        self.j1 = Joueur1(0, col1, self.color_name[col1])
        self.j2 = Joueur2(0, col2, self.color_name[col2])
        pyxel.run(self.update, self.draw)

    def update(self):
        self.j1.update(self.j2)
        self.j2.update()

        if pyxel.btnp(pyxel.KEY_P):
            pass # futur menu pause
        #la combinaison de touche R + O fait revenir au menu directement
        elif pyxel.btnp(pyxel.KEY_R):
            if pyxel.btnp(pyxel.KEY_O):
                pyxel.play(2,6)
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
        self.coHaut=(self.x,self.y+self.speed) #coordonnées du point le plus en haut
        self.coBas=(self.x,self.y+self.speed)
        self.collision = [False, False, False, False] #Haut Bas Gauche Droite

    def update(self,j2):
        self.isCollision(j2) #on update pour voir si il ya une collision
        # permet le déplacement du joueur par rapport à la vitesse
        if pyxel.btn(pyxel.KEY_Z) and not self.collision[0]:
            self.y = self.y - self.speed
        if pyxel.btn(pyxel.KEY_S) and not self.collision[1]:
            self.y = self.y + self.speed
        if pyxel.btn(pyxel.KEY_Q) and not self.collision[2]:
            self.x = self.x - self.speed
        if pyxel.btn(pyxel.KEY_D) and not self.collision[3]:
            self.x = self.x + self.speed

    def draw(self):
        pyxel.circ(self.x, self.y, self.size, self.color)

    def isCollision(self,j2):
        #collision en haut
        self.collision[0] = self.y+self.size == j2.y-j2.size and self.x >= j2.x-j2.size and self.x <= j2.x+j2.size
        #collision en bas
        self.collision[1] = self.y-self.size == j2.y+j2.size and self.x >= j2.x-j2.size and self.x <= j2.x+j2.size

        #collision gauche
        self.collision[2] = self.x-self.size == j2.x+j2.size and self.y <= j2.y+j2.size and self.y >= j2.y-j2.size
        #collision droite
        self.collision[3] = self.x+self.size == j2.x-j2.size and self.y <= j2.y+j2.size and self.y >= j2.y-j2.size


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
        pyxel.init(320, 180, title='HaxBall remake')
        pyxel.load('PYXEL_RESOURCE_FILE.pyxres')
        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        # appel de la classe Menu pour que le jeu se lance premièrement sur la fenêtre d'accueil
        Menu()

App()
