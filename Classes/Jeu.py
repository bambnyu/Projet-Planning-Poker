import json
from Joueur import *



class Jeu:
    """Classe qui représente le jeu"""

    #########################################
    # Attributs et méthodes de la classe Jeu
    #########################################
    
    ##### Attributs #####
    
    def __init__(self):
        """Initialise le jeu avec une liste de joueurs et un backlog initialement vide"""
        self.joueurs = [] # liste des joueurs
        self.backlogs = [] # liste des backlogs
        self.joueur_actif = 1 # joueur actif
        
        
    ######## Méthodes ########
    
    ##### Méthodes liées aux joueurs #####
    def get_joueurs(self):
        """Retourne la liste des joueurs"""
        return [joueur.get_nom() for joueur in self.joueurs]  # getter liste des joueurs

    def ajouter_joueur(self, joueur):
        """Ajoute un joueur à la liste des joueurs"""
        self.joueurs.append(joueur)  # setter liste des joueurs
    
    def set_joueur_actif(self, value):
        """Définit le joueur actif"""
        self.joueur_actif = value  # setter joueur actif

    def get_joueur_actif(self):
        """Retourne le joueur actif"""
        return self.joueur_actif  # getter joueur actif
    
    
    ##### Méthodes liées au backlog #####
    def get_backlogs(self):
        """Retourne le backlog"""
        return self.backlogs # getter backlog
    
    def ajouter_backlog(self, description):
        """Ajoute un backlog avec une description donnée."""
        # Créer un nouvel élément de backlog
        new_backlog_item = {
            "description": description, # description du backlog
            "difficulty": None, # None = pas de difficulté définie null dans le fichier json
        }
        self.backlogs.append(new_backlog_item) # Ajouter cet élément à la liste des backlogs
        
    def charger_backlog(self, fichier):
        """Charge le backlog depuis un fichier json"""
        with open(fichier, 'r') as f:
            self.backlogs = json.load(f) # setter/initilialise le backlog



    def enregistrer_backlog(self, fichier): 
        """Enregistre le backlog dans un fichier json"""
        with open(fichier, 'w') as f:
            json.dump(self.backlogs, f) # enregistre les nouveau backlogs dans le fichier json
            
    def enregistrer_backlog_skipped(self, fichier):
        """Enregistre les backlogs dans un fichier json et transforme les difficultés skipped en None"""
        for backlog in self.get_backlogs():
                if backlog.get('difficulty') == 'Skipped':
                    backlog['difficulty'] = None
        self.enregistrer_backlog("Backlogs/backlog.json")        

                
    def set_difficulty_backlog(self, difficulty):
        """Définit la difficulté d'un backlog du premier backlog sans difficulté"""
        for backlog in self.backlogs: # pour chaque backlog
            if backlog['difficulty'] == None: # si backlog est sans difficulté
                backlog['difficulty'] = difficulty # définit la difficulté du backlog
                break
    
    ##### Méthodes liées a la recuperation des votes #####    
    def get_all_votes(self):
        return [joueur.get_carte() for joueur in self.joueurs]    
    
    def get_numerical_votes(self):
        """Retourne les votes numériques"""
        votes = self.get_all_votes()
        return [int(vote) for vote in votes if vote.isdigit()] # Get only numeric votes
    
    def max_min_votes(self):
        """Retourne le maximum et le minimum des votes"""
        numeric_votes = self.get_numerical_votes() # Get only numeric votes
        max_vote = max(numeric_votes, default=None) # Get the maximum vote
        min_vote = min(numeric_votes, default=None) # Get the minimum vote 
        return max_vote, min_vote
    ##### end Méthodes liées a la recuperation des votes #####
        
    ##### Méthodes liées au calcul de la difficulté #####    
    def medianne(self, liste):
        """Calcule la médiane d'une liste de valeurs"""
        liste.sort() # trier la liste
        if len(liste) % 2 == 0: # si la liste est paire
            return (liste[len(liste) // 2] + liste[len(liste) // 2 - 1]) / 2 # retourne la moyenne des deux valeurs du milieu
        else:
            return liste[len(liste) // 2] # retourne la valeur du milieu
