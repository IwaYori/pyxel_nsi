import pyxel
from math import sqrt
class Menu:
    def __init__(self):
        # initialisation de la liste des couleurs possibles
        self.colors = [1,2,4,5,8,9,10,12,13,14,15]
        # par défaut, joueur1 = colors[3] = 5 (bleu), joueur2 colors[4] = 8 (rouge)
        self.col1_id = 3
        self.col2_id = 4
        self.titleText_id = 6
        self.musicState = True # voir si le joueur décide d'avoir la musique ou non
        self.musicStateCol = 11 # couleur par défaut en 11 (vert)
        pyxel.playm(0,0,True)
        pyxel.run(self.update, self.draw)

    def update(self):
        self.isGameLaunched() # vérifie si le jeu doit être lancé
        self.isColorChanged() # vérifie si un des joueurs essaie de changer sa couleur

        self.isTitleClicked() # vérifie si quelqu'un clique sur le titre (easter egg)
        self.isMusicStateChanged() # vérifie si self.musicState est changé

    def col1idPlus(self):
        pyxel.play(2, 8)
        if self.col1_id == 10:
            self.col1_id = 0
        else:
            self.col1_id += 1
    def col2idPlus(self):
        pyxel.play(2, 8)
        if self.col2_id == 10:
            self.col2_id = 0
        else:
            self.col2_id += 1
    def col1idMinus(self):
        pyxel.play(2, 9)
        if self.col1_id == 0:
            self.col1_id = 10
        else:
            self.col1_id -= 1
    def col2idMinus(self):
        pyxel.play(2, 9)
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
                pyxel.play(2, 7)
                if self.titleText_id == 10:
                    self.titleText_id = 0
                else:
                    self.titleText_id += 1
    def isMusicStateChanged(self):
        if 2 <= pyxel.mouse_x <= 13 and 8 >= pyxel.mouse_y >= 2:
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                if self.musicState:
                    self.musicState = False # on change l'état de la variable
                    self.musicStateCol = 4 # on change la couleur du bouton
                    pyxel.stop(0)
                    pyxel.stop(1)
                    pyxel.stop(3)
                    pyxel.play(2,7)
                else:
                    self.musicState = True # on change l'état de la variable
                    self.musicStateCol = 11 # on change la couleur du bouton
                    pyxel.playm(0,0,True)
                    pyxel.play(2, 7)


    def draw(self):
        pyxel.mouse(True) # affiche la souris sur la fenêtre
        pyxel.cls(0)

        pyxel.text(117, 144, "Q  D", 7)
        pyxel.text(173, 144, "<  >", 7)
        pyxel.circ(124,160,6,self.colors[self.col1_id])
        pyxel.circ(180, 160, 6, self.colors[self.col2_id])
        pyxel.text(108, 130, "Choisissez votre couleur",9)

        pyxel.rectb(130, 12, 52, 18,8)
        pyxel.text(140, 18, "OctoBall", self.colors[self.titleText_id])
        pyxel.text(138, 44, "P : Pause", 11)
        pyxel.text(126, 54, "Espace : Lancer", 2)
        pyxel.text(2, 2, "Son", self.musicStateCol)

        pyxel.text(2,173, "Roan / Loris", 13)
        pyxel.text(303, 173, "2024",13)


