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
            description = "Les joueurs votent pour la tache actuelle. Ils revelent leur votes en meme temps. Si les votes sont tous identiques la valeur est enregistre sinon un nouveau vote est lancer apres une discussion entre les 2 valeurs les plus extremes.\n"
        elif rule_choosen == "moyenne":
            description = "Les joueurs votent pour la tache actuelle. Ils revelent leur votes en meme temps. La valeur enregistre est la moyenne des votes"
        elif rule_choosen == "mediane":
            description = "Les joueurs votent pour la tache actuelle. Ils revelent leur votes en meme temps. La valeur enregistre est la mediane des votes"
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
        
    def open_file_dialog(self):
        """Opens a file dialog and returns the selected file path.""" 
        # we are using tkinter to open the file explorer window because pygame doesn't have a file dialog
        
        # Hide the main Tkinter window
        root = tk.Tk() # Create a Tkinter window
        root.withdraw() # Hide the main window because it is not needed
        # Open the file dialog
        file_path = filedialog.askopenfilename() # Open the file dialog and return the selected file path
        return file_path
        
    #### input box methods ####  
    def input_box_toggle(self,event,input_box,color_inactive,color_active,active,color):
        if event.type == pygame.MOUSEBUTTONDOWN: # If the user clicked on the input_box rect.
                    if input_box.collidepoint(event.pos): # Toggle the active variable.
                        active = not active     
                    else:
                        active = False
        color = color_active if active else color_inactive # Change the current color of the input box.  
        return active, color
    
    def handle_input_box_events(self, event, active, text, backlog_description ):
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
        
        
        
        
    #### change states of variables and options ####
    def change_difficulty(self, difficulty_name):
        """Change the state of the game to the specified menu."""
        # Set all menu states to False initially
        self.strictes_clicked = False # set the strictes button to clicked
        self.moyenne_clicked = False # set the moyenne button to not clicked 
        self.medianne_clicked = False # set the medianne button to not clicked

        # Set the specified menu to True
        if difficulty_name == 'strictes':
            self.strictes_clicked = True
        elif difficulty_name == 'moyenne':
            self.moyenne_clicked = True
        elif difficulty_name == 'medianne':
            self.medianne_clicked = True
        
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
                    pygame.quit() # quit pygame
                    sys.exit() # quit python
        else:
            pass
    
    def quit_game(self):
        """Quit the game"""
        pygame.quit()
        sys.exit()
    #### end quit game methods ####

    def check_if_all_backlogs_have_difficulty(self):
        description = None
        for backlog in self.jeu.get_backlogs():
            if not backlog.get('difficulty'):
                description = backlog.get('description')
                break

        description = description if description else "No backlogs available"
        # Use draw_box to display the backlog description
        self.draw_box(0, 0, self.screen_width, 100, self.WHITE, description, font_size=20)
        return description
    

        


    def load_menu_loop(self):
        """Loop for the load menu"""
        # Text input box properties
        #wait 1 second
        pygame.time.wait(100) # so it doesn't register the click on the load game button as a click on the start button
        input_box = pygame.Rect(400, 225, 140, 40)  # x, y, width, height
        color_inactive = self.BLUE # color of the input box when it is not clicked
        color_active = self.GREY # color of the input box when it is clicked
        color = color_inactive # default color of the input box
        active = False # default state of the input box
        text = '' # default text of the input box
        font = pygame.font.Font(None, 32) # font of the input box

        players = []  # List to store player names
        loop_keyboard = True # Boolean to keep the loop running
        file_path = None # default file path
        
        while loop_keyboard: # while the loop is running
            for event in pygame.event.get(): # Check for events
                if event.type == pygame.QUIT: # If the user clicks the X in the top right corner, quit the game
                    pygame.quit() # quit pygame
                    sys.exit()  # quit python

                if event.type == pygame.MOUSEBUTTONDOWN: 
                    # If the user clicked on the input_box rect.
                    if input_box.collidepoint(event.pos):
                        # Toggle the active variable.
                        active = not active
                    else:
                        active = False
                    # Change the current color of the input box.
                    color = color_active if active else color_inactive

                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                            # Add the entered text to players list
                            # players.append(text)
                            self.jeu.ajouter_joueur(Joueur(text))
                            text = ''  # Clear the text box after adding
                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1] # Remove the last character from the text box
                        else:
                            text += event.unicode # Add the entered character to the text box

            # Render the current text.
            txt_surface = font.render(text, True, color)
            # Resize the box if the text is too long.
            width = max(200, txt_surface.get_width() + 10)
            input_box.w = width

            # Drawing the screen and buttons
            self.screen.fill(self.WHITE) # Fill screen with white (background)

            if file_path == None: # if no file is selected
                if self.draw_button_general("Load Game (none)", self.button_start_x, self.button_start_y, self.button_width, self.button_height, self.GREY, self.GREEN): # if the load game button is clicked
                    ## open file and load it in a variable
                    file_path = self.open_file_dialog()
                    if file_path:
                        # load and process the game data from the selected file
                        self.jeu.charger_backlog(file_path) 
                    else:
                        file_path = None # If no file is selected, set file_path to None
            else:
                if self.draw_button_general("Load Game (done)", self.button_start_x, self.button_start_y, self.button_width, self.button_height, self.GREY, self.DARK_GREEN): # if the load game button is clicked
                    ## open file from your computer and load it in a variable
                    file_path = self.open_file_dialog()
                    if file_path:
                        # Here, you can call your method to load and process the game data from the selected file
                        self.jeu.charger_backlog(file_path) 
                    else:
                        file_path = None  # If no file is selected, set file_path to None
 
            if self.draw_button_general("Start", self.button_start_x, self.button_start_y + 2 * self.button_gap, self.button_width, self.button_height, self.GREY, self.DARK_GREEN): # if the start button is clicked
                if len(self.jeu.joueurs) > 0 and file_path != None: # if there is at least one player and a file is selected
                    self.load_menu = False # set the load menu to false
                    self.start_menu = True  # set the start menu to true
                    loop_keyboard = False # stop the loop
                if len(self.jeu.joueurs) > 0: # if there is at least one player but no file is selected
                    self.load_menu = False # set the load menu to false 
                    self.createBacklog_menu = True # set the create backlog menu to true
                    loop_keyboard = False # stop the loop
            if self.draw_button_general("Back to main menu", self.button_start_x, self.button_start_y + 3 * self.button_gap, self.button_width, self.button_height, self.GREY, self.GREEN): # if the back to main menu button is clicked    
                self.load_menu = False # set the load menu to false
                self.main_menu = True # set the main menu to true
                loop_keyboard = False # stop the loop
                
            # Add player text
            self.screen.blit(font.render("Add Player :", True, self.BLACK), (self.button_start_x-50, self.button_start_y + self.button_gap+15))    
            # at the bottom of the screen, display the list of players
            self.screen.blit(font.render("Players :", True, self.BLACK), (self.button_start_x-50, self.button_start_y + 4*self.button_gap+15))
            # Display the list of players
            players = [joueur.get_nom() for joueur in self.jeu.joueurs]  # getter liste des joueurs 
            wrapped_text = self.wrap_text(str(players), 78) # 20 characters per line
            y_offset = -20  # offset for the y position of the text
            for line in wrapped_text: # for each line of text
                text_surf, text_rect = self.text_objects(line, font) # render text
                text_rect.topleft = (50, self.button_start_y + 5*self.button_gap+15 + y_offset) # position of the text
                self.screen.blit(text_surf, text_rect) # draw text
                y_offset += 30 # increase the offset for the next line
                ######!!!!!!!!!!!!!!!! need refactoring !!!!!!!!!!!!!!!!!!!!!!!##########
                
            ######!!!!!!!!!!!!!!!! need refactoring !!!!!!!!!!!!!!!!!!!!!!!##########           
            # Blit the text box
            self.screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5)) # Blit the text.
            pygame.draw.rect(self.screen, color, input_box, 2) # Blit the rect.
            pygame.display.update() # Update the screen



            
    def vote_menu(self):
        """Loop for the vote menu"""
        clicked_vote = False  # Boolean to keep the loop running
        while not clicked_vote:  # while the loop is running
            self.screen.fill(self.DARK_GREEN)  # Fill screen with dark green (background)

            # Get the first backlog description without a difficulty value
            description = self.check_if_all_backlogs_have_difficulty()
            # Use draw_box to display the backlog description
            self.draw_box(0, 0, self.screen_width, 100, self.WHITE, description, font_size=20)


            # Display the cards
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
                    

            pygame.display.update() # Update the screen
            for event in pygame.event.get(): # Check for events
                if event.type == pygame.QUIT: # If the user clicks the X in the top right corner, quit the game
                    pygame.quit() # quit pygame
                    sys.exit() # quit python

        # After voting, you might want to go back to the start menu or handle the next action
        self.jeu.set_joueur_actif(self.jeu.get_joueur_actif() + 1) # set the active player to the next player
        self.start_menu = True  # Example: Going back to the start menu
                             

