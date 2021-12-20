###########################################################################################################################################################
######################################################### Import des fonctions ############################################################################
###########################################################################################################################################################
import sys
from pathlib import Path
file = Path(__file__).resolve()
package_root_directory = file.parents[1]
sys.path.append(str(package_root_directory))

from Grid.Check_solution import *
from Data.Auxiliary_grids.Additional_grids import *


###########################################################################################################################################################
################################################### Test des fonctions de Check_solution ###################################################################
###########################################################################################################################################################

# Ici on fait le test pour transformer une grille en une sous-grille
def test_grid_to_subgrid():
    global grid_e1
    global grid_e2
    global grid_e3
    global grid_e4
    global grid_m4
    assert grid_to_subgrid(grid_e1) == [[1, 2, 3, 2, 3, 4, 3, 4, 5],
                                        [4, 5, 6, 5, 6, 7, 6, 7, 8],
                                        [7, 8, 9, 8, 9, 1, 9, 1, 2],
                                        [4, 5, 6, 5, 6, 7, 6, 7, 8],
                                        [7, 8, 9, 8, 9, 1, 9, 1, 2],
                                        [1, 2, 3, 2, 3, 4, 3, 4, 5],
                                        [7, 8, 9, 8, 9, 1, 9, 1, 2],
                                        [1, 2, 3, 2, 3, 4, 3, 4, 5],
                                        [4, 5, 6, 5, 6, 7, 6, 7, 8]]

    assert grid_to_subgrid(grid_e2) == [[1, 2, 3, 2, 3, 4, 3, 4, 5],
                                        [4, 5, 6, 5, 6, 7, 6, 7, 8],
                                        [7, 8, 9, 8, 9, 1, 9, 1, 2],
                                        [4, 5, 6, 5, 6, 7, 9, 7, 8],
                                        [7, 8, 9, 8, 9, 1, 6, 1, 3],
                                        [1, 2, 3, 2, 3, 4, 2, 4, 5],
                                        [7, 8, 9, 8, 9, 1, 9, 1, 2],
                                        [1, 2, 3, 2, 3, 4, 3, 4, 5],
                                        [4, 5, 6, 5, 6, 7, 6, 7, 8]]

    assert grid_to_subgrid(grid_e3) == [[9, 7, 6, 2, 4, 3, 5, 1, 8],
                                        [4, 8, 1, 2, 5, 9, 3, 7, 6],
                                        [3, 2, 5, 7, 8, 6, 1, 9, 4],
                                        [6, 9, 4, 8, 1, 2, 7, 3, 5],
                                        [5, 1, 8, 7, 3, 4, 9, 6, 2],
                                        [2, 3, 7, 5, 6, 9, 4, 1, 8],
                                        [4, 6, 7, 2, 5, 1, 3, 8, 9],
                                        [8, 2, 3, 6, 9, 7, 1, 4, 5],
                                        [9, 5, 1, 8, 4, 3, 6, 7, 2]]
                                        
    assert grid_to_subgrid(grid_m4) == [[9, 7, 6, 1, 4, 3, 5, 2, 8],
                                        [4, 8, 1, 2, 5, 9, 3, 7, 6],
                                        [3, 2, 5, 7, 8, 6, 1, 9, 4],
                                        [6, 9, 4, 8, 1, 2, 7, 3, 5],
                                        [5, 1, 8, 7, 3, 4, 9, 6, 2],
                                        [2, 3, 7, 5, 6, 9, 4, 1, 8],
                                        [4, 6, 7, 2, 5, 1, 3, 8, 9],
                                        [8, 2, 3, 6, 9, 7, 1, 4, 5],
                                        [9, 5, 1, 8, 4, 3, 6, 7, 2]]

    assert grid_to_subgrid(grid_e4) ==  [[9, 7, 6, 1, 4, 1, 4, 2, 8], 
                                        [4, 8, 1, 4, 5, 6, 3, 7, 6],
                                        [3, 2, 5, 7, 8, 6, 1, 9, 4],
                                        [6, 9, 4, 8, 1, 2, 7, 3, 5],
                                        [5, 1, 8, 7, 3, 4, 9, 6, 2],
                                        [2, 3, 7, 5, 6, 9, 4, 1, 8],
                                        [4, 6, 4, 2, 5, 1, 3, 8, 9],
                                        [8, 2, 3, 6, 9, 7, 1, 4, 5],
                                        [9, 5, 1, 8, 4, 3, 6, 3, 2]]



