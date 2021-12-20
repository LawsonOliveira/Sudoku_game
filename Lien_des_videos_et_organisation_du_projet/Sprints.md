Objectif 1 (MVP): Un sudoku minimum, sans interface graphique :

 - Sprint 1: Création de projet
	- Créer un dépôt gitlab
	- Tous les membres doivent faire un clone local et créer un projet VisualStudioCode associé

 - Sprint 2: Analyse des besoins et réflexion autour de la conception				
	- Identifier les principaux besoins des utilisateurs 
		- Divertissement de qualité et intuitive
		- Jouer et pouvoir visualiser la solution
		- La possibilité d'effacer des chiffres sur une grille
	- Identifier les différents utilisateurs du produit
		- Les gens qui aiment réfléchir sur des problèmes de logique
		- Les gens qui aiment un jeu interative
		- Les gens qui cherchent une interface jolie et facille
	- Décider comment on va faire le projet
		- C'est expliqué sur les sprints prochaines

 - Sprint 3: Mise en place des données du jeu - Lawson et Gweltaz --> Status: Terminé
	- Fonctionnalité 1 : Générer des grilles de sudoku avec leur solution
	- Fonctionnalité 2 : Représenter une grille de départ en python de taille 9x9 (en base décimale), 16x16 (en base hexadécimale) ou 25x25 (avec l'alphabet)
	- Fonctionnalité 3 : Afficher la grille dans le terminal

 - Sprint 4: Action des joueurs - Rémi et Marouane --> Status: Terminé
	- Fonctionnalité 4 : Donner une instruction de jeu
	- Fonctionnalité 5 : Tester la fin du jeu
	- Fonctionnalité 6 : Faire jouer le joueur (on peut lancer une démo en ligne de commande)

Objectif 2 : Un sudoku avec une interface graphique (Amélioration du MVP) :

 - Sprint 5: Création de l'interface graphique - Benjamin et Jean --> Status: Terminé 
	- Fonctionnalité 7 : Afficher une grille avec pygame
	- Fonctionnalité 8 : Permettre la configuration du jeu via l'interface graphique

Objectif 3 : Un sudoku avec des paramètres optionnels :

 - Sprint 6 : Ajout de paramètres supplémentaires - Benjamin et Jean --> Status: Terminé
	- Fonctionnalité 9 : Ajouter un timer
	- Fonctionnalité 10 : Ajouter des petites notes dans les cases pour aider le joueur

 - Sprint 7 : Création d'un solver numérique de sudoku -  Rémi et Marouane --> Status: Terminé
	- Fonctionnalité 11 : Coder le solver
	- Fonctionnalité 12 : Utilisation du solver pour donner des indices au joueur

 - Sprint 8 : Sauvegarde du jeu MVP en cours - Lawson et Gweltaz --> Status: Terminé
	- Fonctionnalité 13 : Rendre possible enregistrez le jeu MVP afin que l'utilisateur puisse jouer à un autre moment