# Sudoku_game_by_Team6

# Projet des Coding Weeks de l'équipe TeamSix

# Description 

Création d'un jeu de sudoku dans le cadre de la 2ème semaine des Coding Weeks

# Membres de l'équipe : 
- Jean Goepfert
- Gweltaz Pocher
- Benjamin Boutier
- Rémi Forasetto
- Marouane El Ouarraq
- Oliveira Lima Lawson

# Projet : Codage d'un jeu de sudoku

But du jeu : L'objectif est de remplir la grille, de manière à ce que chaque ligne, chaque colonne et chaque case ne comporte qu'une fois chaque caractère.

Avancée du projet : Nous avons créé deux versions du jeu, un MVP qui se joue depuis le terminal, et une version avec interface graphique pygame, qui peut se jouer avec le clavier et la souris.

###########################################################################################################

# Voici les modules qu'il est nécessaire d'importer pour pouvoir jouer au Sudoku

# Installer pygame

Placez vous dans le terminal et rentrez la commande _pip3 install pygame_

# Utilisation du MVP

Se placer dans le fichier sudoku_game_by_team6/Sudoku_MVP_lignes_de_commande.py et l'exécuter.

Vous aurez le choix entre reprendre une partie sauvegardée et une nouvelle partie. Vous aurez aussi la possibilité de choisir le niveau de difficulté de la grille, ainsi que les dimensions de celle-ci. Une fois la grille affichée, vous pourrez remplir une case en rentrant sa valeur dans le terminal, ainsi que ses coordonnées. Vous pouvez à tout moment sauvegarder et quitter la partie, ou simplement abandonner. Si vous abandonnez, la solution de la grille s'affichera dans le terminal.


###########################################################################################################

# Utilisation du jeu avec interface graphique

Se placer dans le fichier sudoku_game_by_team6/main.py et l'exécuter.

Vous aurez le choix entre 3 niveaux de difficulté.
Ensuite la grille s'affiche. Vous pouvez mettre la partie en pause, quitter la partie, ou encore révéler une case de votre choix. Pour ce faire, placer vous sur la case voulue et cliquer sur l'icône lampe. Vous avez aussi la possibilité de rentrer les candidats possibles sur une case. Il faut cliquer sur l'icône crayon, puis cliquer sur la case et taper les valeurs au clavier.

Pour jouer, il suffit de cliquer sur la case et de rentrer la valeur choisie sur le clavier. (Attention, le clavier numérique ne marche cependant pas).

Un chronomètre vous indiquera le temps de jeu.

Une musique de fond se lance au début de la partie. Si vous souhaitez la désactiver, cliquez sur l'icône "note de musique".

Une fois la partie finie, vous pouvez afficher la solution avec le bouton "révéler". Vous pourrez ensuite commencer une nouvelle partie.

###########################################################################################################

# Organisation des fichiers et modules

- Lien_des_videos_et_organisation_du_projet : ce dossier contient des observations sur notre avancement, jalons, sprints et les liens des videos sur YouTube

- Sudoku : ce dossier contient les codes de notre projet
    - Data : ce dossier contient les donnés et images utilisées

    - Game_Sudoku : ce dossier contient les fonctions pour exécuter le MVP
        - Game : il contient les fonctions pour touner le jeu
        - Launch_the_game_MVP : il serve pour éxecuter le MVP sur le VisualStudio
            
        - Grid : ce dossier contient les fonctions pour générer grilles avec solutions uniques et les afficher sur le terminal
            - Check_solution.py : ce module contient les fonctions que sont utilisées pour vérifier si la grille complète est une solution
            - create_sudoku.py : ce module est utilisé pour générer des grilles sudoku complètes et ensuite effacer ses chiffres de façon qu'il existe seuelement une solution possible (On utilise le solveur qu'on a fait pour garantir cela)
            - Display_grids.py : ce module est utilisé pour afficher le jeu sur le terminal
            - Play_a_move.py : ce module est utilisé pour lire des entrées sur le clavier
            - Save.py : ce module est utilisé afin de ce que soit possible l'utilisateur faire des sauvegardes

        - Interface_graphique : ce dossier contient les fonctions pour jouer sur une interface graphique
            - Display_pygame_mac.py : il permet d'utiliser l'interface graphique sur le Mac
            - Display_pygame_windows.py : il permet d'utiliser l'interface graphique sur le Windows

        - Solve_sudoku : ce dossier contient le solveur qu'on a fait
            - Solve_backtracking : ce module contient notre solveur lequel est utilisée dans le module create_grid pour garantir que la grille a une unique solution
            c'est aussi utilisé pour suggérer des chiffres sur l'interface graphique.

        - Tests : ce dossier contient tous les tests qu'on a faits
            - html.cov : il contient le fichier index.html . lequel ont les résultats du test de couverture
            - test_Check_solution.py : il contient les fonctions test qu'on a fait pour le module Check_solution
            - test_create_sudoku.py : il contient les fonctions test qu'on a fait pour le module create_sudoku
            - test_Play_a_move.py : il contient les fonctions test qu'on a fait pour le module Play_a_move
            - test_solve_sudoku.py : il contient les fonctions test qu'on a fait pour le module Solve_sudoku/Solve_backtracking


###########################################################################################################

# Nos points fortes
    - Un générateur de grilles avec solution unique
    - Un solveur qui peut résoudre de façon très vite toutes les grilles
    - Une interface graphique simple et intuitive


###########################################################################################################

# Suggestions pour améliorer notre projet à l'avenir
    - Ajouter le sauvegarde à l'interface graphique
    - Ajouter un bouton pour annuler un mouvement
    - Ajouter des modes de jeu pour grilles 16x16 et 25x25
