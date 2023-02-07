#permettent d'interagir et d'obtenir des informations sur le système d'exploitation
import os
#développement d'applications multimédias "jeux"
import pygame 
# import the system module
import sys
# import the time module
import time


#1 er classe (gameboard)
class Classe1:
    EMPTY_BOX = 0 #cst case vide
    RED_CHIP = -1 #cst case rouge joueur 2
    YELLOW_CHIP = 1 #case jaune joueur 1
    YELLOW_WIN = 4 #ganger joueur 1
    RED_WIN = -4 #ganger joueur 2

    def __init__(self):
        self.board = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]
        ]

    def winning_mover_horizontale(self):
        # initialisation des variables
        # conserver le winner, vide si pas de winner
        winner = ""
        # variable utilisee pour la boucle while
        line = 5
        # variable qui sert a arret si on trouve le winner
        stop = False
        # raisonnement similaire, plus performant qu'un parcours traditionnel
        # on boucle tant qu'on n'a pas atteint (la line) 0 et que l'on a pas de winner
        # le while nous permet de nous deplacer dans les lines de bas en haut (line 5 --> line 0)
        while line >= 0 and stop == False:
            for column in range(4):  # ca nous permet deplacer dans les columns
                # pourquoi 4 ? 4 possibilites de gagner dans une line
                # on determine le winner en fonction des valeurs definies dans les 4 columns (que l'on decale grace a la variable column) que l'on regarde pour la line donnee i
                if self.board[line][column] + self.board[line][column + 1] + self.board[line][column + 2] + \
                        self.board[line][column + 3] == Classe1.YELLOW_WIN:  # gamer jaune gagne
                    # on affecte le winner (car on a nom nombre de points)
                    winner = "jaune"
                    print(winner)
                    # vu qu'on a gagne on arrete les parcours
                    stop = True
                if self.board[line][column] + self.board[line][column + 1] + self.board[line][column + 2] + \
                        self.board[line][column + 3] == Classe1.RED_WIN:  # gamer rouge gagne
                    winner = "rouge"
                    print(winner)
                    stop = True
            # on remonte la line
            line = line - 1
        # retourne la variable winner
        return winner

    def winning_mover_verticale(self):
        winner = ""
        # on regarde chaque column
        for column in range(7):
            # on descend les lines pour la column concernee, pour verifier s'il y a un winner
            # tant que la line est strictement superieur a 2
            # 5 YELLOW_WINNER 3 en baissant de -1 (3eme parametre du for)
            # c'est plus concis que ce qu'on a au-dessous
            for line in range(5, 2, -1):
                if self.board[line][column] + self.board[line - 1][column] + self.board[line - 2][column] + \
                        self.board[line - 3][column] == Classe1.YELLOW_WIN:
                    winner = "jaune"
                if self.board[line][column] + self.board[line - 1][column] + self.board[line - 2][column] + \
                        self.board[line - 3][column] == Classe1.RED_WIN:
                    winner = "rouge"
        return winner

    def winning_mov_diagonale(self):
        winner = ""
        # on va diagonale d'en haut a gauche vers en bas a droite
        # on avance dans les lines
        for line in range(3):
            # on avance dans les columns
            for column in range(4):
                # vu que c'est en meme on avance en diagonale
                if self.board[line][column] + self.board[line + 1][column + 1] + self.board[line + 2][column + 2] + \
                        self.board[line + 3][column + 3] == Classe1.YELLOW_WIN:
                    winner = "jaune"
                if self.board[line][column] + self.board[line + 1][column + 1] + self.board[line + 2][column + 2] + \
                        self.board[line + 3][column + 3] == Classe1.RED_WIN:
                    winner = "rouge"
        # on va diagonale d'en haut a droite vers en bas a gauche
        for line in range(3):
            # 0 1 2 3, la line a laquelle on commence
            for column in range(3, 7):
                # 3 4 5 6, on commence a la column 3 pour aller vers la 6
                if self.board[line][column] + self.board[line + 1][column - 1] + self.board[line + 2][column - 2] + \
                        self.board[line + 3][column - 3] == Classe1.YELLOW_WIN:
                    winner = "jaune"
                if self.board[line][column] + self.board[line + 1][column - 1] + self.board[line + 2][column - 2] + \
                        self.board[line + 3][column - 3] == Classe1.RED_WIN:
                    winner = "rouge"
        return winner
    #teste gamer gagner
    def get_winner(self):
        # on verifie q'il winner d'abord horizontalement
        gamer = self.winning_mover_horizontale()
        # s'il y a un winner, je n'ai pas besoin de verifier les autres cas
        # s'il n'y pas de winner je vais pas sur le return donc je peux continuer les autres etapes de la verification
        if gamer != "":
            return gamer
        gamer = self.winning_mover_verticale()
        if gamer != "":
            return gamer
        gamer = self.winning_mov_diagonale()
        if gamer != "":
            return gamer
            
    #comment placer une piece
    def put_chip(self, column, gamer):
        # boucle sur les lines de bas en haut
        line = 5  # par le bas 5 4 3 2 1 0
        
        # False je continue, true j'arrete
        stop = False
        while line >= 0 and stop == False:
            # si j'ai une case vide pour la column concernee
            if self.board[line][column] == Classe1.EMPTY_BOX:
                if gamer == Classe1.YELLOW_CHIP:
                    # je mets mon pion jaune
                    self.board[line][column] = Classe1.YELLOW_CHIP
                    # vu que je viens de placer mon pion, je ne vais pas en placer d'autres.
                    stop = True
                else:
                    self.board[line][column] = Classe1.RED_CHIP
                    stop = True
            # je remonte de bas en haut avec column fixee dans board
            line = line - 1  # faire le parcours de bas en haut, parce que c'est plus performant (condition arret atteinte plus tot)

    # Methode purement technique d'aide a la representation
    def reverse_game_board(self):
        # par exemple la ligne d'en bas se retrouve en haut
        reversed_game_board = []
        for row in range(5, -1, -1):
            reversed_game_board.append(self.board[row])
        return reversed_game_board

    def display(self):
        print("\n")
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                print(self.board[i][j], end=' ')
            print()
        print("\n")



