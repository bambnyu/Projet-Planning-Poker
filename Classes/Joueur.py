from Carte import *

class Joueur:
    """Class that represents a player"""

    # Attributes
    def __init__(self, nom):
        """Initializes a player with a name and a card"""
        self.nom = nom
        self.carte = Carte("Aucune", "Aucune")
        
    # Methods
    def set_carte(self, carte):
        """Sets the player's card"""
        self.carte.set_valeur(carte)

    def get_nom(self):
        """Returns the player's name"""
        return self.nom

    def get_carte(self):
        """Returns the player's card"""
        if self.carte:
            return self.carte.get_valeur()
        else:
            return "Aucune"
        
# Code by Adjame Tellier-Rozen (ROZEN)