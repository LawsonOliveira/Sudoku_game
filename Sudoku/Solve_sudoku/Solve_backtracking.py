###########################################################################################################################################################
######################################################### Import des fonctions ############################################################################
###########################################################################################################################################################
import sys
from pathlib import Path
file = Path(__file__).resolve()
package_root_directory = file.parents[1]
sys.path.append(str(package_root_directory))

from math import sqrt
import copy


###########################################################################################################################################################
############################################################ Solver d'une grille sudoku ###################################################################
###########################################################################################################################################################

# Renvoie True ou False selon que la valeur n est compatible dans la position (ligne i, colonne j)
def carac_possible(grid, i, j, n):
    dim=len(grid)
    dim_sub=int(sqrt(dim))
    for ligne in range(dim):
        if grid[ligne][j] == n:
            return(False)
    for colonne in range(dim):
        if grid[i][colonne] == n:
            return(False)
    x0 = i//dim_sub
    y0 = j//dim_sub  # Coordonnées des premières lignes et colonnes de la case
    list_subgrid = []
    for k in range(dim_sub):
        for p in range(dim_sub):
            list_subgrid.append(grid[dim_sub*x0+k][dim_sub*y0+p])
    if n in list_subgrid:
        return(False)
    return(True)

# Obtient les caractères possibles dans la position (i,j) de la grille
def get_possible(grid,i,j):
    list=[]
    for element in range(1,len(grid)+1):
        if carac_possible(grid,i,j,element):
            list.append(element)
    return list

# Obtient tous les solutions possibles de la grille initiale 9x9
def solve_sudoku(i,j,grid_aux):
    grid=copy.deepcopy(grid_aux)
    if i==8 and j==9:
        return grid
    if j>8:
        return solve_sudoku(i+1,0,grid)
    if grid[i][j]==0:
        list=get_possible(grid,i,j)
        resp=[]
        for element in list:
            grid[i][j]=element
            aux=solve_sudoku(i,j+1,grid)
            resp += aux                  
            grid[i][j]=0                  
        return resp
    else:
        return solve_sudoku(i,j+1,grid)


###########################################################################################################################################################
#################################### Vérifier se une grille sudoku admet solution et la retourne ###################################################
###########################################################################################################################################################


# Renvoie True ou False selon que la grille admette une solution ou non. La grille est de plus modifiée, de sorte à avoir les solutions
def solve_sudoku_unique(grid, i, j): 
    if (i == 8 and j == 9):                             # On était sur la dernière case, et elle est valide. On a donc trouvé la solution!
        return True 
    if j == 9:                                          # On arrive en bout de ligne, on passe donc à la ligne suivante
        i += 1
        j = 0
    if grid[i][j] > 0:                                  # On est sur une valeur deja remplie de la grille, on passe à la case d'après
        return solve_sudoku_unique(grid, i, j + 1)
    for n in range(1, 10):                              # On parcourt les valeurs possibles de 1 à 9
        if carac_possible(grid,i,j,n):                  # Si la valeur est possible...
            grid[i][j] = n
            if solve_sudoku_unique(grid, i, j + 1):     # On vérifie si la valeur d'après est possible    RECURSION
                return (True)
        grid[i][j] = 0                                  # Si aucune valeur n'est possible pour la case suivante, on remet la valeur de la case à 0 et on essaye les autres valeurs de n possibles.
    return (False)
