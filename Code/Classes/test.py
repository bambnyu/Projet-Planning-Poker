from Board import *

# Fichier en français pour plus de clarté car etape importante du projet dans un cours en français (et non en anglais) malgré le fait que le reste du code soit en anglais pour des raisons de convention
# File in french for more clarity because it is an important step of the project in a french course (and not an english one) despite the fact that the rest of the code is in english for convention reasons

# Gestion des tests unitaires avec pytest
# pip install pytest
# pour le lancez, tapez pytest Classes/Test/test.py dans le terminal
# pour lancer un test spécifique, tapez pytest -k <nom du test> dans le terminal

# Unit tests management with pytest
# pip install pytest
# to launch it, type pytest Classes/Test/test.py in the terminal
# to launch a specific test, type pytest -k <test name> in the terminal




### Tests unitaires

# Test de la classe Carte
def test_création_carte():
    """Test de la classe Carte"""
    # Création d'une carte
    carte = Carte(1)
    # Vérification des attributs
    assert carte.get_valeur() == 1

# Test de la classe Joueur
def test_création_joueur():
    """test de la classe Joueur"""
    # Création d'un joueur
    joueur = Joueur("Bob")
    # Vérification des attributs
    assert joueur.get_nom() == "Bob"
    assert joueur.get_carte() == "Aucune"
    # Vérification de la méthode set_carte
    carte = Carte("1")
    joueur.set_carte(carte)
    print(joueur.get_carte())
    print(carte.get_valeur())
    assert joueur.get_carte().get_valeur() == carte.get_valeur()
    # Vérification de la méthode get_nom
    assert joueur.get_nom() == "Bob"


# Test de la classe Jeu
def test_création_jeu():
    """test de la classe Jeu"""
    # Création d'un jeu
    jeu = Jeu()
    # Vérification des attributs
    assert jeu.joueurs == []
    assert jeu.backlogs == []
    # Vérification de la méthode ajouter_joueur
    jeu.ajouter_joueur(Joueur("Alice"))
    assert jeu.joueurs[0].get_nom() == "Alice"
    jeu.ajouter_joueur(Joueur("Bob"))
    assert jeu.joueurs[1].get_nom() == "Bob"
    # Vérification de la get_joueurs
    assert jeu.get_joueurs() == ["Alice", "Bob"]
    # Vérification de la méthode get_joueur_actif
    assert jeu.get_joueur_actif() == 1
    # Vérification de la méthode set_joueur_actif
    jeu.set_joueur_actif(2)
    assert jeu.get_joueur_actif() == 2
    # Vérification de la méthode get_backlogs (vide)
    assert jeu.get_backlogs() == []
    # Vérification de la méthode ajouter_backlog
    jeu.ajouter_backlog("description")
    assert jeu.backlogs[0]['description'] == "description"
    # Vérification de la méthode get_backlogs (non vide)
    assert jeu.get_backlogs() == jeu.backlogs
    # Vérification de la méthode charger_backlog
    jeu.charger_backlog("Code/Backlogs/backlog.json")
    assert jeu.backlogs[0]['difficulty'] == "2"
    # Vérification de la méthode enregistrer_backlog
    jeu.enregistrer_backlog("Code/Backlogs/backlog.json")
    jeu.charger_backlog("Code/Backlogs/backlog.json")
    assert jeu.backlogs[0]['difficulty'] == "2"
    # verification de la méthode enregistrer_backlog_skipped
    jeu.enregistrer_backlog_skipped("Code/Backlogs/backlog.json")
    jeu.charger_backlog("Code/Backlogs/backlog.json")
    assert jeu.backlogs[0]['difficulty'] == "2"
    # Vérification de la méthode set_difficulty_backlog
    jeu.set_difficulty_backlog(None)
    assert jeu.backlogs[1]['difficulty'] == None
    # Vérification de la méthode get_all_votes
    assert jeu.get_all_votes() == ["Aucune", "Aucune"]
    # Vérification de la méthode get_numerical_votes
    assert jeu.get_numerical_votes() == []
    # Vérification de la méthode max_min_votes
    assert jeu.max_min_votes() == (None, None)
    # Vérification de la méthode medianne
    assert jeu.medianne([1,2,3,4,5]) == 3
    # Vérification de la méthode moyenne
    assert jeu.moyenne([1,2,3,4,5,6]) == 4
    
# Test de la classe Visual
def test_visual():
    """test de la classe Visual"""
    # Création d'un jeu
    # Création d'une visualisation
    visual = Visual()
    # Vérification des attributs ecran
    assert visual.main_menu == True
    assert visual.rules_menu == False
    # Vérification des attributs regles
    assert visual.strictes_clicked == True
    assert visual.moyenne_clicked == False
    # Vérification des attributs couleur
    assert visual.WHITE == (255, 255, 255)
    # Vérification des attributs screen
    assert visual.screen_width == 800
    assert visual.screen_height == 600
    # Vérification des attributs boutons
    assert visual.button_width == 200
    assert visual.button_start_x == visual.screen_width/2 - visual.button_width/2
    assert visual.button_gap == 70
    # Vérification des attributs description
    assert visual.description_posX == 3.5*visual.screen_width//5
    # Vérification des methodes difficiles car liées à pygame et à l'affichage
    
# Test de la classe Board
def test_board():
    """test de la classe Board"""
    board = Board()
    # Vérification des attributs
    assert board.visual.jeu.joueurs == []
    assert board.visual.jeu.backlogs == []
    assert board.visual.main_menu == True
    assert board.visual.rules_menu == False
    assert board.visual.strictes_clicked == True
    assert board.visual.moyenne_clicked == False
    assert board.visual.WHITE == (255, 255, 255)
    assert board.visual.screen_width == 800
    assert board.visual.screen_height == 600
    assert board.visual.button_width == 200
    assert board.visual.button_start_x == board.visual.screen_width/2 - board.visual.button_width/2
    assert board.visual.button_gap == 70
    assert board.visual.description_posX == 3.5*board.visual.screen_width//5
    # Vérification des methodes difficiles car liées à pygame et à l'affichage
    
    
    
    
    



# Code by Adjame Tellier-Rozen (ROZEN)