###########################################################################################################################################################
######################################################### Import des fonctions ############################################################################
###########################################################################################################################################################

import sys
from pathlib import Path
file = Path(__file__).resolve()
package_root_directory = file.parents[1]
sys.path.append(str(package_root_directory))

from Game_Sudoku.Game import start_the_game, game
###########################################################################################################################################################
######################################### Fonctions pour faire tourner le jeu #############################################################################
###########################################################################################################################################################


#Permet de lancer le jeu
def game_MVP():
    answer=' '
    while answer not in ['oui','non']:
        answer=input("Voulez-vous commencer à partir d'une sauvegarde ? (oui ou non) : ")
    grid_player,grid_init,grid_complete=start_the_game(answer)
    game(grid_player,grid_init,grid_complete)
    return

game_MVP()

