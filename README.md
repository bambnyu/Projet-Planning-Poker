# README du projet de jeu de Planning Poker
## Introduction
Ce projet est un jeu de Planning Poker conçu pour un cadre scolaire, offrant une expérience visuelle et interactive simple. Il permet aux joueurs de participer à des sessions de Planning Poker en fournissant ou en créant leurs backlogs, en gérant les votes, les joueurs, le jeu, l'application et les backlogs.

## Structure du projet
Le projet est composé de plusieurs fichiers Python, chacun ayant un rôle spécifique dans l'application:

### Carte.py
Définit la classe `Carte` qui représente une carte à jouer avec des méthodes pour obtenir et définir sa valeur.

### Joueur.py
Définit la classe `Joueur` qui représente un joueur dans le jeu, gérant son nom et sa carte.

### Jeu.py
Définit la classe `Jeu` qui représente le cœur logique du jeu, gérant les joueurs, l'état du jeu et le backlog.

### Visual.py
Définit la classe `Visual` qui gère tous les aspects visuels du jeu, utilisant pygame et tkinter pour l'affichage graphique.

### Board.py
Définit la classe `Board` qui gère l'interface principale du jeu, y compris l'initialisation de la fenêtre de jeu et le cycle de vie du jeu.

### main.py
Point d'entrée pour lancer le jeu. Il crée une instance de `Board` et démarre le jeu.

### test.py
Contient les tests unitaires pour le projet, en utilisant pytest pour valider les composants du jeu.

## Configuration et installation
Assurez-vous que Python est installé sur votre système.
Installez les dépendances nécessaires, notamment [Pygame](https://www.pygame.org/news) et [tkinter](https://wiki.python.org/moin/TkInter) et [numpy](https://numpy.org/).
```
pip install pygame tkinter numpy
```
Clonez le dépôt ou téléchargez les fichiers du projet.
## Utilisation
Pour lancer le jeu, naviguez jusqu'au dossier du projet dans votre terminal (dans le dossier `Code/Classes`) et exécutez:
```
python main.py
```
Suivez les instructions à l'écran pour interagir avec le jeu.

Pour créer des tests unitaire nous avons choisi [pytest](https://docs.pytest.org/en/7.4.x/).
Pour lancer les test naviguez jusqu'au dossier du projet dans votre terminal (dans le dossier `Code/Classes`) et exécutez:
```
type pytest Code/Classes/test.py`
```
Pour lancer un test spécifique exécutez:
```
pytest -k <test name>
```
## En jeu
### Ecran de démarrage
Dans cet écran, vous avez le choix de commencer le jeu, de choisir le type de règles que vous souhaitez adopter ou de quitter le jeu grâce à trois boutons. Cet écran est aussi celui affiché en fin de partie, pour permettre de recommencer une partie si nécessaire.

### Ecran de règles
Dans cet écran vous pouvez choisir le type de règle avec lequel vous souhaitez jouer parmis :
- strictes
- moyenne
- médianne
- majorité absolue
- majorité relative
  
La règle par défaut est la stricte, car elle est la plus couramment utilisée et la plus présentée en cours.

### Ecran de chargement
Dans cet écran, vous pouvez charger un fichier de Backlog si vous en possédez un. Assurez-vous de le placer dans le bon dossier pour que les redirections soient efficaces ainsi que les chargements et enregistrements. Si vous n'en avez pas, vous pourrez entrer votre liste de backlogs dans l'écran suivant (qui ne se déclenche que si aucun fichier de Backlogs n'a été choisi). Pour lancer le jeu avec le bouton start, il faudra d'abord entrer au moins le nom d'un joueur dans l'emplacement prévu à cet effet. Sinon, le jeu refusera de continuer. Une partie de Planning Poker a besoin d'au moins un joueur.

### Ecran de création de Backlogs
Cet écran n'est atteint que si vous n'avez pas fourni de fichier de Backlogs. Vous pourrez y créer vos Backlogs sans difficulté un par un. Une fois fait, vous pourrez cliquer sur le bouton start. Nous sommes censés commencer directement le jeu avec les backlogs écrits, mais malheureusement, un bug inconnu nous renvoie à l'écran de démarrage. Les backlogs sont bien enregistrés dans le fichier `Code/Backlogs/backlog.json` et sont donc accessibles si, en lançant le jeu, vous ouvrez ce fichier de backlog pour jouer.

### Ecran de vote Joueur
Nous allons parcourir le fichier de Backlogs et afficher la première tâche sans difficulté. Si il n'y en a pas, le jeu est fini et on retourne vers l'écran de démarrage. Chaque joueur sera annoncé pour chaque tâche et pourra voter chacun son tour à la valeur qui lui semble juste.

### Ecran de vote Résultat
Une fois tous les votes effectués, ils sont affichés pour permettre aux joueurs de voir les difficultés. Au besoin (règles strictes), un nouveau round pour la tâche est relancé. Une fois fait, un nouveau round est lancé sur la tâche suivante. Quand toutes les tâches sont passées, le fichier est enregistré dans `Code/Backlogs/backlog.json` et vous pouvez y accéder comme vous le voulez. Puis, vous êtes redirigés vers l'écran de démarrage.

#### le ?
Si un vote `?` est fait, le vote est sauté et on passe à la tâche suivante.
#### le cafe
Si un vote `cafe` est fait, on enregistre les anciens backlogs et on quitte la partie. Qui pourra être reprise plus tard si on rouvre le fichier.


Contribution
Les contributions sont actuellement bloquées car il s'agit d'un projet scolaire. Elles pourront être ouvertes suite à l'évaluation. Dans ce cas, veuillez suivre les conventions de codage standard et fournir des tests pour les nouvelles fonctionnalités.


