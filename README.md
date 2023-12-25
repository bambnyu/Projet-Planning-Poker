# README du projet de jeu de planification de poker
## Introduction
Ce projet est un jeu de Planning Poker dans un cadre scolaire, conçu pour fournir une expérience visuelle et interactive simple.
Le jeu permet aux joueurs de participer à des sessions de Planning Poker en fournissant ou en créant ses Backlogs
en gérant des votes, les joueurs, le jeu, l'application et les backlogs.

## Structure du projet
Le projet est composé de plusieurs fichiers Python, chacun ayant un rôle spécifique dans l'application:

### Carte.py
Définit la classe Carte qui représente une carte à jouer avec des méthodes pour obtenir et définir sa valeur.

### Joueur.py
Définit la classe Joueur qui représente un joueur dans le jeu, gérant son nom et sa carte.

### Jeu.py
Définit la classe Jeu qui représente le cœur logique du jeu, gérant les joueurs, l'état du jeu et le backlog.

### Visual.py
Définit la classe Visual qui gère tous les aspects visuels du jeu, utilisant pygame et tkinter pour l'affichage graphique.

### Board.py
Définit la classe Board qui gère l'interface principale du jeu, y compris l'initialisation de la fenêtre de jeu et le cycle de vie du jeu.

### main.py
Point d'entrée pour lancer le jeu. Il crée une instance de Board et démarre le jeu.

### test.py
Contient les tests unitaires pour le projet, en utilisant pytest pour valider les composants du jeu.

## Configuration et installation
Assurez-vous que Python est installé sur votre système.
Installez les dépendances nécessaires, notamment pygame et tkinter.
`pip install pygame`
`pip install tkinter`
`pip install numpy`
Clonez le dépôt ou téléchargez les fichiers du projet.
Utilisation
Pour lancer le jeu, naviguez jusqu'au dossier du projet dans votre terminal (dans le dossier Code/Classes) et exécutez:
`python main.py`
Suivez les instructions à l'écran pour interagir avec le jeu.

Pour lancer les test unitaires naviguez jusqu'au dossier du projet dans votre terminal (dans le dossier Code/Classes) et exécutez:
`type pytest Code/Classes/test.py`
Pour lancer un test spécifique exécutez:
`pytest -k <test name>`

Contribution
Les contributions sont actuellement bloquées car il s'agit d'un projet scolaire. Les contributions pourront être ouverte suite à l'évaluation
et dans ce cas veuillez suivre les conventions de codage standard et fournir des tests pour les nouvelles fonctionnalités.