# Ici on fait le test pour transformer une sous-grille en une grille
def test_subgrid_to_grid():
    global grid_e1
    global grid_e2
    global grid_e3
    assert subgrid_to_grid(grid_to_subgrid(grid_e1)) == grid_e1
    assert subgrid_to_grid(grid_to_subgrid(grid_e2)) == grid_e2
    assert subgrid_to_grid(grid_to_subgrid(grid_e3)) == grid_e3


# Ici on fait le test pour vérifier si les lignes de la grille sont une solution du Sudoku
def test_check_line():
    global grid_e1
    global grid_e2
    global grid_e3
    global grid_e4
    global grid_m4
    assert check_line(grid_e1)==(True, {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: []})
    assert check_line(grid_e2)==(True, {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: []})
    assert check_line(grid_e3)==(False, {0: [], 1: [2], 2: [1], 3: [], 4: [], 5: [], 6: [], 7: [], 8: []})
    assert check_line(grid_e4)==(False, {0: [], 1: [6, 4, 1], 2: [4], 3: [], 4: [], 5: [], 6: [4], 7: [], 8: [3]})
    assert check_line(grid_m4)==(True, {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: []})


# Ici on fait le test pour vérifier si les colonnes de la grille sont une solution du Sudoku
def test_check_column():
    global grid_e1
    global grid_e2
    global grid_e3
    global grid_e4
    global grid_m4
    assert check_column(grid_e1)==(True, {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: []})
    assert check_column(grid_e2)==(False, {0: [9], 1: [], 2: [], 3: [6], 4: [], 5: [3], 6: [2], 7: [], 8: []})
    assert check_column(grid_e3)==(False, {0: [2], 1: [1], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: []})
    assert check_column(grid_e4)==(False, {0: [4], 1: [], 2: [1, 4], 3: [4], 4: [], 5: [6], 6: [], 7: [3], 8: []})
    assert check_column(grid_m4)==(True, {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: []})


# Ici on fait le test pour vérifier si les sous-grilles de la grille sont une solution du Sudoku
def test_check_subgrid():
    global grid_e1
    global grid_e2
    global grid_e3
    global grid_e4
    global grid_m4
    assert check_subgrid(grid_e1)==(False, {0: [4, 3, 3, 2], 1: [7, 6, 6, 5], 2: [1, 9, 9, 8], 3: [7, 6, 6, 5], 4: [1, 9, 9, 8], 5: [4, 3, 3, 2], 6: [1, 9, 9, 8], 7: [4, 3, 3, 2], 8: [7, 6, 6, 5]})
    assert check_subgrid(grid_e2)==(False, {0: [4, 3, 3, 2], 1: [7, 6, 6, 5], 2: [1, 9, 9, 8], 3: [7, 6, 5], 4: [1, 9, 8], 5: [4, 2, 3, 2], 6: [1, 9, 9, 8], 7: [4, 3, 3, 2], 8: [7, 6, 6, 5]})
    assert check_subgrid(grid_e3)==(True, {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: []})
    assert check_subgrid(grid_e4)==(False, {0: [4, 1], 1: [6, 4], 2: [], 3: [], 4: [], 5: [], 6: [4], 7: [], 8: [3]})
    assert check_subgrid(grid_m4)==(True, {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: []})


# Ici on fait le test pour vérifier si la grille est une solution du Sudoku
def test_check_solutions():
    global grid_e1
    global grid_e2
    global grid_e3
    global grid_e4
    global grid_m4
    assert check_solutions(grid_e1)==False
    assert check_solutions(grid_e2)==False
    assert check_solutions(grid_e3)==False
    assert check_solutions(grid_e4)==False
    assert check_solutions(grid_m4)==True