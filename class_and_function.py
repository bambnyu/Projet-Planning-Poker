#import
import json


# Création des classes

class Carte:
    """Classe qui représente une carte à jouer"""

    # Attributs
    def __init__(self, valeur, image):
        """Initialise une carte avec une valeur et une image"""
        self.valeur = valeur
        self.image = image # chemin vers l'image

    # Méthodes
    def get_valeur(self):
        """Retourne la valeur de la carte"""
        return self.valeur
    

class Joueur:
    """Classe qui représente un joueur"""

    # Attributs
    def __init__(self, nom):
        """Initialise un joueur avec un nom un emplacement pour une carte et un deck de cartes"""
        self.nom = nom
        self.carte = None
        self.deck = [Carte(valeur, f"images_cartes/cartes_{valeur}.png") for valeur in [0, 1, 2, 3, 5, 8, 13, 20, 40, 100, "interro", "cafe"]] # liste de cartes
        
    # Méthodes
    def set_carte(self, carte):
        """Défini la carte du joueur"""
        self.carte = carte

    def get_nom(self):
        """Retourne le nom du joueur"""
        return self.nom

    def get_carte(self):
        """Retourne la carte du joueur"""
        if self.carte:
            return self.carte.get_valeur()
        else:
            return "Aucune"
        

class Jeu:
    """Classe qui représente le jeu"""

    # Attributs
    def __init__(self):
        """Initialise le jeu avec une liste de joueurs et un backlog initialement vide"""
        self.joueurs = []
        self.backlogs = []

    def get_joueurs(self):
        """Retourne la liste des joueurs"""
        return [joueur.get_nom() for joueur in self.joueurs]

    def ajouter_joueur(self, joueur):
        """Ajoute un joueur à la liste des joueurs"""
        self.joueurs.append(joueur)
    
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
    