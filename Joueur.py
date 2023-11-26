from Carte import *

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