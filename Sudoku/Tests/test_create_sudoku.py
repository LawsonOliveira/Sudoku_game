###########################################################################################################################################################
######################################################### Import des fonctions ############################################################################
###########################################################################################################################################################
import sys
from pathlib import Path
file = Path(__file__).resolve()
package_root_directory = file.parents[1]
sys.path.append(str(package_root_directory))

from Data.Auxiliary_grids.Additional_grids import *
from Data.Auxiliary_grids.Medium_grids import *
from Grid.Check_solution import *
from Grid.create_sudoku import *
from Grid.Display_grids import *


###########################################################################################################################################################
################################################### Test des fonctions de Create_sudoku ###################################################################
###########################################################################################################################################################

# Teste de la fonction qui déplace n éléments á gauche d'une liste
def test_shift():
    global grid_m4
    assert shift(grid_m4[0], 1) == [7, 6, 4, 8, 1, 3, 2, 5, 9]
    assert shift(grid_m4[0], 2) == [6, 4, 8, 1, 3, 2, 5, 9, 7]
    assert shift(grid_m4[1], 3) == [2, 5, 9, 7, 8, 6, 1, 4, 3]
    assert shift(grid_m4[1], 4) == [5, 9, 7, 8, 6, 1, 4, 3, 2]

#Teste de la fonction qui mélange les blocs d'une list
def test_shuffle_sudoku_blocks():
    assert shuffle_sudoku_blocks([[1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3 ,4]] )== [[1, 3, 1, 3], [2, 4, 2, 4], [1, 3, 1, 3], [2, 4, 2, 4]]
    assert shuffle_sudoku_blocks([[1, 2, 3, 4],[4, 5, 6, 7],[1, 2, 3, 4],[4, 5, 6, 7]] )== [[1, 3, 1, 3], [2, 4, 2, 4], [4, 6, 4, 6], [5, 7, 5, 7]]
    assert shuffle_sudoku_blocks([[2, 4, 8, 3],[1, 2, 3, 4],[4, 5, 6, 7],[1, 2, 3, 4]] )== [[2, 8, 4, 6], [4, 3, 5, 7], [1, 3, 1, 3], [2, 4, 2, 4]]

#Teste de la fonction qui mélange les lignes d'une list
def test_shuffle_sudoku_lines():
    assert shuffle_sudoku_lines([[1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3 ,4]] )== [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
    assert shuffle_sudoku_lines([[1, 2, 3, 4],[4, 5, 6, 7],[1, 2, 3, 4],[4, 5, 6, 7]] )== [[4, 5, 6, 7], [1, 2, 3, 4], [4, 5, 6, 7], [1, 2, 3, 4]]
    assert shuffle_sudoku_lines([[2, 4, 8, 3],[1, 2, 3, 4],[4, 5, 6, 7],[1, 2, 3, 4]] )== [[1, 2, 3, 4], [2, 4, 8, 3], [1, 2, 3, 4], [4, 5, 6, 7]]


# Teste de la fonction qui crée une grille complète
def test_create_sudoku_complete():
    assert check_solutions(create_sudoku_complete(9)) == True
    assert check_solutions(create_sudoku_complete(16)) == True
    assert check_solutions(create_sudoku_complete(25)) == True  # grid 25x25


# Teste de la fonction qui crée un grille sudoku complète et une effacée
def test_create_sudoku():
    assert check_solutions(create_sudoku(9,0)[0]) == True
    assert check_solutions(create_sudoku(16,0)[0]) == True
    assert check_solutions(create_sudoku(25,0)[1]) == False  # grid 25x25 avec zeros


# Teste de la fonction qui obtient les positions remplies d'une grille sudoku
def test_get_filled_tiles_positions():
    assert get_filled_tiles_positions(grid_m1) ==[(0, 6), (0, 7), (1, 2), (1, 3), (1, 8), (2, 2), (2, 4), (2, 7), (3, 1), (3, 3), (3, 8), (4, 1), (4, 3), (5, 1), (5, 4), (5, 6), (5, 8), (7, 2), (7, 3), (7, 8), (8, 1), (8, 5), (8, 8)]
    assert get_filled_tiles_positions(grid_m2) ==[(0, 1), (0, 5), (0, 8), (1, 3), (1, 5), (2, 0), (2, 4), (2, 8), (3, 2), (3, 4), (3, 7), (4, 0), (4, 4), (4, 8), (6, 1), (6, 3), (6, 4), (6, 7), (7, 0), (7, 7), (8, 0), (8, 4), (8, 7)]
    assert get_filled_tiles_positions(grid_m3) ==[(0, 4), (0, 5), (0, 7), (1, 0), (1, 3), (1, 4), (1, 5), (1, 6), (2, 2), (3, 1), (3, 2), (3, 5), (3, 6), (3, 8), (4, 0), (5, 0), (5, 1), (5, 4), (5, 5), (5, 6), (5, 7), (6, 4), (6, 8), (8, 0), (8, 1), (8, 2), (8, 4), (8, 6)]


# Teste de la fonction qui obtient une position d'une grille sudoku pour effacer
def test_get_filled_position_to_erase():
    assert get_filled_position_to_erase(grid_m1) in [(0, 6), (0, 7), (1, 2), (1, 3), (1, 8), (2, 2), (2, 4), (2, 7), (3, 1), (3, 3), (3, 8), (4, 1), (4, 3), (5, 1), (5, 4), (5, 6), (5, 8), (7, 2), (7, 3), (7, 8), (8, 1), (8, 5), (8, 8)]
    assert get_filled_position_to_erase(grid_m2) in [(0, 1), (0, 5), (0, 8), (1, 3), (1, 5), (2, 0), (2, 4), (2, 8), (3, 2), (3, 4), (3, 7), (4, 0), (4, 4), (4, 8), (6, 1), (6, 3), (6, 4), (6, 7), (7, 0), (7, 7), (8, 0), (8, 4), (8, 7)]
    assert get_filled_position_to_erase(grid_m3) in [(0, 4), (0, 5), (0, 7), (1, 0), (1, 3), (1, 4), (1, 5), (1, 6), (2, 2), (3, 1), (3, 2), (3, 5), (3, 6), (3, 8), (4, 0), (5, 0), (5, 1), (5, 4), (5, 5), (5, 6), (5, 7), (6, 4), (6, 8), (8, 0), (8, 1), (8, 2), (8, 4), (8, 6)]

