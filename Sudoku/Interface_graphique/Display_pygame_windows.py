###########################################################################################################################################################
######################################################### Import des fonctions ############################################################################
###########################################################################################################################################################
import sys
from pathlib import Path
file = Path(__file__).resolve()
package_root_directory = file.parents[1]
sys.path.append(str(package_root_directory))

import pygame
import copy
from pygame.constants import K_BACKSLASH, K_BACKSPACE, KEYDOWN
from Data import *
from Grid.create_sudoku import create_sudoku
from Solve_sudoku.Solve_backtracking import solve_sudoku_unique
from Grid.Check_solution import is_full,check_solutions

###########################################################################################################################################################
######################################## Fonctions pour afficher l'interface graphique du jeu sur Macbook #################################################
###########################################################################################################################################################




#####################################################################################################
######################################## Constantes #################################################
#####################################################################################################


#initialisation du module pygame qui gère les polices
pygame.font.init()

#initialisation du module pygame qui gère les sons
pygame.mixer.init()

# Police que l'on va utiliser pour écrire les chiffres dans la grille
NUMBERS_FONT = pygame.font.SysFont('comicsans', 30)
COMMENTS_FONT = pygame.font.SysFont('comicsans', 11)
TIME_FONT = pygame.font.SysFont('Arial',35)
NEW_GAME_FONT=pygame.font.SysFont('comicsans', 30)
WINNER_FONT = pygame.font.SysFont('comicsans',20)
HOME_FONT = pygame.font.SysFont('comicsans',35)
HOME_LITTLE_FONT =  pygame.font.SysFont('comicsans',30)

# dimensions
WINDOW_WIDTH,WINDOW_HEIGHT = 800,450

BLOCK_SIDE = 50  # en pixels, taille d'un bloc
GRID_WIDTH, GRID_HEIGHT = 9*BLOCK_SIDE, 9 * BLOCK_SIDE  # taille de la grille de sudoku

# taille des frontières horizontales normales de la grille
H_BORDER_WIDTH, H_BORDER_HEIGHT = GRID_WIDTH, 2
# taille des frontières verticales normales de la grille
V_BORDER_WIDTH, V_BORDER_HEIGHT = H_BORDER_HEIGHT, H_BORDER_WIDTH

MAIN_H_BORDER_WIDTH, MAIN_H_BORDER_HEIGHT = GRID_WIDTH, 4
MAIN_V_BORDER_WIDTH, MAIN_V_BORDER_HEIGHT = MAIN_H_BORDER_HEIGHT, MAIN_H_BORDER_WIDTH

X_NUMBER_OFFSET = 17
Y_NUMBER_OFFSET = 2

##images
#image du bouton crayon
IMAGE_CRAYON=pygame.transform.scale(pygame.image.load("Sudoku/Data/crayon_detoure.png"),(75,52))
BUTTUN_CRAYON=IMAGE_CRAYON.get_rect()
BUTTUN_CRAYON.x,BUTTUN_CRAYON.y = 490,85
BUTTUN_CRAYON.height+=20

#image du bouton play
IMAGE_PLAY = pygame.transform.scale(pygame.image.load("Sudoku/Data/play.jpg"),(50,50))
IMAGE_PAUSE = pygame.transform.scale(pygame.image.load("Sudoku/Data/Pause.jpg"),(50,50))
BUTTON_PLAY_PAUSE = IMAGE_PLAY.get_rect()
BUTTON_PLAY_PAUSE.x , BUTTON_PLAY_PAUSE.y = 600,85

#image de l'ampoule
IMAGE_BULB = pygame.transform.scale(pygame.image.load("Sudoku/Data/Ampoule.jpg"),(75,75))
BUTTON_HINT = IMAGE_BULB.get_rect()
BUTTON_HINT.x,BUTTON_HINT.y = 700,85

