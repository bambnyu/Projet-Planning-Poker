#from class_and_function import *

import sys
import os

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from Jeu import *



# Gestion des tests unitaires avec pytest
# pip install pytest
# pour le lancez, tapez pytest Classes/Test/test.py dans le terminal
# pour lancer un test spécifique, tapez pytest -k <nom du test> dans le terminal



### Tests unitaires

# Test de la classe Carte
def test_création_carte():
    """Test de la classe Carte"""
    # Création d'une carte
    carte = Carte(1, "cartes_1.png")
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
    # Vérification du deck
    assert joueur.deck[0].get_valeur() == 0
    assert joueur.deck[0].image == "images_cartes/cartes_0.png"
    # Vérification de la méthode set_carte
    joueur.set_carte(Carte(1, "cartes_1.png"))
    assert joueur.get_carte() == 1
    # Vérification de la méthode get_carte
    assert joueur.get_carte() == 1
    # Vérification de la méthode get_nom
    assert joueur.get_nom() == "Bob"




##! a refaire et la decouper en plusieurs tests unitaires, et certaines fonctions ne sont pas testées

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
    # Vérification de la méthode charger_backlog
    jeu.charger_backlog("Backlogs/backlog.json")
    assert jeu.backlogs['backlogItems'][0]['taskId'] == "1"
    # Vérification de la méthode voter
    jeu.voter(jeu.backlogs['backlogItems'][0])
    assert jeu.backlogs['backlogItems'][0]['difficulty'] == "Aucune"
    # Vérification de la méthode verifier_votes
    assert jeu.verifier_votes() == True
    # Vérification de la méthode voter
    jeu.voter(jeu.backlogs['backlogItems'][0])
    assert jeu.backlogs['backlogItems'][0]['difficulty'] == "Aucune"
    # Vérification de la méthode get_joueurs
    assert jeu.get_joueurs() == ["Alice", "Bob"]
    # Vérification de la méthode get_backlogs
    assert jeu.get_backlogs() == jeu.backlogs



# Code by Adjame Tellier-Rozen (ROZEN)