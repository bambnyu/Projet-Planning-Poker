from Carte import *

class Joueur:
    """Classe qui représente un joueur"""

    # Attributs
    def __init__(self, nom):
        """Initialise un joueur avec un nom un emplacement pour une carte et un deck de cartes"""
        self.nom = nom
        self.carte = Carte("Aucune", "Aucune")
        
    # Méthodes
    def set_carte(self, carte):
        """Défini la carte du joueur"""
        self.carte.set_valeur(carte)

    def get_nom(self):
        """Retourne le nom du joueur"""
        return self.nom

    def get_carte(self):
        """Retourne la carte du joueur"""
        if self.carte:
            return self.carte.get_valeur()
        else:
            return "Aucune"