#images du boutton musique
IMAGE_MUSIC_ON = pygame.transform.scale(pygame.image.load("Sudoku/Data/music_on.png"),(30,30))
IMAGE_MUSIC_OFF = pygame.transform.scale(pygame.image.load("Sudoku/Data/music_off.png"),(30,30))
BUTTON_MUSIC = IMAGE_MUSIC_ON.get_rect()
BUTTON_MUSIC.x,BUTTON_MUSIC.y = 500,30


# création de la grille principale
WINDOW = pygame.display.set_mode(
    (WINDOW_WIDTH, WINDOW_HEIGHT))  # crée la fenêtre générale
# Change le titre de la fenêtre
pygame.display.set_caption("Jeu de Sudoku fait maison !")

# couleurs :
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_GREY = (100, 100, 100)
GREY = (150, 150, 150)
LIGHT_GREY = (206, 206, 206)
BLUE = (0,0,230)
BLUE_GREY = (187,210,225)
PINK=(254,191,210)
RED = (255,0,0)

#sounds
CLICK_SOUND = pygame.mixer.Sound('Sudoku/Data/click_button_sound.mp3')
CLICK_SOUND.set_volume(0.07)


BACKGROUND_MUSIC = pygame.mixer.Sound("Sudoku/Data/background_music.mp3")
BACKGROUND_MUSIC.set_volume(0.25)

# images par secondes :
MAX_FPS = 60


########################################################################################################################################################
######################################## Fonctions qui font le dessin pur du jeu sur la fenêtre pygame #################################################
########################################################################################################################################################