# 2 eme classe(gameview)
class Classe2(Classe1):
    IMAGE_DIRECTORY = "images"
#constructeur
    def __init__(self):
        self.gamer = 1 #un joueur courant
        self.gameBoard = Classe1()
        self.pyGame = pygame 

        # initialiser l'interface
        # utiliser la librairie pygame
        pygame.init()

        # charger l'image du plateau de jeu
        self.board_picture = pygame.image.load(os.path.join(Classe2.IMAGE_DIRECTORY, "plateau.png"))

        # obtenir la taille du plateau de jeu
        taille_plateau_de_jeu = self.board_picture.get_size()
        # stocker cette taille
        self.size = (taille_plateau_de_jeu[0] * 1, taille_plateau_de_jeu[1])
        # setter la taille de la fenetre jeu au meme d'imension que celle du plateau de jeu (image)
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("My Game")
        self.screen.blit(self.board_picture, (0, 0))
        pygame.display.flip()

        # charger l'image du pion jaune
        self.yellowChip = pygame.image.load(os.path.join(Classe2.IMAGE_DIRECTORY, "pion_jaune.png"))
        # charger l'image du pion rouge
        self.redChip = pygame.image.load(os.path.join(Classe2.IMAGE_DIRECTORY, "pion_rouge.png"))
        # Police pour le jeu
        self.font = pygame.font.Font("freesansbold.ttf", 15)

# Cette fonction retourne la colonne demandee au joueur1
    def determine_column(self, x):
        
        # Tant que la valeur n'est pas acceptable, on demande la colonne a jouer

        column = x - 16
        column = column / 97 #pour avoir votre place dans le board
        if column in range(0, 7):
            if self.gameBoard.board[5][int(column)] == 0:
                game_board_state = False
        return int(column)

# Cette fonction d'affichage notre modele "matrice" 
    def render(self):
        # On nettoye l'ecran de jeu
        self.screen.fill((0, 0, 0))
        # On remet l'image en commencant a la base de l'affichage
        self.screen.blit(self.board_picture, (0, 0))

        # on inverse la gameBoard (backend) pour faciliter les traitements qui suivent
        game_board_game_state = self.gameBoard.reverse_game_board()

        # Affichage de debugging
        self.gameBoard.display()

        # parcours en ordre normal
        for i in range(len(game_board_game_state)):
            for j in range(len(game_board_game_state[i])):
                # cas du joueur jaune
                if game_board_game_state[i][j] == Classe1.YELLOW_CHIP:
                    # on place une image d'un pion jaune sur l'écran en fonction de la colonne ou l'on se situe
                    self.screen.blit(self.yellowChip, (16 + 97 * j, 13 - 97.5 * i + 486))
                pygame.display.flip()
                # cas du joueur rouge
                if game_board_game_state[i][j] == Classe1.RED_CHIP:
                    # on place une image d'un pion rouge sur l'écran en fonction de la colonne ou l'on se situe
                    self.screen.blit(self.redChip, (16 + 97 * j, 13 - 97.5 * i + 486))
                pygame.display.flip()

# 3 éme classe(game)
class Classe3(Classe2):
    NUMBER_OF_CHIPS = 42  #nbr maximum de jeton

    def __init__(self):
        self.gamer = 1 #un joueur courant
        self.playedChips = 0 #nbr de jeton  qui jouer
        self.potentialWinner = False #test gagner ou pas 
        self.gameView = Classe2() #modele de jeux
     
        # Cette fonction retourne le numero du joueur qui doit jouer
    def get_gamer(self):
        if self.playedChips % 2 == 0:
            gamer_id = Classe1.YELLOW_CHIP
        else:
            gamer_id = Classe1.RED_CHIP
        return gamer_id
    # Cette fonction retourne le joueur gagner
    def display_winner(self):
        if self.gamer == "" or self.gamer is None:
            return "personne n'a gagne"
        else:
            return self.gamer + " a gagne"
     # Cette fonction retourne le joueur start
    def start(self):
        while self.potentialWinner != "jaune" \
                and self.potentialWinner != "rouge" \
                and self.playedChips < Classe3.NUMBER_OF_CHIPS:
            time.sleep(0.05)
            # Le joueur joue
            for event in self.gameView.pyGame.event.get():

                self.gameView.gameBoard.display()

                if event.type == self.gameView.pyGame.MOUSEBUTTONUP:
                    x, y = self.gameView.pyGame.mouse.get_pos()
                    gamer = self.get_gamer()
                    column = self.gameView.determine_column(x)
                    # On modifie les variables pour tenir compte du jeton depose.
                    self.gameView.gameBoard.put_chip(column, gamer)
                    self.playedChips = self.playedChips + 1
                    self.potentialWinner = self.gameView.gameBoard.get_winner()
                    print("GAGNANT ? : " + str(self.potentialWinner))
                    self.gameView.render()
                    self.gameView.pyGame.display.flip()

                if event.type == self.gameView.pyGame.QUIT:
                    sys.exit(0)

