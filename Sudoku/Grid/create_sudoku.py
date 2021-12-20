###########################################################################################################################################################
######################################################### Import des fonctions ############################################################################
###########################################################################################################################################################
import sys
from pathlib import Path
file = Path(__file__).resolve()
package_root_directory = file.parents[1]
sys.path.append(str(package_root_directory))

from Grid.Check_solution import grid_to_subgrid
from Solve_sudoku.Solve_backtracking import solve_sudoku_unique, solve_sudoku
from math import sqrt
import random
import numpy as np
import copy



###########################################################################################################################################################
################################# Fonctions pour mélanger la solution rencontré et complexifier le sudoku #################################################
###########################################################################################################################################################

# Cette fonction déplace n positions d'une liste à gauche

def shift(list, n):
    return list[n:] + list[:n]

# Cette fonction mélange les blocks d'une grille de sudoku en gardant les conditions sur les lignes, colonnes et sous-grilles
# C'est utilisé pour cacher la logique utilisée lors de l'obtention de la solution


def shuffle_sudoku_blocks(grid):
    # Convertit chaque sous-grille en une ligne
    grid = grid_to_subgrid(grid)
    # Prend la transpose
    grid = np.array(grid).T.tolist()
    return grid

# Cette fonction mélange les lignes d'une grille de sudoku en gardant les conditions sur les lignes, colonnes et sous-grilles


def shuffle_sudoku_lines(grid):
    # Dimmension de la grille principale
    dim = len(grid)
    # Dimmension de la sous grille
    dim_sub = int(sqrt(dim))
    # Compteur pour choisir une sous-grille
    n = 0
    # Variable auxiliare
    aux = copy.deepcopy(grid)
    for i in range(0, dim):
        if i in list(range((int(n*dim_sub)), int((n+1)*dim_sub)-1)):
            # Mélange les lignes d'une sous-grille
            random.shuffle(grid[i:i+dim_sub])
        else:
            aux = grid[n*dim_sub][:]
            # Mélange les lignes d'une sous-grille
            grid[n*dim_sub][:] = grid[(n+1)*dim_sub-1][:]
            # Mélange les lignes d'une sous-grille
            grid[(n+1)*dim_sub-1][:] = aux
            # Choisit la sous-grille prochaine
            n = n+1
    return grid

# Cette fonction mélange les colonnes d'une grille de sudoku en gardant les conditions sur les lignes, colonnes et sous-grilles


def shuffle_sudoku_columns(grid):
    grid = np.array(grid).T.tolist()
    grid = shuffle_sudoku_lines(grid)
    return grid


###########################################################################################################################################################
###################################### Fonction permettant la création d'une grille de Sudoku #############################################################
###########################################################################################################################################################

# Cette fonction crée une grille sudoku rempli et mélange ses élements en utilisant les fonctions au-dessus
def create_sudoku_complete(dim):
    # Crée une grille dim x dim vide
    grid = [[0]*dim]*dim
    # Obtient la dimension de la sous-grille
    dim_sub = int(sqrt(dim))
    # Ajoute des chiffres sur la ligne
    grid[0] = list(range(1, dim+1))
    # Mélange les chiffres de la ligne
    random.shuffle(grid[0])
    n = 0
    for i in range(1, dim):
        if i in list(range((int(n*dim_sub+1)), int((n+1)*dim_sub))):
            # Ajoute des valeur à la grille suivant les règles pour créer une grille de sudoku
            grid[i] = shift(grid[i-1], dim_sub)
        if int(i % dim_sub) == 0:
            n = n+1
            # Ajoute des valeur à la grille suivant les règles pour créer une grille de sudoku
            grid[n*dim_sub] = shift(grid[n*dim_sub-1], 1)
    # Mélange les colonnes pour complexifier le jeu
    grid = shuffle_sudoku_columns(grid)
    # Mélange les lignes pour complexifier le jeu
    grid = shuffle_sudoku_lines(grid)
    # Mélange les sous-grilles pour complexifier le jeu
    grid = shuffle_sudoku_blocks(grid)
    # Mélange les colonnes pour complexifier le jeu
    grid = shuffle_sudoku_columns(grid)
    return grid

 ###########################################################################################################################################################
 ################ Fonctions utilisées pour effacer des cases d'une grille compléte et créer une grille de sudoku initiale  #################################
 ###########################################################################################################################################################

# Cette fonction obtient les positions des cases remplies d'une grille sudoku


def get_filled_tiles_positions(game_grid):
    tiles = []
    for i in range(0, len(game_grid)):
        for j in range(0, len(game_grid)):
            if game_grid[i][j] != 0:
                # Liste avec les positions rempli
                tiles.append((i, j))
    return tiles

# Cette fonction génère de façon aléatoire une position vide de la grille


def get_filled_position_to_erase(game_grid):
    # Obtient une position rempli de façon aleatoire
    x, y = random.choice(get_filled_tiles_positions(game_grid))
    return x, y

# Cette fonction reçoit une grille de sudoku complète, efface quelques uns de ses élements de façon aléatoire et génére une grille de sudoku initialle


def sudoku_complete_to_init(grid_complete, level):
    dim = len(grid_complete)
    dim_sub = int(sqrt(dim))
    grid_init = copy.deepcopy(grid_complete)
    if dim == 9 and level == 0:
        # 0 correspond à facile
        nb_positions_to_erase = 18
    elif dim == 9 and level == 1:
        # 1 correspond à moyen
        nb_positions_to_erase = 24
    elif dim == 9 and level == 2:
        # 2 correspond à difficile
        nb_positions_to_erase = 40
    elif dim == 16 and level == 0:
        nb_positions_to_erase = 50
    elif dim == 16 and level == 1:
        nb_positions_to_erase = 75
    elif dim == 16 and level == 2:
        nb_positions_to_erase = 100
    elif dim == 25 and level == 0:
        nb_positions_to_erase = 100
    elif dim == 25 and level == 1:
        nb_positions_to_erase = 200
    elif dim == 25 and level == 2:
        nb_positions_to_erase = 300
    # Efface des caractères de la grille jusqu'à ce qu'il n'y en ait seulement nb_positions_to_erase
    while nb_positions_to_erase >= 0:
        x, y = get_filled_position_to_erase(grid_init)
        grid_init[x][y] = 0
        # Décompte
        nb_positions_to_erase -= 1
    return grid_init


# Cette fonction crée un jeu de sudoku avec des chiffres initiaux et sa solution
def create_sudoku(dim, level):
    # Crée une grille de sudoku complète
    grid_complete = []
    grid_init = []
    sol=[]
    # On crée une grille compléte et ensuite en efface quelques de ses éléments
    if dim in [16, 25]:
        grid_complete = create_sudoku_complete(dim)
        grid_init = sudoku_complete_to_init(grid_complete, level)
    else:
        while True:
            grid_complete = create_sudoku_complete(dim)
            grid_init = sudoku_complete_to_init(grid_complete, level)
            # On utilise le solver pour rendre la solution unique
            sol = solve_sudoku(0, 0, grid_init)
            if len(sol) == 9:                                                #ici, grid_complete==sol, parce que la solution est unique
                break
    return grid_complete, grid_init