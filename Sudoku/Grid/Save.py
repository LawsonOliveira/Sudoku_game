###########################################################################################################################################################
######################################################### Import des fonctions ############################################################################
###########################################################################################################################################################

import shelve

###########################################################################################################################################################
############################################# Fonctions pour sauvegarder et lire une partie ###############################################################
###########################################################################################################################################################

# Cette fonction faire une sauvegarde du jeu
def save(grid_player,grid_init,grid_complete):
    data=shelve.open("./save_file.txt")                         # On crée un fichier dans lequel on écrit la grille initiale, la grille du joueur et la solution
    data["grid_player"]=grid_player
    data["grid_init"]=grid_init
    data["grid_complete"]=grid_complete
    print("Le jeu a été sauvé.\n Merci !")
    data.close()
    return

# Cette fonction lire la sauvegarde du jeu
def read():
    data=shelve.open("./save_file.txt")
    if "grid_player" in data.keys():                            # Si une partie est sauvegardée, on récupère la grille initiale, la grille du joueur et la solution
        grid_player=data["grid_player"]
        grid_init=data["grid_init"]
        grid_complete=data["grid_complete"]
        data.close()
        return  grid_player,grid_init,grid_complete 
    else:                                                       # Fichier vide
        data.close()
        return True