class Jeu:
    def __init__(self, col1, col2):
        # associe à chaque couleur son nom
        self.color_name = {1:'Bleu foncé',2:'Magenta',4:'Sang',5:'Bleu',8:'Rouge',9:'Orange',
                           10:'Jaune',12:'Bleu ciel',13:'Gris',14:'Rose',15:'Beige'}
        self.j1 = Joueur1(0, col1, self.color_name[col1])
        self.j2 = Joueur2(0, col2, self.color_name[col2])
        self.balle = Balle()
        self.pauseState = False # état du menu pause
        self.pauseMusicStateCol = 11 # couleur du texte 'son' dans le menu pause
        self.pauseMusicState = True
        pyxel.run(self.update, self.draw)

    def update(self):
        if not self.pauseState:
            self.j1.update(self.j2)
            self.j2.update()

        self.isPausedButtonPressed()
        self.isMenuButtonPressed() #la combinaison de touche R + O fait revenir au menu directement
        self.isMusicStateChanged()

    def isPausedButtonPressed(self): # pas fini, à ne pas implementer dans update
        if pyxel.btnp(pyxel.KEY_P):
            pyxel.play(2,13)
            if not self.pauseState: # vérifie si le jeu est en pause
                self.pauseState = True
            else: self.pauseState = False
    def isMenuButtonPressed(self):
        if pyxel.btnp(pyxel.KEY_R):
            if pyxel.btnp(pyxel.KEY_O):
                pyxel.play(2,6)
                Menu()
    def isMusicStateChanged(self):
        if self.pauseState:
            if 2 <= pyxel.mouse_x <= 13 and 8 >= pyxel.mouse_y >= 2:
                if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                    if self.pauseMusicState:
                        self.pauseMusicState = False # on change l'état de la variable
                        self.pauseMusicStateCol = 4 # on change la couleur du bouton
                        pyxel.stop(0)
                        pyxel.stop(1)
                        pyxel.stop(3)
                        pyxel.play(2,7)
                    else:
                        self.pauseMusicState = True # on change l'état de la variable
                        self.pauseMusicStateCol = 11 # on change la couleur du bouton
                        pyxel.playm(0,0,True)
                        pyxel.play(2, 7)

    def draw(self):
        pyxel.mouse(False)
        pyxel.cls(11)
        self.j1.draw()
        self.j2.draw()
        self.balle.draw()

        if self.pauseState:
            pyxel.mouse(True)
            pyxel.rect(0,0,320,180,0)
            pyxel.text(124,34,'Jeu mis en pause',5)
            pyxel.text(100, 54, 'Appuyez sur P pour reprendre', 7)
            pyxel.text(2, 2, "Son", self.pauseMusicStateCol)


class Joueur1:
    def __init__(self, team, color, name):
        self.team = team
        self.x = 130
        self.y = 90
        self.size = 6
        self.points = 0
        self.speed = 2
        self.color = color
        self.name = name
        self.coHaut = (self.x+self.size/2,self.y-self.size) # coordonnées du point le plus en haut      )
        self.coBas = (self.x+self.size/2,self.y) # coordonnées du point le plus en bas                  ) fonctionne
        self.coGauche = (self.x, self.y+self.size/2) # coordonnées du point le plus à gauche            ) pas
        self.coDroite = (self.x+self.size, self.y+self.size/2) # coordonnées du point le plus à droite  )
        self.emplacementj2 = [False, False, False, False] # 0Bas 1Haut 2Gauche 3Droite si le joueur 2 est au dessus du j1 etc...

    def update(self,j2):
        collision=self.isCollisionJoueur(j2)

        if pyxel.btn(pyxel.KEY_Z):
            if not collision and not self.emplacementj2[1]:
                self.y = self.y - self.speed
        if pyxel.btn(pyxel.KEY_S):
            if not collision and not self.emplacementj2[0]:
                self.y = self.y + self.speed
        if pyxel.btn(pyxel.KEY_Q):
            self.x = self.x - self.speed
        if pyxel.btn(pyxel.KEY_D):
            self.x = self.x + self.speed

    def draw(self):
        pyxel.circ(self.x, self.y, self.size, self.color)

    def isCollisionJoueur(self,j2):
        """Renvoie True si il y a une collision entre les deux joueurs"""
        distance=sqrt((self.x-j2.x)**2+(self.y-j2.y)**2)
        return distance<=self.size*2

    def emplacementJ2(self,j2):
        if j2.x>self.x:
            self.emplacementj2[3]=True
            self.emplacementj2[2]=False
        else:
            self.emplacementj2[2]=True
            self.emplacementj2[3]=False

        if j2.y>self.y:
            self.emplacementj2[0]=True
            self.emplacementj2[1]=False

        else:
            self.emplacementj2[1]=True
            self.emplacementj2[0]=False

class Joueur2:
    def __init__(self, team, color, name):
        self.team = team
        self.x = 190
        self.y = 90
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

class Balle:
    def __init__(self):
        self.size = 4
        self.color = 7 # blanc
        self.x = 160
        self.y = 90
        self.speed = 2

    def draw(self):
        pyxel.circ(self.x,self.y,self.size,self.color)


##############################################################


class App:
    """classe mère qui lance la fenêtre"""
    def __init__(self):
        pyxel.init(320, 180, title='Octoball')
        pyxel.load('PYXEL_RESOURCE_FILE.pyxres')
        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        # appel de la classe Menu pour que le jeu se lance premièrement sur la fenêtre d'accueil
        Menu()

App()