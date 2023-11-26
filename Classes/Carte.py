
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
    
