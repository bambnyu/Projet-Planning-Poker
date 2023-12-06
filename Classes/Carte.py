
class Carte:
    """Classe qui représente une carte à jouer"""

    # Attributs
    def __init__(self, valeur, image):
        """Initialise une carte avec une valeur """
        self.valeur = valeur

    # Méthodes
    def get_valeur(self):
        """Retourne la valeur de la carte"""
        return self.valeur
    
    def set_valeur(self, valeur):
        """Définit la valeur de la carte"""
        self.valeur = valeur
    
