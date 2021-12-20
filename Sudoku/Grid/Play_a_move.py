###########################################################################################################################################################
######################################################### Import des fonctions ############################################################################
###########################################################################################################################################################

import sys
from pathlib import Path
file = Path(__file__).resolve()
package_root_directory = file.parents[1]
sys.path.append(str(package_root_directory))

import copy
from Grid.Display_grids import converte_to_theme


###########################################################################################################################################################
################################################### Fonctions pour recevoir des entrées ###################################################################
###########################################################################################################################################################

# Vérifie si il est possible pour l'utilisateur de changer le valeur de la grille
def check_coord(grid_init):
    coord=[]
    for i in range(len(grid_init)):
        for j in range(len(grid_init)):
            if grid_init[i][j] == 0:
                coord.append((j+1,i+1))                                         # Liste des positions lesquelles sont possibles changer
    return coord

# Renvoie un tuple de dimension 3 : (valeur voulue, abscisse, ordonnée)
def read_player_command(grid_init):
    dim=len(grid_init)
    possible_carac,themes=converte_to_theme(grid_init)[1:]              # convert_to_theme revnvoie le thème de la grille en fonction de sa taille et les caractères pouvant être joués
    data_in = 0
    themes_nb = {v: k for k, v in themes.items()}                       # On inverse les clés et les valeurs du dictionnaire
    while data_in not in list(themes.values())[1:]+['a']+['s']:
        print("\nChiffres/lettres possibles : "+possible_carac)
        data_in = input("Rentrez la valeur/lettre de la case à remplir, 'a' si vous souhaitez abandonner et vérifier la solution ou 's' pour faire une sauvegarde du jeu et sortir : " )
    if data_in in ['a','s']:
        return data_in
    else:
        data_in=themes_nb[data_in]
        coordx = input("Rentrez la coordonnée de l'abscisse de la case à remplir (Exemple: si la case est situé sur la colonne 4, rentrez 4 ) : ")
        coordy = input("Rentrez la coordonnée de l'ordonnée de la case à remplir (Exemple: si la case est situé sur la ligne 4, rentrez 4 ) : ")
        while coordx not in [str(i) for i in range(1,dim+1)] or coordy not in [str(i) for i in range(1,dim+1)] or (coordx,coordy) in check_coord(grid_init):
            coordx = input("Rentrez la coordonnée de l'abscisse de la case à remplir, il n'est pas possible de modifier les valeurs initiales de la grille): ")
            coordy = input("Rentrez la coordonnée de l'ordonnée de la case à remplir, il n'est pas possible de modifier les valeurs initiales de la grille) : ")
        move = (data_in,int(coordx),int(coordy))
        return move

# Renvoie la dimension et le niveau de difficulté choisis par l'utilisateur
def read_dimension_level():
    dim = int(input("Entrez la dimension de la grille (9, 16 ou 25) : "))
    level = int(input("Choisissez la difficulté du sudoku (facile : 0, moyen : 1 ou difficile : 2) : "))
    while dim not in [9,16,25]:
        dim = int(input("Attention, entrez la dimension de la grille (9, 16 ou 25) : "))
    while level not in [0,1,2]:
        level = int(input("Attention, choisissez la difficulté du sudoku (facile : 0, moyen : 1 ou difficile : 2) : "))
    return dim, level

# Renvoie une grille ayant pris en compte le coup du joueur
def update_grid(grid,move):
    new_grid = copy.deepcopy(grid)
    new_grid[move[2]-1][move[1]-1] = move[0]            # move est un tuple de dimension 3 : (valeur voulue, abscisse, ordonnée)
    return new_grid
    