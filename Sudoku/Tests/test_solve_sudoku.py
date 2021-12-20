
###########################################################################################################################################################
######################################################### Import des fonctions ############################################################################
###########################################################################################################################################################
import sys
from pathlib import Path
file = Path(__file__).resolve()
package_root_directory = file.parents[1]
sys.path.append(str(package_root_directory))

from pytest import *
from Solve_sudoku.Solve_backtracking import *
from Data.Auxiliary_grids.Easy_grids import *
from Data.Auxiliary_grids.Medium_grids import *


###########################################################################################################################################################
####################################################### Testes des fonctions de Solve_sudoku #######################################################
###########################################################################################################################################################


# Teste de la fonction qui renvoie True ou False selon que la valeur n est compatible dans la position (ligne i, colonne j)
def test_carac_possible():
    assert carac_possible(grid_f1,0,0,5) == False
    assert carac_possible(grid_f2,1,1,5) == False
    assert carac_possible(grid_f3,3,3,8) == True
    assert carac_possible(grid_m1,5,4,1) == False


# Teste de la fonction qui obtient les caractères possibles dans la position (i,j) de la grille
def test_get_possible():
    assert get_possible(grid_f1,0,0)==[3, 6, 9]
    assert get_possible(grid_f2,1,5)==[4]
    assert get_possible(grid_f3,7,2)==[1, 5]
    assert get_possible(grid_m1,4,1)==[2, 3, 5, 6]


# Teste de la fonction qui obtient tous les solutions possibles de la grille initiale 9x9
def test_solve_sudoku():
    assert solve_sudoku(0,0,grid_f1)==[[6, 1, 3, 5, 4, 9, 2, 8, 7], [2, 5, 7, 8, 3, 1, 4, 6, 9], [9, 8, 4, 6, 7, 2, 3, 5, 1], [8, 3, 2, 1, 5, 7, 9, 4, 6], [7, 4, 5, 3, 9, 6, 1, 2, 8], [1, 9, 6, 2, 8, 4, 5, 7, 3], [3, 7, 8, 4, 1, 5, 6, 9, 2], [4, 2, 9, 7, 6, 3, 8, 1, 5], [5, 6, 1, 9, 2, 8, 7, 3, 4]]
    assert solve_sudoku(0,0,grid_f2)==[[4, 2, 7, 5, 6, 8, 9, 1, 3], [6, 8, 3, 1, 9, 7, 2, 5, 4], [9, 1, 5, 3, 4, 2, 6, 8, 7], [2, 5, 6, 4, 7, 3, 8, 9, 1], [3, 4, 9, 8, 5, 1, 7, 2, 6], [8, 7, 1, 9, 2, 6, 3, 4, 5], [1, 3, 2, 6, 8, 5, 4, 7, 9], [5, 9, 8, 7, 3, 4, 1, 6, 2], [7, 6, 4, 2, 1, 9, 5, 3, 8]]
    assert solve_sudoku(0,0,grid_f3)==[[9, 4, 6, 1, 5, 7, 8, 2, 3], [1, 2, 8, 3, 9, 6, 7, 5, 4], [5, 7, 3, 2, 8, 4, 1, 6, 9], [3, 5, 1, 6, 7, 2, 9, 4, 8], [4, 6, 9, 8, 3, 1, 2, 7, 5], [2, 8, 7, 5, 4, 9, 6, 3, 1], [6, 9, 2, 4, 1, 5, 3, 8, 7], [8, 1, 5, 7, 6, 3, 4, 9, 2], [7, 3, 4, 9, 2, 8, 5, 1, 6]]
    assert solve_sudoku(0,0,grid_m1)==[[3, 5, 9, 7, 6, 4, 1, 8, 2], [7, 1, 6, 5, 8, 2, 4, 9, 3], [8, 2, 4, 9, 1, 3, 7, 5, 6], [6, 9, 1, 2, 7, 8, 5, 3, 4], [4, 8, 3, 1, 5, 9, 2, 6, 7], [2, 7, 5, 4, 3, 6, 9, 1, 8], [9, 3, 7, 8, 2, 5, 6, 4, 1], [5, 6, 2, 3, 4, 1, 8, 7, 9], [1, 4, 8, 6, 9, 7, 3, 2, 5]]


# Teste qui de la fonction qui renvoie True ou False selon que la grille admette une solution ou non. La grille est de plus modifiée, de sorte à avoir les solutions
def test_solve_sudoku_unique():
    grid1=copy.deepcopy(grid_f1)
    grid2=copy.deepcopy(grid_f2)
    grid3=copy.deepcopy(grid_f3)
    grid4=copy.deepcopy(grid_f4)

    assert solve_sudoku_unique(grid1,0,0)== True
    assert grid1==[[6, 1, 3, 5, 4, 9, 2, 8, 7], [2, 5, 7, 8, 3, 1, 4, 6, 9], [9, 8, 4, 6, 7, 2, 3, 5, 1], [8, 3, 2, 1, 5, 7, 9, 4, 6], [7, 4, 5, 3, 9, 6, 1, 2, 8], [1, 9, 6, 2, 8, 4, 5, 7, 3], [3, 7, 8, 4, 1, 5, 6, 9, 2], [4, 2, 9, 7, 6, 3, 8, 1, 5], [5, 6, 1, 9, 2, 8, 7, 3, 4]]
    assert solve_sudoku_unique(grid2,0,0)== True
    assert grid2==[[4, 2, 7, 5, 6, 8, 9, 1, 3], [6, 8, 3, 1, 9, 7, 2, 5, 4], [9, 1, 5, 3, 4, 2, 6, 8, 7], [2, 5, 6, 4, 7, 3, 8, 9, 1], [3, 4, 9, 8, 5, 1, 7, 2, 6], [8, 7, 1, 9, 2, 6, 3, 4, 5], [1, 3, 2, 6, 8, 5, 4, 7, 9], [5, 9, 8, 7, 3, 4, 1, 6, 2], [7, 6, 4, 2, 1, 9, 5, 3, 8]]
    assert solve_sudoku_unique(grid3,0,0)== True
    assert grid3==[[9, 4, 6, 1, 5, 7, 8, 2, 3], [1, 2, 8, 3, 9, 6, 7, 5, 4], [5, 7, 3, 2, 8, 4, 1, 6, 9], [3, 5, 1, 6, 7, 2, 9, 4, 8], [4, 6, 9, 8, 3, 1, 2, 7, 5], [2, 8, 7, 5, 4, 9, 6, 3, 1], [6, 9, 2, 4, 1, 5, 3, 8, 7], [8, 1, 5, 7, 6, 3, 4, 9, 2], [7, 3, 4, 9, 2, 8, 5, 1, 6]]
    assert solve_sudoku_unique(grid4,0,0)== False




