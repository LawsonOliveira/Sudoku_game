###########################################################################################################################################################
######################################################### Import des fonctions ############################################################################
###########################################################################################################################################################

import sys
from pathlib import Path, WindowsPath
file = Path(__file__).resolve()
package_root_directory = file.parents[1]
sys.path.append(str(package_root_directory))

from Sudoku.Interface_graphique.Display_pygame_mac import play_mac
from Sudoku.Interface_graphique.Display_pygame_windows import play_windows

###########################################################################################################################################################
######################################### Fonctions pour faire tourner le jeu #############################################################################
###########################################################################################################################################################



def main():
    operateur = sys.platform

    if operateur == 'win32':
        play_windows()
    elif operateur == 'darwin':
        play_mac()
    
    else:
        print("Votre système d'exploitation n'est pas supporté par notre programme, l'affichage peut ne pas se faire correctement !")
        play_windows()


if __name__ == "__main__":
    main()