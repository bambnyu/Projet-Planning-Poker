import json
from Joueur import *
from Regles import *


class Jeu:
    """Classe qui représente le jeu"""

    # Attributs
    def __init__(self):
        """Initialise le jeu avec une liste de joueurs et un backlog initialement vide"""
        self.joueurs = []
        self.backlogs = []
        self.joueur_actif = 1

    def get_joueurs(self):
        """Retourne la liste des joueurs"""
        return [joueur.get_nom() for joueur in self.joueurs]

    def ajouter_joueur(self, joueur):
        """Ajoute un joueur à la liste des joueurs"""
        self.joueurs.append(joueur)
    
    def get_joueur_actif(self):
        """Retourne le joueur actif"""
        return self.joueur_actif
    def set_joueur_actif(self, value):
        """Définit le joueur actif"""
        self.joueur_actif = value

    def get_backlogs(self):
        """Retourne le backlog"""
        return self.backlogs

    def charger_backlog(self, fichier):
        """Charge le backlog depuis un fichier json"""
        with open(fichier, 'r') as f:
            self.backlogs = json.load(f)

    def voter(self, backlog_item):
        """Permet aux joueurs de voter pour un item du backlog"""
        print(f"Vote pour l'item du backlog : {backlog_item}")
        for joueur in self.joueurs:
            print(joueur.get_nom(), "a voté : ", joueur.get_carte())
        if self.verifier_votes():
            backlog_item['difficulty'] = self.joueurs[0].get_carte() # on enregistre la valeur validée par les joueurs
        else:
            print("Les votes ne sont pas unanimes, on ne peut pas valider la valeur")
            

    def verifier_votes(self):
        """Vérifie que les votes des joueurs sont unanimes"""
        precedent = None # valeur de la carte du joueur précédent dans la liste 
        for joueur in self.joueurs: # on parcourt la liste des joueurs
            if precedent and joueur.get_carte() != precedent:
                return False
            precedent = joueur.get_carte() # on met à jour la valeur de la carte précédente
        return True
    
    def enregistrer_backlog(self, fichier): 
        """Enregistre le backlog dans un fichier json"""
        with open(fichier, 'w') as f:
            json.dump(self.backlogs, f)
        
    def afficher_backlog(self):
        """Affiche le backlog"""
        if self.backlogs['backlogItems']['difficulty'] != 'null':
            print("Pour la tache ",self.backlogs['backlogItems']['description'], " la valeur est ", self.backlogs['backlogItems']['difficulty'])
        else : 
            print("Pour la tache ",self.backlogs['backlogItems']['description'], " la valeur est a determiner")
    
    def afficher_1_backlog(self, i):
        """Renvoie le backlog"""
        return ("Pour la tache : " + self.backlogs[i]['description'])
    
    def ajouter_backlog(self, description):
        """Ajoute un backlog"""
        """Ajoute un backlog avec une description donnée."""
        # Créer un nouvel élément de backlog
        new_backlog_item = {
            "description": description,
            "difficulty": None  # ou toute autre valeur initiale par défaut
        }

        # Ajouter cet élément à la liste des backlogs
        self.backlogs.append(new_backlog_item)
        
    def set_difficulty_backlog(self, difficulty):
        """Définit la difficulté d'un backlog du premier backlog sans difficulté"""
        for backlog in self.backlogs:
            if backlog['difficulty'] == None:
                backlog['difficulty'] = difficulty
                break
        
    def medianne(self, liste):
        """Calcule la médiane d'une liste de valeurs"""
        liste.sort()
        if len(liste) % 2 == 0:
            return (liste[len(liste) // 2] + liste[len(liste) // 2 - 1]) / 2
        else:
            return liste[len(liste) // 2]
