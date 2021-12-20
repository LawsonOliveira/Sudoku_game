###########################################################################################################################################################
######################################################### Import des fonctions ############################################################################
###########################################################################################################################################################
from math import sqrt
import copy



###########################################################################################################################################################
###################################### Fonctions permettant l'affichage de grilles dans le terminal #######################################################
###########################################################################################################################################################

# Cette fonction affiche une grille n x n sur le terminal
def grid_to_string(grid):
    dim=len(grid)                                                                                   # Obtient la dimension de la grille principale
    dim_sub=int(sqrt(dim))                                                                          # Obtient la dimension des sous-grilles
    grid_str=converte_to_theme(grid)[0]                                                             # Convertit la grille pour le thème choisi
    display="---"+" --- "*(dim-dim_sub+1)
    for i in range(dim):
        if i in list(range(dim_sub-1,dim-dim_sub,dim_sub)):
            l="|"
            for j in range(dim):
                if j in list(range(dim_sub-1,dim-dim_sub,dim_sub)):
                    if grid_str[i][j]==0:
                        l+="   ||"                                                                  # Affiche des espaces blancs
                    else:
                        l+=" "+grid_str[i][j]+" ||"                                                 # Affiche les caractères
                else:
                    if grid_str[i][j]==0:
                        l+="   |"                                                                   # Affiche des espaces blancs
                    else:
                        l+=" "+grid_str[i][j]+" |"                                                  # Affiche les caractères
                      
            display+="\n"+l+"\n"+(" ==="*(dim_sub-1)+" === ")*dim_sub
        else:
            l="|"
            for j in range(dim):
                if j in list(range(dim_sub-1,dim-dim_sub,dim_sub)):
                    if grid_str[i][j]==0:
                        l+="   ||"                                                                  # Affiche des espaces blancs
                    else:
                        l+=" "+grid_str[i][j]+" ||"                                                 # Affiche les caractères
                else:
                    if grid_str[i][j]==0:                                                           # Affiche des espaces blancs
                        l+="   |"    
                    else:
                        l+=" "+grid_str[i][j]+" |"                                                  # Affiche les caractères
            display+="\n"+l+"\n"+(" ---"*(dim_sub-1)+" --- ")*dim_sub
    return display


# Cette fonction affiche deux grilles, la grid_init au-dessous et la grid_player au-dessus. 
def display_2_grids(grid_init,grid_player):
    dim=len(grid_init)
    print("\n"+(dim//2)*"   "+" Grille initiale"+(dim//2)*"   "+"\n",grid_to_string(grid_init))     # Affiche la grille initiale
    print("\n"+(dim//2)*"   "+" Votre grille"+(dim//2)*"   "+"\n",grid_to_string(grid_player))      # Affiche la grille du joueur
    return None

# Donne le thème de la grille en fonction de sa taille, modifie la grille qui doit être affichée et crée une chaine de caractères avec les caractères pouvant être joués
def converte_to_theme(grid):
    grid=copy.deepcopy(grid)
    dim=len(grid)
    if dim==9:
        themes={0:0,1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9'}                                                         # Thème base décimale
    elif dim==16:
        themes={0:0,1:'0',2:'1',3:'2',4:'3',5:'4',6:'5',7:'6',8:'7',9:'8',10:'9',11:'A',12:'B',13:'C',14:'D',15:'E',16:'F' }       # Thème base hexadécimale
    elif dim==25:
        themes={0:0,1:'A',2:'B',3:'C',4:'D',5:'E',6:'F',7:'G',8:'H',9:'I',10:'J',11:'K',12:'L',13:'M',14:'N',15:'O',16:'P',17:'Q',18:'R',19:'S',20:'T',21:'U',22:'V',23:'W',24:'X',25:'Y' }  #Thème alphabet     
    possible_carac=''                                                                                                               # Caractères possibles pour l'utilisateur
    for i in range(dim):
        for j in range(dim):
            grid[i][j]=themes[grid[i][j]]                                                                                           # Convertit la grille pour le thème choisi
        if i<dim-1:
            possible_carac+=themes[i+1]+", "
        else:
            possible_carac+=themes[dim]
    return grid,possible_carac,themes


