import math
import pyxel

class Menu:
    def __init__(self):
        # initialisation de la liste des couleurs possibles
        self.colors = [1,2,4,5,8,9,10,12,14,15]
        # par défaut, joueur1 = colors[3] = 5 (bleu), joueur2 colors[4] = 8 (rouge)
        self.col1_id = 3
        self.col2_id = 4
        self.titleText_id = 6

        self.playerNumber = 2 # de base, le jeu contient 2 joueurs (1vs1)

        self.t1Name = None
        self.t2Name = None
        self.scores = [1,2,3,4,5,6] # liste des limites de score
        self.scoreLimitId = 2 # id qui correspond à 3 dans la liste au dessus

        self.musicState = True # voir si le joueur décide d'avoir la musique ou non
        self.musicStateCol = 11 # couleur par défaut en 11 (vert)

        pyxel.playm(0,0,True)
        pyxel.run(self.update, self.draw)

    def update(self):
        self.isGameLaunched() # vérifie si le jeu doit être lancé
        self.isColorChanged() # vérifie si un des joueurs essaie de changer sa couleur
        self.isTitleClicked() # vérifie si quelqu'un clique sur le titre (easter egg)
        self.isMusicStateChanged() # vérifie si self.musicState est changé
        self.isNameChanged() # vérifie si le nom d'une équipe est changé
        self.isPlayerNumberChanged() # vérifie si le nb de joueurs est changé
        self.isScoreLimitChanged() # vérifie si le score limite est changé

    # impossibilité de réduire ces 4 fonctions en une même si ceci paraît évident
    def col1idPlus(self):
        pyxel.play(2, 8)
        if self.col1_id == 9: # 9 = dernière indice
            self.col1_id = 0
        else:
            self.col1_id += 1
    def col2idPlus(self):
        pyxel.play(2, 8)
        if self.col2_id == 9: # 9 = dernière indice
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
                # lance le jeu avec comme paramètre les deux couleurs, les noms d'équipe, le score limite et le nombre de joueurs
                Jeu(self.colors[self.col1_id], self.colors[self.col2_id], self.t1Name, self.t2Name, self.scores[self.scoreLimitId], self.playerNumber)
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
    def isNameChanged(self):
        if 90 <= pyxel.mouse_x <= 150 and 120 >= pyxel.mouse_y >= 114:
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                self.t1Name = input("Choisissez le nom de l'équipe 1 :")

        if 170 <= pyxel.mouse_x <= 210 and 120 >= pyxel.mouse_y >= 114:
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                self.t2Name = input("Choisissez le nom de l'équipe 2 :")
    def isPlayerNumberChanged(self):
        if pyxel.btnp(pyxel.KEY_V):
            if self.playerNumber == 2:
                self.playerNumber = 4
            else: self.playerNumber = 2
            pyxel.play(2,8)
    def isScoreLimitChanged(self):
        if pyxel.btnp(pyxel.KEY_UP):
            if self.scoreLimitId == len(self.scores)-1: # si l'id est le dernier de la liste
                 pyxel.play(2, 4) # cela n'augmente pas plus
            else:
                self.scoreLimitId += 1 # sinon il s'incrémente
                pyxel.play(2, 9)

        if pyxel.btnp(pyxel.KEY_DOWN):
            if self.scoreLimitId == 0: # si l'id est le premier de la liste
                pyxel.play(2, 4) # cela ne descend pas plus
            else :
                self.scoreLimitId -= 1 # sinon il se décrémente
                pyxel.play(2, 9)


    def draw(self):
        pyxel.mouse(True) # affiche la souris sur la fenêtre
        pyxel.cls(0)

        pyxel.text(117, 144, "Q  D", 7)
        pyxel.text(173, 144, "<  >", 7)
        pyxel.circ(124,160,6,self.colors[self.col1_id])
        pyxel.circ(180, 160, 6, self.colors[self.col2_id])
        pyxel.text(108, 130, "Choisissez votre couleur",9)

        pyxel.rectb(130, 12, 52, 18,8) # cadre autour du titre
        pyxel.text(140, 18, "OctoBall", self.colors[self.titleText_id])
        pyxel.text(138, 44, "P : Pause", 11)
        pyxel.text(126, 54, "Espace : Lancer", 2)
        pyxel.text(100, 64, "V : Changer le nb de joueurs", 12)
        pyxel.text(112, 84, f"Nombre de joueurs : {self.playerNumber}", 10)
        pyxel.text(90, 114, 'Changer nom T1',3)
        pyxel.text(166, 114, 'Changer nom T2',3)
        pyxel.text(2, 2, "Son", self.musicStateCol)

        pyxel.text(280, 4, "UP", 7)
        pyxel.text(250, 14, f"Limite score : {self.scores[self.scoreLimitId]}", 10)
        pyxel.text(276, 24, "DOWN", 7)

        pyxel.text(2,173, "Roan / Loris", 13)
        pyxel.text(303, 173, "2024",13)


