import json
from Joueur import *



class Jeu:
    """Class that represents the game"""

    #########################################
    # Attributs and methods of the Jeu class
    #########################################
    
    ##### Attributs #####
    
    def __init__(self):
        """Initializes the game with a list of players and an initially empty backlog"""
        self.joueurs = [] # player list
        self.backlogs = [] # backlog list
        self.joueur_actif = 1 # active player
        
        
    ######## Methods ########
    
    ##### Methods linked to the player #####
    def get_joueurs(self):
        """Returns the list of players"""
        return [joueur.nom for joueur in self.joueurs]  # getter player list 

    def ajouter_joueur(self, joueur):
        """Adds a player to the list of players"""
        self.joueurs.append(joueur)  # setter player list
    
    def set_joueur_actif(self, value):
        """Sets the active player"""
        self.joueur_actif = value  # setter active player

    def get_joueur_actif(self):
        """Returns the active player"""
        return self.joueur_actif  # getter active player
    
    
    ##### Methods linked to the backlogs #####
    def get_backlogs(self):
        """Returns the backlog"""
        return self.backlogs # getter backlog
    
    def ajouter_backlog(self, description):
        """Adds a backlog with a given description."""
        # Create a new backlog item
        new_backlog_item = {
            "description": description, # description of the backlog
            "difficulty": None, # None = no difficulty defined null in the json file
        }
        self.backlogs.append(new_backlog_item) # add this item to the backlog list
        
    def charger_backlog(self, fichier):
        """Loads the backlog from a json file"""
        with open(fichier, 'r') as f:
            self.backlogs = json.load(f) # setter/initilialise the backlog

    def enregistrer_backlog(self, fichier): 
        """Saves the backlog to a json file"""
        with open(fichier, 'w') as f:
            json.dump(self.backlogs, f) # save the new backlogs to the json file
            
    def enregistrer_backlog_skipped(self, fichier):
        """Saves the backlogs to a json file and transforms the skipped difficulties into None"""
        for backlog in self.get_backlogs():
                if backlog.get('difficulty') == 'Skipped':
                    backlog['difficulty'] = None
        self.enregistrer_backlog("Code/Backlogs/backlog.json")        
                
    def set_difficulty_backlog(self, difficulty):
        """Defines the difficulty of a backlog of the first backlog without difficulty"""
        for backlog in self.backlogs: # for each backlog
            if backlog['difficulty'] == None: # if the backlog has no difficulty
                backlog['difficulty'] = difficulty # define the difficulty of the backlog
                break
    ##### End Methods linked to the backlogs #####
    

    ##### Methods linked to the recovery of votes #####
    def get_all_votes(self):
        """Returns all votes"""
        return [joueur.get_carte() for joueur in self.joueurs]    
    
    def get_numerical_votes(self):
        """Returns the numeric votes"""
        votes = self.get_all_votes()
        return [int(vote) for vote in votes if vote.isdigit()] # Get only numeric votes
    
    def max_min_votes(self):
        """Returns the maximum and minimum votes"""
        numeric_votes = self.get_numerical_votes() # Get only numeric votes
        max_vote = max(numeric_votes, default=None) # Get the maximum vote
        min_vote = min(numeric_votes, default=None) # Get the minimum vote 
        return max_vote, min_vote
    ##### End Methods linked to the recovery of votes #####
    
    ##### Methods linked to the calculation of the difficulty #####
    def medianne(self, liste):
        """Calculates the median of a list of values"""
        liste.sort() # sort the list
        if len(liste) % 2 == 0: #   if the list is even
            return (liste[len(liste) // 2] + liste[len(liste) // 2 - 1]) / 2 #  return the average of the two values in the middle
        else:
            return liste[len(liste) // 2] #  return the value in the middle

    def moyenne(self, liste):
        """Calculates the average of a list of values"""
        if not liste:  # Check if the list is empty
            return 0
        sum_of_elements = sum(liste)
        length_of_list = len(liste)
        # Calculate the average and round up
        average = -(-sum_of_elements // length_of_list)

        return average
    ##### End Methods linked to the calculation of the difficulty #####
    
# Code by Adjame Tellier-Rozen (ROZEN)