def draw_grid():  # dessine la grille brute (les lignes et colonnes)
    for i in range(0, 10):
        X, Y = BLOCK_SIDE*i, BLOCK_SIDE*i
        if i % 3 == 0: #dessine les grosses lignes et colonnes
            MAIN_BORDER_X = pygame.Rect(
                X-MAIN_V_BORDER_WIDTH//2, 0, MAIN_V_BORDER_WIDTH, MAIN_V_BORDER_HEIGHT)
            pygame.draw.rect(WINDOW, BLACK, MAIN_BORDER_X)
            MAIN_BORDER_Y = pygame.Rect(
                0, Y-MAIN_H_BORDER_HEIGHT//2, MAIN_H_BORDER_WIDTH, MAIN_H_BORDER_HEIGHT)
            pygame.draw.rect(WINDOW, BLACK, MAIN_BORDER_Y)
        else: #dessine les lignes et colonnes plus petites
            BORDER_X = pygame.Rect(X-V_BORDER_WIDTH//2,
                                   0, V_BORDER_WIDTH, V_BORDER_HEIGHT)
            BORDER_Y = pygame.Rect(0, Y-H_BORDER_HEIGHT //
                                   2, H_BORDER_WIDTH, H_BORDER_HEIGHT)
            pygame.draw.rect(WINDOW, BLACK, BORDER_X)
            pygame.draw.rect(WINDOW, BLACK, BORDER_Y)


# met en valeur la case sélectionnée actuellement (en bleu), les cases ayant le même chiffre que celui de la case sélectionnée (gris), et les cases dans la même ligne, colonne et carré 
def draw_current_case_selected(grid,current_case_selected_i, current_case_selected_j):
    cases_avec_meme_chiffre = [(i,j) for i in range(9) for j in range(9) if grid[i][j]== grid[current_case_selected_i][current_case_selected_j] and grid[i][j]!=0]
    for coord in cases_avec_meme_chiffre:
        X,Y = coord[1]*BLOCK_SIDE,coord[0]*BLOCK_SIDE
        case = pygame.Rect(X, Y, BLOCK_SIDE, BLOCK_SIDE)
        pygame.draw.rect(WINDOW, GREY, case)

    
    cases_a_colorier_gris = [(i,current_case_selected_j) for i in range(9)] + [(current_case_selected_i,j) for j in range(9)]#liste de toutes les cases dans la même ligne et la même colonne que la case sélectionnée
    
    big_coord = current_case_selected_i//3,current_case_selected_j//3 
    for k in range(3):
        for l in range(3):
            cases_a_colorier_gris.append((3*big_coord[0]+k,3*big_coord[1]+l)) #on ajoute également à cette liste toutes les cases qui sont dans le même carré 3x3 que la case sélectionnée
    
    for coord in cases_a_colorier_gris:
        X,Y = coord[1]*BLOCK_SIDE,coord[0]*BLOCK_SIDE
        case = pygame.Rect(X, Y, BLOCK_SIDE, BLOCK_SIDE)
        pygame.draw.rect(WINDOW, LIGHT_GREY, case)

    X, Y = current_case_selected_j*BLOCK_SIDE, current_case_selected_i*BLOCK_SIDE
    current_case = pygame.Rect(X, Y, BLOCK_SIDE, BLOCK_SIDE)
    pygame.draw.rect(WINDOW, BLUE_GREY, current_case)


def draw_numbers(grid,original_coordinates):  # dessine les nombres de la grille sur la fenêtre: ceux de la grille initiale (contenus dans la liste original_coordinates) en noir et ceux mis par l'utilisateur en bleu.
    n = len(grid)
    for i in range(n):
        for j in range(n):
            if grid[i][j] != 0:
                X, Y = j*BLOCK_SIDE, i*BLOCK_SIDE
                if (i,j) in original_coordinates: #chiffres de la grille initiale en noir
                    number_to_draw = NUMBERS_FONT.render(str(grid[i][j]), 1, BLACK)
                    WINDOW.blit(number_to_draw,
                                (X+X_NUMBER_OFFSET, Y+Y_NUMBER_OFFSET))
                else:
                    number_to_draw = NUMBERS_FONT.render(str(grid[i][j]), 1, BLUE)   #chiffres ajoutés en bleu
                    WINDOW.blit(number_to_draw,
                                (X+X_NUMBER_OFFSET, Y+Y_NUMBER_OFFSET))


def draw_comments(comments_grid): #dessine les notes (contenus dans la liste de liste(=grille) de set() comments_grid) en petit et gris dans les cases 
    offset_comments={1:(7,1),2:(21,1),3:(36,1),
                     4:(7,17),5:(21,17),6:(36,17),
                     7:(7,32),8:(21,32),9:(36,32)}
    for i in range(9):
        for j in range(9):
            X, Y = j*BLOCK_SIDE, i*BLOCK_SIDE
            for number in comments_grid[i][j]:
                comments_to_draw=COMMENTS_FONT.render(str(number),1,DARK_GREY)
                WINDOW.blit(comments_to_draw,(X+offset_comments[number][0],Y+offset_comments[number][1]))


def draw_notes_button(comments_activated): #dessine le bouton note qui permet au joueur de passer en mode note ou non
    if comments_activated:
        pygame.draw.rect(WINDOW,BLUE_GREY,BUTTUN_CRAYON)   #le bouton apparait en bleu clair si le mode note est activé
    else:
        pygame.draw.rect(WINDOW,PINK,BUTTUN_CRAYON)    #le bouton apparait en rose si le mode note est désactivé
    WINDOW.blit(IMAGE_CRAYON,(490,95))

def draw_pause_button(in_pause): #dessine le bouton pause qui permet au joueur de passer en mode pause ou play
    if in_pause:
        
        WINDOW.blit(IMAGE_PLAY,(600,95))  #affiche le bouton play si le joueur est en mode pause
    else:

        WINDOW.blit(IMAGE_PAUSE,(600,95)) #affiche le bouton pause si le joueur est en mode play

#bouton nouvelle partie
BUTTON_NEW_GAME=pygame.draw.rect(WINDOW,BLUE_GREY,pygame.Rect(490,180,270,70))

def draw_new_game_button():   #dessine le bouton nouvelle partie qui remet tous les paramètres à l'état initial (timer,mode note,mode pause) et affiche une nouvelle grille de jeu
    pygame.draw.rect(WINDOW,BLUE_GREY,pygame.Rect(490,180,270,70))
    text=NEW_GAME_FONT.render("Nouvelle partie",1,BLACK)
    WINDOW.blit(text,(490+30,180+10))
    


def draw_hint_button():    #dessine le bouton indice qui révèle le chiffre de la solution correspondant à la case sélectionnée
    WINDOW.blit(IMAGE_BULB,(700,85))


#boutton quitter
BUTTON_QUIT = pygame.draw.rect(WINDOW,BLUE_GREY,pygame.Rect(490,260,270,70))

def draw_quit_button():  #dessine le bouton quiiter qui permet de quitter la partie 
    pygame.draw.rect(WINDOW,BLUE_GREY,pygame.Rect(490,260,270,70))
    quit_text = NEW_GAME_FONT.render("Quitter",1,BLACK)
    WINDOW.blit(quit_text,(490+80,270))

#boutton révéler
BUTTON_SHOW = pygame.draw.rect(WINDOW,BLUE_GREY,pygame.Rect(490,340,270,70))

def draw_show_button(): #dessine le bouton révéler qui permet d'afficher la solution à la grille initiale 
    pygame.draw.rect(WINDOW,BLUE_GREY,pygame.Rect(490,340,270,70))
    show_text = NEW_GAME_FONT.render("Révéler",1,BLACK)
    WINDOW.blit(show_text,(490+80,350))


def draw_music_button(music_activated):
    if music_activated:
        WINDOW.blit(IMAGE_MUSIC_ON,(500,30))
    else:
        WINDOW.blit(IMAGE_MUSIC_OFF,(500,30))



def draw_time(total_time): #dessine le timer à droite  de la grille
    total_time //=1000
    heures = str(total_time//3600)
    minutes = str(total_time//60)
    secondes = str(total_time%60)
    text = ""

    if heures!='0':
        if len(heures)==1:
            text+='0'
        text+=heures + ':'
    if len(minutes)==1:
        text+="0"
    text+=minutes + ":"
    if len(secondes)==1:
        text+='0'
    text+=secondes
    
    time_text = TIME_FONT.render(text,1,BLACK)
    WINDOW.blit(time_text,(600,30))

def draw_empty_grid(): #dessine une grille vide (utilisée quand le joueur met le jeu en pause)
    WINDOW.fill(WHITE)
    draw_grid()


# fonction qui dessine la fenêtre à chaque tour dans la boucle de jeu
def draw_window(grid, comments_grid,current_case_selected_i, current_case_selected_j,original_coordinates,total_time,comments_activated,in_pause,game_won,music_activated):
    WINDOW.fill(WHITE)
    draw_current_case_selected(grid,
        current_case_selected_i, current_case_selected_j)

    draw_grid()

    draw_numbers(grid,original_coordinates)

    draw_comments(comments_grid)


    if in_pause:
        draw_empty_grid()
    
    if game_won:
        winner_text = WINNER_FONT.render("Partie terminée !",1,RED)
        WINDOW.blit(winner_text,(560,2))


    draw_notes_button(comments_activated)
    draw_pause_button(in_pause)
    draw_new_game_button()
    draw_hint_button()
    draw_quit_button()
    draw_show_button()
    draw_music_button(music_activated)

    draw_time(total_time)




    pygame.display.update()



def handle_music(music_activated): #gère la musique de fond 
    if not music_activated and BACKGROUND_MUSIC.get_num_channels(): #coupe la musique si l'utilisateur n'en veut plus
        BACKGROUND_MUSIC.fadeout(1000)
    if music_activated and not BACKGROUND_MUSIC.get_num_channels(): #relance la musique si elle s'était arrêtée
        BACKGROUND_MUSIC.play()


###########################################################################################################################################
######################################## Fonctions qui gèrent les intééractions du joueur #################################################
###########################################################################################################################################



def handle_quit(event, run): #permet de quitter la fenêtre en cliquant sur la croix en haut de la fenêtre ou sur le bouton quitter ou en tapant sur échap
    #si une des ces évènement a lieu run=False et la fonction renvoie False
    if event.type == pygame.QUIT:  # Quitte le jeu si on appuie sur la croix
        run = False
    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
        run = False
    run=interact_buttons(event,BUTTON_QUIT,run)
    return run

def mode_comments_selected(event,comments_activated): #permet de passer en mode notes ou non si la touche 'c' est pressé ou si le joueur clique sur le bouton note (celui avec l'image de crayon)
    #si un de ces évènement a lieu la valeur du booléen comments_activated change
    if event.type == pygame.KEYDOWN and event.key == pygame.K_c : #Si l'utilisateur appuie sur la touche 'c' du clavier, il passera en mode commentaires
        comments_activated = not comments_activated
    comments_activated = interact_buttons(event,BUTTUN_CRAYON,comments_activated)
    return comments_activated

def mode_pause_selected(event,in_pause): #permet de passer en mode pause ou play si la 'p' est pressé ou si le joueur clique sur le bouton play/pause
    #si un de ces évvènements a lieu la valeur du booléen in_pause change
    if event.type == pygame.KEYDOWN and event.key == pygame.K_p :
        in_pause = not in_pause
    in_pause = interact_buttons(event,BUTTON_PLAY_PAUSE,in_pause)
    return in_pause



# quand le joueur appuie sur une des flèches du clavier ou clique sur une case, la fonction fait un update de la case sélectionnée
def update_current_case_selected(event, current_case_selected_i, current_case_selected_j):
    if event.type == pygame.KEYDOWN:  # si le joueur appuie sur une touche du clavier
        if event.key == pygame.K_RIGHT and current_case_selected_j < 8: #droite
            current_case_selected_j += 1
        if event.key == pygame.K_LEFT and current_case_selected_j > 0: #gauche
            current_case_selected_j -= 1
        if event.key == pygame.K_UP and current_case_selected_i > 0: #haut
            current_case_selected_i -= 1
        if event.key == pygame.K_DOWN and current_case_selected_i < 8: #bas
            current_case_selected_i += 1
    if event.type == pygame.MOUSEBUTTONDOWN: #si le joueur clique sur une case
        if event.button == 1:
            mx, my = pygame.mouse.get_pos()
            i, j = my//BLOCK_SIDE, mx//BLOCK_SIDE
            if i < 9 and j < 9 and i >= 0 and j >= 0:
                current_case_selected_i, current_case_selected_j = i, j

    return current_case_selected_i, current_case_selected_j  


def update_grid(event, grid, current_case_selected_i, current_case_selected_j,original_coordinates,comments_grid,comments_activated): #met à jour la grille et la grille de notes
    keys_to_numbers = {pygame.K_1 : 1,pygame.K_2 : 2,pygame.K_3 : 3,
                        pygame.K_4 : 4,pygame.K_5 : 5,pygame.K_6 : 6,
                        pygame.K_7 : 7,pygame.K_8 : 8,pygame.K_9 : 9}
    if (current_case_selected_i, current_case_selected_j) in original_coordinates or event.type != pygame.KEYDOWN: #Si la case était dans la grille de départ, on n'y touche pas
                                                                                                                   #De même, si l'évènement ne correspond pas à une touche appuyée sur le clavier, on ne fait rien
        return grid,comments_grid
    
    if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE: #Si l'utilisateur appuie sur DEL, on supprime les chiffres et les commentaires de la grille
        grid[current_case_selected_i][current_case_selected_j] = 0
        comments_grid[current_case_selected_i][current_case_selected_j].clear()
    
    
    for key in keys_to_numbers.keys(): #ajoute les chiffres dans les cases
        if event.key==key:
            if not comments_activated:# si le joueur n'est pas en mode notes on ajoute les chiffres classiques à la grille
                grid[current_case_selected_i][current_case_selected_j] = keys_to_numbers[key]
                comments_grid[current_case_selected_i][current_case_selected_j].clear()
            elif grid[current_case_selected_i][current_case_selected_j]==0: #si le joueur est en mode notes et que la cas est vide, on ajoute les chiffres à la grille de notes
                if keys_to_numbers[key] not in comments_grid[current_case_selected_i][current_case_selected_j]:
                    comments_grid[current_case_selected_i][current_case_selected_j].add(keys_to_numbers[key])
                else:
                    comments_grid[current_case_selected_i][current_case_selected_j].remove(keys_to_numbers[key])
    
    return grid, comments_grid #renvoie la grille et la grille de commentaires


def interact_buttons(event,button,Bool): #si le joueur clique sur un bouton, change la valeur du booléen associé et renvoie ce booléen 
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
            CLICK_SOUND.play()
            x,y=pygame.mouse.get_pos()
            if button.collidepoint(x,y):
                Bool = not Bool        
    return Bool

def interact_new_game(event,button): # si le joueur clique sur un bouton renvoie True sinon renvoie False
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
            CLICK_SOUND.play()
            x,y=pygame.mouse.get_pos()
            if button.collidepoint(x,y):
                return True
    return False

############################################################################################
######################### Fonctions destinées à l'écran d'accueil ##########################
############################################################################################


def choose_difficulty(event,choosing_difficulty): #dans la page d'accueil du jeu, permet au joueur de choisir la difficulté
    difficulty = None
    if event.type == pygame.KEYDOWN :
        if event.key == pygame.K_0:
            difficulty = 0
            choosing_difficulty = False
        elif event.key == pygame.K_1 : 
            difficulty = 1
            choosing_difficulty = False
        elif event.key == pygame.K_2 :
            difficulty = 2
            choosing_difficulty = False
    return choosing_difficulty,difficulty


def draw_home_page(): #dessine l'écran d'accueil
    WINDOW.fill(WHITE)

    home_text = HOME_FONT.render('Pour commencer, veuillez choisir votre niveau',1,BLACK)
    WINDOW.blit(home_text,(40,150))
    diff_text_easy = HOME_LITTLE_FONT.render('Facile : tapez 0',1,BLACK)
    WINDOW.blit(diff_text_easy,(280,200))
    diff_text_medium = HOME_LITTLE_FONT.render('Moyen : tapez 1',1,BLACK)
    WINDOW.blit(diff_text_medium,(276,250))
    diff_text_hard = HOME_LITTLE_FONT.render('Difficile : tapez 2',1,BLACK)
    WINDOW.blit(diff_text_hard,(265,300))


    pygame.display.update()


##################################################################################################################################
######################################## Fonction finale qui fait tourner le jeu #################################################
##################################################################################################################################


def play_windows(): #fonction main qui gère le jeu 

    # Booléen qui gère la fin du jeu (quand run devient faux, le jeu s'arrête)
    run = True

    choosing_difficulty = True
 
    while choosing_difficulty: #loop dans laquelle le joueur va choisir sa difficulté, dans l'écran d'accueil
        
        draw_home_page()

        for event in pygame.event.get():
            choosing_difficulty,difficulty = choose_difficulty(event,choosing_difficulty) #si le joueur tape sur 0,1 ou 2 pour choisir son niveau de difficulté, la phase de choix de difficulté est terminée : choosing_difficulty passe à False, et on récupère le niveau de difficulté choisi

            if not choosing_difficulty:
                break
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE): #si l'utilisateur veut quitter le jeu avant d'avoir choisi la difficulté
                run = False
                choosing_difficulty = False

        
    BACKGROUND_MUSIC.play()
    music_activated = True


    clock = pygame.time.Clock()
    total_time = 0

    grid = create_sudoku(9,difficulty)[1] #on crée une nouvelle grille selon le niveau de difficulté

    

    original_coordinates = [(i,j) for i in range(9) for j in range(9) if grid[i][j]!=0] #liste de tuples contenant les coordonnées des cases non nulles de la grille initiale
    current_case_selected_i, current_case_selected_j = 0, 0  #coordonées de la case sélectionnée au début

    solved_grid = copy.deepcopy(grid) 
    solve_sudoku_unique(solved_grid,0,0)  # grille solution de la grille initiale

    comments_activated = False #variable qui indique l'état du mode notes (False correspond au mode notes désactivé)
    comments_grid = [[set() for j in range(9)] for i in range(9)] #grille (=liste de liste) contenant les notes de chaque case sous forme de set()

    in_pause=False #variable qui indique l'état de mode pause (False correspond à un jeu en cours)
    game_won = False #variable qui indique l'état de la partie : si la grille est pleine et correcte, game_won passera à True et le timer sera gelé

    while run:  # boucle du jeu : tourne tant que le jeu n'est pas terminé

        # s'assure que la boucle ne tourne pas trop vite. Le jeu tournera ici en MAX_FPS images par secondes
        clock.tick(MAX_FPS)
        
        if not in_pause and not game_won: #si le jeu n'est pas en pause ou terminé, le timer continue de s'incrémenter, il s'arrête sinon
            total_time+=clock.get_time()
        
        if is_full(grid): #si la grille est pleine, on vérifie que les valeurs rentrées par l'utilisateur sont correctes (game_won passe à True si c'est le cas)
            game_won = check_solutions(grid)        

        for event in pygame.event.get():

            run = handle_quit(event, run) # permet de quitter le jeu (met run à False quand l'utilisateur clique sur la croix ou échap ou sur le bouton quitter avec la souris)
            
            current_case_selected_i, current_case_selected_j = update_current_case_selected(
                event, current_case_selected_i, current_case_selected_j)#change la case sélectionnée lorsque l'utilisateur clique sur la case ou joue avec les flèches

            comments_activated = mode_comments_selected(event,comments_activated) #permet de changer le mode notes
            
            in_pause = mode_pause_selected(event,in_pause)#permet de changer le mode play ou pause

            music_activated = interact_buttons(event,BUTTON_MUSIC,music_activated) #si le joueur appuie sur le bouton musique, il change la valeur du booléen music_activated

            grid,comments_grid = update_grid(
                event, grid, current_case_selected_i, current_case_selected_j,original_coordinates,comments_grid,comments_activated) #change les numéros quand l'utilisateur rentre un nouveau chiffre
            
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_n) or interact_new_game(event,BUTTON_NEW_GAME): #permet de lancer une nouvelle partie en cliquant sur le bouton nouvelle partie ou en tapant la touche 'n'
                
                grid = create_sudoku(9,difficulty)[1] #on prend une nouvelle grille selon le niveau de difficulté
                
                #on remet les paramètres à l'état initial
                total_time=0   
                comments_activated=False
                in_pause=False
                game_won = False
                comments_grid = [[set() for j in range(9)] for i in range(9)]
                current_case_selected_i, current_case_selected_j = 0, 0
                original_coordinates = [(i,j) for i in range(9) for j in range(9) if grid[i][j]!=0]

                solved_grid = copy.deepcopy(grid)    #grille solution correspondant à la nouvelle grille 
                solve_sudoku_unique(solved_grid,0,0)
            
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_h) or interact_new_game(event,BUTTON_HINT): #permet de dévoiler le chiffre de la case sélectionnée correspondant à la grille solution en cliquuant sur le bouton hint répresenter par une ampoule ou tapant la touche 'h'
                comments_grid[current_case_selected_i][current_case_selected_j].clear()
                grid[current_case_selected_i][current_case_selected_j] = solved_grid[current_case_selected_i][current_case_selected_j] 

            if interact_new_game(event,BUTTON_SHOW): #permet de dévoiler toute la grille solution en cliquant sur le bouton révéler
                grid = copy.deepcopy(solved_grid)
                comments_grid = [[set() for j in range(9)] for i in range(9)]

        # A chaque tour dans la boucle, on redessine la fenêtre, avec la grille qui a potentiellement été modifiée
        draw_window(grid,comments_grid, current_case_selected_i, current_case_selected_j,original_coordinates,total_time,comments_activated,in_pause,game_won,music_activated)

        handle_music(music_activated)
    pygame.quit()  # fonction obligatoire pour quitter le jeu


if __name__ == "__main__":
    play_windows()