class Jeu:
    def __init__(self, col1, col2, t1Name, t2Name, scoreLimit, playerNumber):
        self.scoreLimit = scoreLimit
        self.playerNumber = playerNumber

        self.t1Name = t1Name
        self.t2Name = t2Name
        self.color_name = {1:'Bleu foncé',2:'Magenta',4:'Sang',5:'Bleu',8:'Rouge',9:'Orange',
                           10:'Jaune',12:'Bleu ciel',14:'Rose',15:'Beige'} # associe à chaque couleur son nom
        if self.t1Name == None:
            self.t1Name = self.color_name[col1] # si le nom de t1 est vide, il prend le nom de la couleur
        if self.t2Name == None:
            self.t2Name = self.color_name[col2] # si le nom de t2 est vide, il prend le nom de la couleur

        self.team1 = Team(self.t1Name,col1)
        self.team2 = Team(self.t2Name,col2)

        self.j1 = Joueur1(col1, self.team1.name, self.team1)
        self.j2 = Joueur2(col2, self.team2.name, self.team2)

        if self.playerNumber == 4:
            pass # rajouter les 2 autres joueurs

        self.balle = Balle()

        self.pauseState = False # état du menu pause
        self.pauseMusicStateCol = 11 # couleur du texte 'son' dans le menu pause
        self.pauseMusicState = True
        self.winStateCol = 11 # couleur de celui qui gagne, 11 (couleur terrain) si égalité
        self.winState = False

        pyxel.run(self.update, self.draw)

    def update(self):
        if not self.pauseState and self.winState == 0: # vérifie si le jeu n'est pas en pause et que personne n'a gagné
            self.j1.update(self.j2,self.balle)
            self.j2.update()
            self.balle.update()

            if self.balle.x-self.balle.size<=0 and self.balle.y>=pyxel.height/3 and self.balle.y<= 2*(pyxel.height/3): #Si but à gauche
                self.team2.addPoints()
                self.balle.x=pyxel.width/2
                self.balle.y=pyxel.height/2
                self.balle.vitesse_x,self.balle.vitesse_y=0,0

            if self.balle.x+self.balle.size>=pyxel.width and self.balle.y>=pyxel.height/3 and self.balle.y<= 2*(pyxel.height/3): #Si but à droite
                self.team1.addPoints()
                self.balle.x=pyxel.width/2
                self.balle.y=pyxel.height/2
                self.balle.vitesse_x, self.balle.vitesse_y = 0, 0


        self.isPausedButtonPressed()
        self.isMenuButtonPressed() #la combinaison de touche R + O fait revenir au menu directement
        self.isMusicStateChanged()
        self.defineWinStateColor()
        self.isBallReset()
        self.winStateCheck()

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
    def defineWinStateColor(self):
        if self.team1.points > self.team2.points:
            self.winStateCol = self.team1.color
        elif self.team1.points < self.team2.points:
            self.winStateCol = self.team2.color
        else: self.winStateCol = 13
    def isBallReset(self): # en cas de soucis, combinaison de MAJ + TAB pour remettre la balle au centre
        if pyxel.btnp(pyxel.KEY_SHIFT):
            if pyxel.btnp(pyxel.KEY_TAB):
                pyxel.play(2, 6)
                self.balle.x = 160
                self.balle.y = 80
                self.balle.vitesse_x = 0
                self.balle.vitesse_y
    def winStateCheck(self):
        if not self.winState:
            if self.team1.points == self.scoreLimit:
                self.winState = self.team1.name
            elif self.team2.points == self.scoreLimit:
                self.winState = self.team2.name

    def draw(self):
        pyxel.mouse(False)
        pyxel.cls(11)
        self.j1.draw()
        self.j2.draw()
        self.balle.draw()
        pyxel.line(pyxel.width / 2, 0, pyxel.width / 2, pyxel.height, 7)
        pyxel.circb(pyxel.width/2,pyxel.height/2,20,7)
        pyxel.text(pyxel.width/2-9,pyxel.height/2-80,str(self.team1.points) +' - '+str(self.team2.points),0)

        pyxel.rectb(0,0,320,180, self.winStateCol) #bordure

        pyxel.rectb(0,pyxel.height/3,20,pyxel.height/3,7) #Cage gauche
        pyxel.rectb(pyxel.width-20, pyxel.height / 3, 20, pyxel.height / 3, 7) #Cage droite





        if self.pauseState:
            pyxel.mouse(True) # affiche la souris
            pyxel.rect(0,0,320,180,0)
            pyxel.text(124,34,'Jeu mis en pause',5)
            pyxel.text(100, 54, 'Appuyez sur P pour reprendre', 7)
            pyxel.text(2, 2, "Son", self.pauseMusicStateCol)

        if self.winState != 0:
            pyxel.stop(0)
            pyxel.stop(1)
            pyxel.stop(3)
            pyxel.text(124, 76, f'Victoire de {self.winState}') # self.winState aura comme valeur l'équipe gagnante (str)
            pyxel.text(98,86, 'R+O pour revenir au menu principal')



