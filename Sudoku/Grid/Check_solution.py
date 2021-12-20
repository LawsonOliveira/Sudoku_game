###########################################################################################################################################################
######################################################### Import des fonctions ############################################################################
###########################################################################################################################################################

import copy
from math import sqrt
import numpy as np

###########################################################################################################################################################
################################################### Fonctions pour tester la fin du jeu ###################################################################
###########################################################################################################################################################


# Cette fonction reçoit une grille n x n et fait la conversion pour mettre des sous-grilles de taile n^(1/2) x n^(1/2) dans une seule ligne
def grid_to_subgrid(grid):
    dim=len(grid)
    subgrids=[[0]*dim]*dim
    dim_sub=int(sqrt(dim))
    for i in range(0,dim,dim_sub):
        for j in range(0,dim_sub):  
            aux=[]
            for k in range(0,dim_sub):  
                aux=aux+grid[i+k][j*dim_sub:(j+1)*dim_sub]
            subgrids[i+j]=aux
    return subgrids

# Cette fonction reçoit des subgrids de taile n^(1/2) x n^(1/2) et fait la conversion pour une grille n x n
def subgrid_to_grid(subgrid):
    dim=len(subgrid)
    grid=[[0]*dim]*dim
    dim_sub=int(sqrt(dim))
    for i in range(0,dim,dim_sub):
        for j in range(0,dim_sub):  
            aux=[]
            for k in range(0,dim_sub):  
                aux=aux+subgrid[i+k][j*dim_sub:(j+1)*dim_sub]
            grid[i+j]=aux
    return grid

# Cette fonction reçoit une grille n x n et verifie si elle satisfait toutes les conditions pour les lignes
# Cette fonction renvoie un booléen et un dictionnaire avec toutes les erreurs sur les lignes
def check_line(grid):
    line_condition=True
    aux=True
    dict_errors_line={}                                     # Repertorie tous les doublons de chaque ligne avec le numéro de ligne en clé             
    dim=len(grid)
    dict={}                                                 # Dictionnaire utilisé pour vérifier si il y a des doublons sur la ligne
    for i in range(1,dim+1):
        dict[i]=i
    dict_aux=copy.deepcopy(dict)
    for i in range(dim):
        dict=copy.deepcopy(dict_aux)
        list_errors_line=[]
        for j in range(dim):
            if grid[i][j] in dict.values():
                line_condition=line_condition and aux
                dict.pop(grid[i][j])
            else:
                aux=False
                list_errors_line=[grid[i][j]]+list_errors_line
        dict_errors_line[i]=list_errors_line
    return line_condition, dict_errors_line

# Cette fonction reçoit une grille n x n et verifie si elle satisfait toute les conditions pour les colonnes
def check_column(grid):
    grid=np.array(grid).T.tolist()                  # On vérifie que la transposée satisfait toutes les conditions pour les lignes
    return check_line(grid)

# Cette fonction reçoit une grille et verifie si elle satisfait toutes les conditions pour les sous-grilles
def check_subgrid(grid):
    sub_grid=grid_to_subgrid(grid)                  # On vérifie que la grille dont chaque ligne correspond à une sous-grille initiale vérifie toutes les conditions sur les lignes
    return check_line(sub_grid)

# Cette fonction reçoit une grid et vérifie si la grid est une solution
def check_solutions(grid):
    return check_line(grid)[0] and check_column(grid)[0] and check_subgrid(grid)[0]

#cette fonction recoit une grille et renvoie true si tous les chiffres de la grille ont été complétés, et false si le joueur peut encore rajouter un chiffre dedans
def is_full(grid):
    Bool = True
    for i in range(9):
        for j in range(9):
            if not grid[i][j]:
                Bool = False
                break
    return Bool


