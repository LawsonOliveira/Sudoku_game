###########################################################################################################################################################
######################################################### Import des fonctions ############################################################################
###########################################################################################################################################################

import sys
from pathlib import Path
file = Path(__file__).resolve()
package_root_directory = file.parents[1]
sys.path.append(str(package_root_directory))

from Grid.create_sudoku import create_sudoku
from Grid.Check_solution import check_solutions
from Grid.Display_grids import grid_to_string, display_2_grids
from Grid.Play_a_move import read_player_command, update_grid, check_coord, read_dimension_level
from Grid.Save import save, read
import copy

###########################################################################################################################################################
######################################### Fonctions pour faire tourner le jeu #############################################################################
###########################################################################################################################################################

# Cette fonction commence le jeu
def start_the_game(answer):
    if answer=='oui':                                           # On vérifie si le joueur veut reprendre une partie sauvegardée
        status=read() 
        if status!=True:                                        # On vérifie qu'il y a bien une sauvegarde
            grid_player,grid_init,grid_complete=status
            dim=len(grid_player)
        else:                                                   # Si il n'y a pas de partie sauvegardée, on lance une nouvelle partie
            print("Il n y a pas des sauvegardes! \n")
            dim, level = read_dimension_level()
            grid_complete, grid_init = create_sudoku(dim,level)
            grid_player = copy.deepcopy(grid_init) 
    else:                                                       # Si le joueur ne souhaite pas continuer une partie sauvegarder, on lance une nouvelle partie
        dim, level = read_dimension_level()
        grid_complete, grid_init = create_sudoku(dim,level)
        grid_player = copy.deepcopy(grid_init) 
    display_2_grids(copy.deepcopy(grid_init),copy.deepcopy(grid_player))
    return grid_player,grid_init, grid_complete

# Cette fonction est une boucle pour permettre jouer et mettre des chiffres sur la grille
def  game(grid_player,grid_init,grid_complete):
    while not check_solutions(grid_player):
        move=read_player_command(grid_init)
        coord_possibles=check_coord(grid_init)
        if move=='s':                                           # Si le joueur souhaite sauvegarder et quitter sa partie
            save(grid_player,grid_init,grid_complete)
            return
        elif gameover(move,grid_complete):                      # Si le joueur souhaite abandonner et regarder la solution
            return
        elif move!='a' and move!='s':
            if (move[1],move[2]) in coord_possibles:
                grid_player=update_grid(grid_player,move)
                display_2_grids(copy.deepcopy(grid_init),copy.deepcopy(grid_player))
            else:
                print("Ce n'est pas possible modifier un caractère initial du jeu")
    print("Vous avez gagné")
    return

# Cette fonction vérifie la condition de gameover
def gameover(move,grid_complete):
    dim=len(grid_complete)
    if move == 'a':                              # Si le joueur abandonne, le jeu se termine et on montre la solution
        print("\n \nGameover")
        print("\n"+(dim//2)*"   "+"   Solution"+(dim//2)*"   "+"\n",grid_to_string(grid_complete))
        return True
    else:
        return False