class Joueur1:
    def __init__(self, color, name, team):
        self.name = name
        self.team = team
        self.x = 10
        self.y = 20
        self.size = 6
        self.speed = 3

        self.points = self.team.points
        self.color = color
        self.collision = False

    def update(self, j2, balle):
        self.collisionBalle(balle)
        self.isCollisionJoueur(j2)

        if self.speed < 2:
            self.speed*=1.2  # permet au joueur de retrouver sa vitesse initial post contact avec la balle
        elif self.speed > 2:
            self.speed = 2

        if pyxel.btn(pyxel.KEY_Z):
            if self.y > 0+self.size:
                self.y = self.y - self.speed + 0.2
        if pyxel.btn(pyxel.KEY_S):
            if self.y < 180 - self.size:
                self.y = self.y + self.speed - 0.2
        if pyxel.btn(pyxel.KEY_Q):
            if self.x > 0 + self.size:
                self.x = self.x - self.speed
        if pyxel.btn(pyxel.KEY_D):
            if self.x < 320 - self.size:
                self.x = self.x + self.speed

    def draw(self):
        pyxel.circ(self.x, self.y, self.size, self.color)
        if self.collision: # test uniquement mis dans la classe Joueur 1 car si le j1 est en collision avec le j2, le j2 est
            pyxel.dither(0.5) # en collision avec le j1, inutile de recopier cette partie dans l'autre classe
        else: pyxel.dither(1) # dither change l'opacité des sprites affichés (hors le fond)

    def isCollisionJoueur(self,j2):
        """Renvoie True si il y a une collision entre les deux joueurs"""
        distance=math.sqrt((self.x-j2.x)**2+(self.y-j2.y)**2)
        if distance<=self.size*2:
            self.collision = True
        else: self.collision = False

    def collisionBalle(self,balle):
        distanceBalle = math.sqrt((self.x - balle.x)**2 + (self.y - balle.y)**2)

        if distanceBalle <= self.size + balle.size + 2: #Distance j1 + balle
            balle.angle = math.atan2(balle.y - self.y, balle.x - self.x)

            #balle.angle += math.pi
            balle.vitesse_x = math.cos(balle.angle) + 0.3
            balle.vitesse_y = math.sin(balle.angle) + 0.3
            self.speed = 0.82 # ralentit le joueur au contact





class Joueur2:
    def __init__(self, color, name, team):
        self.name = name
        self.team = team
        self.x = 60
        self.y = 30
        self.size = 6
        self.speed = 2

        self.points = self.team.points
        self.color = color
        self.emplacementj1 = [False, False, False,False]  # 0Bas 1Haut 2Gauche 3Droite si le joueur 2 est au dessus du j1 etc...

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
        self.x = 90
        self.y = 90
        self.angle=0
        self.vitesse_x = -3
        self.vitesse_y= 0

    def update(self):

        self.x = self.x + self.vitesse_x
        self.y = self.y - self.vitesse_y

        if self.x - self.size <= 0 or self.x + self.size >= pyxel.width: #Vérifier contact avec les bords
            self.vitesse_x *= -1
        if self.y - self.size <= 0 or self.y + self.size >= pyxel.height:
            self.vitesse_y *= -1


        self.vitesse_x*=0.989 #Ralentir la balle
        self.vitesse_y*=0.989

    def draw(self):
        pyxel.circ(self.x,self.y,self.size,self.color)


class Team:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.points = 0

    def addPoints(self):
        self.points += 1


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