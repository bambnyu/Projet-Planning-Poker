import pygame
import sys
import tkinter as tk
from tkinter import filedialog

from Jeu import *
class Visual:
    def __init__(self):
        
        self.jeu = Jeu()
        
        # Game state
        self.main_menu = True 
        self.rules_menu = False
        self.load_menu = False
        self.start_menu = False
        self.createBacklog_menu = False
        self.show_result = False
        
        # state variables for rules menu buttons
        # we need to know which rule is choosen to display the description and correctly handle the votes
        self.strictes_clicked = True
        self.moyenne_clicked = False
        self.medianne_clicked = False
        self.majorite_abs_clicked = False
        self.majorite_rel_clicked = False
        
        # Define colors
        self.WHITE = (255, 255, 255) # used for the background
        self.BLACK = (0, 0, 0) # used for the text
        self.GREY = (200, 200, 200) # used for the buttons
        self.GREEN = (0, 200, 0) # used for the buttons 
        self.DARK_GREEN = (0, 100, 0) # used for the buttons and the background
        self.RED = (200, 0, 0) # used for the buttons / cards with extreme values
        self.BLUE = (0, 0, 200) # used for the buttons / cards with ?
        
        #set up screen 
        
        self.screen_width, self.screen_height = 800, 600
        
        # Define default button properties 
        self.button_width, self.button_height = 200, 50  # width and height of the buttons
        self.button_start_x = self.screen_width // 2 - self.button_width // 2 # x position of the buttons (centered)
        self.button_start_y = 150 # y position of the first button
        self.button_gap = 70 # gap between buttons

        # description test default properties
        self.description_posX =  3.5 * self.screen_width // 5 # x position of the description text

    ##### Methods #####

    ##### Methods linked to boxes and buttons #####
    def draw_box(self, x, y, width, height, box_color, text=None, font_size=20, text_color=None):
        """ Draws a box on the screen and optionally adds text to it. """
        # Draw the box
        pygame.draw.rect(self.screen, box_color, [x, y, width, height])

        # If text is provided, render it on the box
        if text:
            # Use the provided text color or default to black if not provided
            text_color = text_color if text_color else self.BLACK

            # Create font and render text
            small_text = pygame.font.Font("freesansbold.ttf", font_size)
            text_surf = small_text.render(text, True, text_color)
            text_rect = text_surf.get_rect()
            text_rect.center = ((x + (width // 2)), (y + (height // 2)))

            # Draw the text on the box
            self.screen.blit(text_surf, text_rect)
            
    def draw_box_dynamic(self, x, y, initial_width, height, color, text='', font_size=20, text_color=None, max_width=None):
        """Draws a dynamically resizing box based on the length of the input text."""
        font = pygame.font.Font(None, font_size)  # Use default font
        text_surface = font.render(text, True, text_color if text_color else self.BLACK)
        text_width = text_surface.get_width() + 10  # Add some padding

        # Adjust the box width based on the text width
        box_width = max(initial_width, text_width)
        if max_width and box_width > max_width:
            box_width = max_width

        # Draw the box
        pygame.draw.rect(self.screen, color, [x, y, box_width, height])

        # Position the text starting from the left edge of the box
        text_rect = text_surface.get_rect()
        text_rect.topleft = (x + 5, y + (height - text_rect.height) // 2)  # Vertical center
        self.screen.blit(text_surface, text_rect)


    def draw_button_general(self, text, x, y, width, height, active_color, inactive_color, clicked=False):
        """ Draws a button on the screen at a specified position with specified dimensions. """
        mouse = pygame.mouse.get_pos()  # Get mouse position
        click = pygame.mouse.get_pressed()  # Get mouse click

        if clicked:  # If button is clicked, draw button with active color
            button_color = active_color
        elif x < mouse[0] < x + width and y < mouse[1] < y + height:  # If mouse is hovering over button, draw button with active color
            if click[0] == 1 and not clicked:  # If the button is clicked
                return True
            button_color = active_color
        else:
            button_color = inactive_color
        self.draw_box(x, y, width, height, button_color, text)
        return False    
    
    ##### End Methods linked to boxes and buttons #####
    
    #### input box methods ####  
    def input_box_toggle(self,event,input_box,color_inactive,color_active,active,color):
        """Toggle the active variable of an input box based on a mouse click event."""
        if event.type == pygame.MOUSEBUTTONDOWN: # If the user clicked on the input_box rect.
                    if input_box.collidepoint(event.pos): # Toggle the active variable.
                        active = not active     
                    else:
                        active = False
        color = color_active if active else color_inactive # Change the current color of the input box.  
        return active, color
    
    def handle_input_box_events(self, event, active, text, backlog_description):
        """Handle keyboard events for an input box."""

        if event.type == pygame.KEYDOWN:  # Check for keydown event
            if active:  # Check if input box is active
                if event.key == pygame.K_RETURN:  # Enter key pressed
                    # Add the text to backlogs and reset text
                    backlog_description = text
                    self.jeu.ajouter_backlog(backlog_description)
                    text = ''
                elif event.key == pygame.K_BACKSPACE:  # Backspace key pressed
                    text = text[:-1]  # Remove last character
                else:
                    text += event.unicode  # Add new character

        return text
    #### end input box methods ####
        
    ##### Methods linked to text manipulation and representation #####    
    def text_objects(self, text, font):
        """ Creates a text object """
        text_surface = font.render(text, True, self.BLACK) # Render text
        return text_surface, text_surface.get_rect() # Return text surface and rectangle around text
    
    
    def wrap_text(self, text, max_chars):
        """Wraps text into multiple lines based on the maximum characters per line."""
        words = text.split() # Split text into words
        wrapped_lines = [] # List of lines
        current_line = "" # Current line of text
        for word in words: # For each word
            if len(current_line + word) <= max_chars: # If the word can fit on the current line
                current_line += word + " " # Add the word to the current line
            else: # If the word cannot fit on the current line
                wrapped_lines.append(current_line) # Add the current line to the list of lines
                current_line = word + " " # Start a new line with the current word
        if current_line: # If there is text on the current line
            wrapped_lines.append(current_line) # Add the current line to the list of lines
        return wrapped_lines # Return the list of lines
    
    def display_rule_description(self, rule_choosen):
        """Display the description of the rule choosen"""

        if rule_choosen == "strictes":
            description = "Players vote for the current task and reveal their votes simultaneously. If all votes are identical, the value is recorded. If not, a new vote is initiated after a discussion between the two most extreme values.\n"
        elif rule_choosen == "moyenne":
            description = "Players vote for the current task and reveal their votes at the same time. The recorded value is the average of the votes."
        elif rule_choosen == "medianne":
            description = "Players vote for the current task and reveal their votes simultaneously. The recorded value is the median of the votes."
        elif rule_choosen == "majorite_abs":
            description = "Players vote for the current task and reveal their votes at the same time. The recorded value is the one that receives more than half of the votes."
        elif rule_choosen == "majorite_rel":
            description = "Players vote for the current task and reveal their votes simultaneously. The recorded value is the one with the most votes."
        
        else:
                description = "Error"
                
        small_text = pygame.font.Font("freesansbold.ttf", 20) # Define font
        wrapped_text = self.wrap_text(description, 20) # 20 characters per line
        y_offset = -20 # offset for the y position of the text
        for line in wrapped_text: # for each line of text
            text_surf, text_rect = self.text_objects(line, small_text) # render text
            text_rect.topleft = (self.description_posX, 200 + y_offset) # position of the text
            self.screen.blit(text_surf, text_rect) # draw text
            y_offset += 30 # increase the offset for the next line
            
    def display_players_list(self):
        """Display the list of players"""
        players =  self.jeu.get_joueurs() # get the list of players
        wrapped_text = self.wrap_text(str(players), 78) # 20 characters per line
        y_offset = -20  # offset for the y position of the text
        for line in wrapped_text: # for each line of text
            text_surf, text_rect = self.text_objects(line, font = pygame.font.Font(None, 32)) # render text
            text_rect.topleft = (50, self.button_start_y + 5*self.button_gap+15 + y_offset) # position of the text
            self.screen.blit(text_surf, text_rect) # draw text
            y_offset += 30 # increase the offset for the next line
            
    ##### End Methods linked to text manipulation and representation #####   
        
    ##### Methods linked to files #####   
    def open_file_dialog(self):
        """Opens a file dialog and returns the selected file path.""" 
        # we are using tkinter to open the file explorer window because pygame doesn't have a file dialog
        
        # Hide the main Tkinter window
        root = tk.Tk() # Create a Tkinter window
        root.withdraw() # Hide the main window because it is not needed
        # Open the file dialog
        file_path = filedialog.askopenfilename() # Open the file dialog and return the selected file path
        return file_path
    
    ##### End Methods linked to files #####
        
    
        
        
        
        
    #### change states of variables and options ####
    
    def change_difficulty(self, difficulty_name):
        """Change the state of the game to the specified menu."""
        # Set all menu states to False initially
        self.strictes_clicked = False # set the strictes button to clicked
        self.moyenne_clicked = False # set the moyenne button to not clicked 
        self.medianne_clicked = False # set the medianne button to not clicked
        self.majorite_abs_clicked = False # set the majorite_abs button to not clicked
        self.majorite_rel_clicked = False # set the majorite_rel button to not clicked

        # Set the specified menu to True
        if difficulty_name == 'strictes':
            self.strictes_clicked = True
        elif difficulty_name == 'moyenne':
            self.moyenne_clicked = True
        elif difficulty_name == 'medianne':
            self.medianne_clicked = True
        elif difficulty_name == 'majorite_abs':
            self.majorite_abs_clicked = True
        elif difficulty_name == 'majorite_rel':
            self.majorite_rel_clicked = True
        
    def change_state(self, menu_name):
        """Change the state of the game to the specified menu."""
        # Set all menu states to False initially
        self.main_menu = False
        self.rules_menu = False
        self.load_menu = False
        self.start_menu = False
        self.createBacklog_menu = False
        self.show_result = False
        # Set the specified menu to True
        if menu_name == 'main_menu':
            self.main_menu = True
        elif menu_name == 'rules_menu':
            self.rules_menu = True
        elif menu_name == 'load_menu':
            self.load_menu = True
        elif menu_name == 'start_menu':
            self.start_menu = True
        elif menu_name == 'createBacklog_menu':
            self.createBacklog_menu = True
        elif menu_name == 'show_result':
            self.show_result = True
    #### end change states of variables and options ####
    
    #### quit game methods ####
    def check_for_quit(self,event):
        """Quit the game if the user clicks the X in the top right corner."""
        if event.type == pygame.QUIT:
                    self.quit_game()
        else:
            pass
    
    def quit_game(self):
        """Quit the game"""
        pygame.quit()
        sys.exit()
    #### end quit game methods ####
    
    
    #### search backlog methods ####
    def check_if_all_backlogs_have_difficulty(self):
        """Check if all backlogs have a difficulty value."""
        description = None
        for backlog in self.jeu.get_backlogs():
            if not backlog.get('difficulty'):
                description = backlog.get('description')
                break

        description = description if description else "No backlogs available"
        # Use draw_box to display the backlog description
        self.draw_box(0, 0, self.screen_width, 100, self.WHITE, description, font_size=20)
        return description
    #### end search backlog methods ####
            
    #### display methods for votes ####
    def vote_color(self,vote,max_vote,min_vote):
        """ vote color"""
        if vote.isdigit() and (int(vote) == max_vote or int(vote) == min_vote) and max_vote != min_vote: # If the vote is a number and it is the maximum or minimum vote
                    box_color = self.RED  # Red for extreme values
        elif vote in ["?", "cafe"]: # If the vote is a question mark or coffee
            box_color = self.BLUE   #pygame.Color('blue')  # Blue for "?" or "coffee"
        else:
            box_color = self.WHITE  # Default color
        return box_color


    def cafe_vote(self):
        """cafe vote"""
        for backlog in self.jeu.get_backlogs(): # for each backlog
                if backlog.get('difficulty') == 'Skipped': # if the backlog has a difficulty value of skipped
                    backlog['difficulty'] = None # set the difficulty value to None (default value)
                self.jeu.enregistrer_backlog("Code/Backlogs/backlog.json") # save the backlogs in a json file
                
    def question_mark_vote(self):
        """ question mark vote"""
        if self.draw_button_general("Skip this backlog", self.button_start_x, self.screen_height - 200, self.button_width, self.button_height, self.GREY,self.GREEN):    
                    self.jeu.set_difficulty_backlog('Skipped')  # Mark current backlog as skipped
                    self.jeu.set_joueur_actif(1)  # Reset active player for next backlog
                    self.change_state("start_menu") # change the state to start menu
                       
    def medianne_vote(self,numeric_votes):
        """ moyenne vote"""
        if self.draw_button_general("Validate votes", self.button_start_x, self.screen_height - 200, self.button_width, self.button_height, self.GREY, self.GREEN):                    
                        medianne = self.jeu.medianne(numeric_votes) # Calculate the medianne
                        self.jeu.set_difficulty_backlog(medianne)  # Set the difficulty of the backlog to the medianne
                        self.jeu.set_joueur_actif(1) # Reset active player for next backlog go back to the first player
                        self.change_state("start_menu") # change the state to start menu
                        
    def moyenne_vote(self,numeric_votes):
        """ medianne vote"""
        if self.draw_button_general("Validate votes", self.button_start_x, self.screen_height - 200, self.button_width, self.button_height, self.GREY, self.GREEN):
                        moyenne = self.jeu.moyenne(numeric_votes)
                        self.jeu.set_difficulty_backlog(moyenne) # Set the difficulty of the backlog to the moyenne
                        self.jeu.set_joueur_actif(1) # Reset active player for next backlog go back to the first player
                        self.change_state("start_menu") # change the state to start menu
    
    def strictes_vote_egaux(self,all_votes):
        """ strictes vote"""
        if self.draw_button_general("Validate votes", self.button_start_x, self.screen_height - 200, self.button_width, self.button_height, self.GREY, self.GREEN):    
            self.jeu.set_difficulty_backlog(all_votes[0]) # Set the difficulty of the backlog to the first vote
            self.jeu.set_joueur_actif(1) # Reset active player for next backlog go back to the first player
            self.change_state("start_menu") # change the state to start menu 
  
    def strictes_vote_diff(self):
        """ strictes vote"""
        if self.draw_button_general("Restart vote", self.button_start_x, self.screen_height - 200, self.button_width, self.button_height, self.GREY, self.GREEN):
            self.jeu.set_joueur_actif(1) # Reset active player for next backlog go back to the first player
            self.change_state("start_menu") # change the state to start menu
    
    def majorite_abs_vote_exist(self,value):
        """ majorite_abs vote"""
        if self.draw_button_general("Validate votes", self.button_start_x, self.screen_height - 200, self.button_width, self.button_height, self.GREY, self.GREEN):
            self.jeu.set_difficulty_backlog(value) # Set the difficulty of the backlog to the most frequent vote
            self.jeu.set_joueur_actif(1) # Reset active player for next backlog go back to the first player
            self.change_state("start_menu") # change the state to start menu
            
    def majorite_abs_vote_not_exist(self):
        """ majorite_abs vote"""
        if self.draw_button_general("Restart vote", self.button_start_x, self.screen_height - 200, self.button_width, self.button_height, self.GREY, self.GREEN):
            self.jeu.set_joueur_actif(1)
            self.change_state("start_menu")
    
    def majorite_rel_vote(self,numeric_votes):
        """ majorite_rel vote"""
        # count the number of votes for each value
        # the value with the most votes is the difficulty
        # if there is a tie, the difficulty is the lowest value
        count = {}
        for i in numeric_votes:
            count[i] = count.get(i, 0) + 1
        max_count = max(count.values())
        difficulty = min([k for k, v in count.items() if v == max_count])
        if self.draw_button_general("Validate vote", self.button_start_x, self.screen_height - 200, self.button_width, self.button_height, self.GREY, self.GREEN):
            self.jeu.set_difficulty_backlog(difficulty) # Set the difficulty of the first backlog without a difficulty value
            self.jeu.set_joueur_actif(1) # Set the active player to the first player
            self.change_state("start_menu") # change the state to start menu
    
    
    def display_cards_to_vote_screens(self,clicked_vote):
        """Display the cards to vote screens"""
        card_values = ["0", "1", "2", "3", "5", "8", "13", "20", "40", "100", "?", "cafe"]
        card_start_y = self.screen_height // 2 - 50
        card_gap = 75
        card_width = 50
        card_start_x = 65
        for i in range(int(len(card_values) / 2)): # for each card
            if self.draw_button_general(card_values[i], card_start_x + i * (card_width + card_gap), card_start_y, card_width, self.button_height, self.WHITE, self.WHITE):
                clicked_vote = True # set clicked_vote to true
                self.jeu.joueurs[self.jeu.get_joueur_actif()-1].set_carte(card_values[i]) # set the card of the player to the value of the card clicked
                

        for i in range(0, int(len(card_values) / 2)): # for each card
            if self.draw_button_general(card_values[i+6], card_start_x + i * (card_width + card_gap), card_start_y + 150, card_width, self.button_height ,self.WHITE, self.WHITE):
                clicked_vote = True # set clicked_vote to true
                self.jeu.joueurs[self.jeu.get_joueur_actif()-1].set_carte(card_values[i+6]) # set the card of the player to the value of the card clicked
        
        return clicked_vote
            
    #### display methods for votes ####
    
    
# Code by Adjame Tellier-Rozen (ROZEN)