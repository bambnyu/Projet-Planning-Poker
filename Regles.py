

class Regles:
    """Classe qui représente les règles du jeu"""
    def __init__(self):
        """Initialise le mode de jeu"""
        self.mode= "Classique" #Classique, strictes, moyenne, médiane, etc

    def set_mode(self, mode):
        """Défini le mode de jeu"""
        self.mode = mode

    def get_mode(self):
        """Retourne le mode de jeu"""
        return self.mode

