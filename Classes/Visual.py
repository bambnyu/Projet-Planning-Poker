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



    def draw_box(self, x, y, width, height, color, text):
        """ Draws a box on the screen """
        pygame.draw.rect(self.screen, color, [x, y, width, height]) # Draw button
        small_text = pygame.font.Font("freesansbold.ttf", 20) # Define font
        text_surf, text_rect = self.text_objects(text, small_text) # Render text
        text_rect.center = ((x + (width // 2)), (y + (height // 2))) # Center text on button
        self.screen.blit(text_surf, text_rect) # Draw text
        
         
    
    def draw_button(self, text, y, active_color, inactive_color, clicked=False):
        """ Draws a button on the screen  """
        mouse = pygame.mouse.get_pos() # Get mouse position
        click = pygame.mouse.get_pressed() # Get mouse click

        if clicked: # If button is clicked, draw button with active color
            pygame.draw.rect(self.screen, active_color, [self.button_start_x, y, self.button_width, self.button_height]) 
        elif self.button_start_x < mouse[0] < self.button_start_x + self.button_width and y < mouse[1] < y + self.button_height: # If mouse is hovering over button, draw button with active color
            pygame.draw.rect(self.screen, active_color, [self.button_start_x, y, self.button_width, self.button_height]) 
            if click[0] == 1: # If button is clicked, return True
                return True
        else: # If mouse is not hovering over button, draw button with inactive color
            pygame.draw.rect(self.screen, inactive_color, [self.button_start_x, y, self.button_width, self.button_height])

        small_text = pygame.font.Font("freesansbold.ttf", 20) # Define font
        text_surf, text_rect = self.text_objects(text, small_text) # Render text
        text_rect.center = ((self.button_start_x + (self.button_width // 2)), (y + (self.button_height // 2))) # Center text on button
        self.screen.blit(text_surf, text_rect) # Draw text
         
        
        
    def draw_button_anywhere(self, text, x, y, width, active_color, inactive_color, clicked=False):
        """ Draws a button on the screen  """
        mouse = pygame.mouse.get_pos() # Get mouse position
        click = pygame.mouse.get_pressed() # Get mouse click

        if clicked: # If button is clicked, draw button with active color
            pygame.draw.rect(self.screen, active_color, [x, y, width, self.button_height])
        elif x < mouse[0] < x +width and y < mouse[1] < y + self.button_height: # If mouse is hovering over button, draw button with active color
            pygame.draw.rect(self.screen, active_color, [x, y, width, self.button_height])
            if click[0] == 1: # If button is clicked, return True
                return True
        else: # If mouse is not hovering over button, draw button with inactive color
            pygame.draw.rect(self.screen, inactive_color, [x, y, width, self.button_height])

        small_text = pygame.font.Font("freesansbold.ttf", 20) # Define font
        text_surf, text_rect = self.text_objects(text, small_text)  # Render text
        text_rect.center = ((x + (width // 2)), (y + (self.button_height // 2))) # Center text on button
        self.screen.blit(text_surf, text_rect) # Draw text
        
        
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
            description = "Les joueurs votent pour la tache actuelle. Ils revelent leur votes en meme temps." \
                        "Si les votes sont tous identiques la valeur est enregistre sinon un nouveau vote est lancer apres une discussion entre les 2 valeurs les plus extremes.\n"
        
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
        
    def rules_menu_loop(self):
        """Loop for the rules menu"""
        if self.strictes_clicked: # if the strictes button is clicked
            self.display_rule_description("strictes")
        elif self.moyenne_clicked: # if the moyenne button is clicked
            self.display_rule_description("moyenne")
        elif self.medianne_clicked: # if the medianne button is clicked
            self.display_rule_description("mediane")
                
                
        if self.draw_button("Strictes", self.button_start_y, self.GREY, self.GREEN, self.strictes_clicked): # if the strictes button is clicked
            self.strictes_clicked = True # set the strictes button to clicked
            self.moyenne_clicked = False # set the moyenne button to not clicked 
            self.medianne_clicked = False # set the medianne button to not clicked
        if self.draw_button("Moyenne", self.button_start_y + self.button_gap, self.GREY, self.GREEN, self.moyenne_clicked): # if the moyenne button is clicked
            self.strictes_clicked = False # set the strictes button to not clicked
            self.moyenne_clicked = True # set the moyenne button to clicked
            self.medianne_clicked = False # set the medianne button to not clicked
        if self.draw_button("Medianne", self.button_start_y + 2 * self.button_gap, self.GREY, self.GREEN, self.medianne_clicked): # if the medianne button is clicked
            self.strictes_clicked = False # set the strictes button to not clicked
            self.moyenne_clicked = False # set the moyenne button to not clicked
            self.medianne_clicked = True # set the medianne button to clicked
        if self.draw_button("Back to main menu", self.button_start_y + 3 * self.button_gap, self.GREY, self.GREEN): # if the back to main menu button is clicked
            self.rules_menu = False # set the rules menu to not clicked
            self.main_menu = True # set the main menu to clicked
        
    
    def main_menu_loop(self):
        """Loop for the main menu"""
        if self.draw_button("Start", self.button_start_y, self.GREY, self.GREEN): # if the start button is clicked
            self.main_menu = False # set the main menu to not clicked
            self.load_menu = True # set the load menu to clicked 
        if self.draw_button("Rules", self.button_start_y + self.button_gap, self.GREY, self.GREEN): # if the rules button is clicked
            self.main_menu = False # set the main menu to not clicked
            self.rules_menu = True # set the rules menu to clicked
        if self.draw_button("Quit", self.button_start_y + 2 * self.button_gap, self.GREY, self.RED): # if the quit button is clicked
            pygame.quit() # quit pygame
            sys.exit() # quit python
            
    def load_menu_loop(self):
        """Loop for the load menu"""
        # Text input box properties
        #wait 1 second
        pygame.time.wait(100) # so it doesn't register the click on the load game button as a click on the start button
        input_box = pygame.Rect(400, 225, 140, 40)  # x, y, width, height
        color_inactive = pygame.Color('lightskyblue3') # color of the input box when it is not clicked
        color_active = pygame.Color('dodgerblue2') # color of the input box when it is clicked
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
                if self.draw_button("Load Game (none)", self.button_start_y, self.GREY, self.GREEN): # if the load game button is clicked
                    ## open file and load it in a variable
                    file_path = self.open_file_dialog()
                    if file_path:
                        # load and process the game data from the selected file
                        self.jeu.charger_backlog(file_path) 
                    else:
                        file_path = None # If no file is selected, set file_path to None
            else:
                if self.draw_button("Load Game (done)", self.button_start_y, self.GREY, self.DARK_GREEN): # if the load game button is clicked
                    ## open file from your computer and load it in a variable
                    file_path = self.open_file_dialog()
                    if file_path:
                        # Here, you can call your method to load and process the game data from the selected file
                        self.jeu.charger_backlog(file_path) 
                    else:
                        file_path = None  # If no file is selected, set file_path to None

            if self.draw_button("Start", self.button_start_y + 2 * self.button_gap, self.GREY, self.DARK_GREEN): # if the start button is clicked 
                if len(self.jeu.joueurs) > 0 and file_path != None: # if there is at least one player and a file is selected
                    self.load_menu = False # set the load menu to false
                    self.start_menu = True  # set the start menu to true
                    loop_keyboard = False # stop the loop
                if len(self.jeu.joueurs) > 0: # if there is at least one player but no file is selected
                    self.load_menu = False # set the load menu to false 
                    self.createBacklog_menu = True # set the create backlog menu to true
                    loop_keyboard = False # stop the loop
            if self.draw_button("Back to main menu", self.button_start_y + 3 * self.button_gap, self.GREY, self.GREEN): # if the back to main menu button is clicked
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

            # Blit the text box
            self.screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5)) # Blit the text.
            pygame.draw.rect(self.screen, color, input_box, 2) # Blit the rect.
            pygame.display.update() # Update the screen


    def createBacklog_menu_loop(self):
        """Loop for the create backlog menu"""
        #### HERE WE NEED AN INPUT BOX TO ENTER THE DESCRIPTION OF BACKLOGS
        ### and show the already created backlogs on the bottom of the screen
        ### a button to go back to the main menu
        ### a button to go to the start menu
            # Input box setup
        input_box = pygame.Rect(300, 200, 200, 60)  # x, y, width, height
        color_inactive = pygame.Color('lightskyblue3') # color of the input box when it is not clicked
        color_active = pygame.Color('dodgerblue2') # color of the input box when it is clicked
        color = color_inactive # default color of the input box
        active = False # default state of the input box
        text = '' # default text of the input box
        font = pygame.font.Font(None, 32) # font of the input box
 
        backlog_description = '' # default backlog description
        #######
        
        # Loop for the create backlog menu
        while True: # while the loop is running                     
            for event in pygame.event.get(): # Check for events
                if event.type == pygame.QUIT: # If the user clicks the X in the top right corner, quit the game
                    pygame.quit() # quit pygame
                    sys.exit() # quit python

                # Event handling for the input box
                if event.type == pygame.MOUSEBUTTONDOWN: # If the user clicked on the input_box rect.
                    if input_box.collidepoint(event.pos): # Toggle the active variable.
                        active = not active     
                    else:
                        active = False
                    color = color_active if active else color_inactive # Change the current color of the input box.

                if event.type == pygame.KEYDOWN: # If a key is pressed
                    if active: # If the input box is active
                        if event.key == pygame.K_RETURN: # If the enter key is pressed
                            backlog_description = text # Set the backlog description to the text in the input box
                            self.jeu.ajouter_backlog((backlog_description))  # Add the backlog to your game object
                            text = '' # Clear the text box after adding
                        elif event.key == pygame.K_BACKSPACE: # If the backspace key is pressed
                            text = text[:-1] # Remove the last character from the text box
                        else:
                            text += event.unicode # Add the entered character to the text box

            self.screen.fill(self.WHITE) # Fill screen with white (background)
            
            instruction_text = "Enter the description of your backlogs in the box below" # Instruction text
            self.screen.blit(font.render(instruction_text, True, self.BLACK), (110, 50)) # Display instruction text


            # Display existing backlogs
            y_offset = 150  # offset for the y position of the text
            for backlog in self.jeu.get_backlogs(): # for each backlog
                self.screen.blit(font.render(backlog['description'], True, self.BLACK), (50, y_offset)) # Display the description of the backlog
                y_offset += 40 # increase the offset for the next line

            # Navigation buttons
            if self.draw_button("Back to main menu", self.screen_height - 120, self.GREY, self.GREEN): # if the back to main menu button is clicked
                self.createBacklog_menu = False # set the create backlog menu to false
                self.main_menu = True # set the main menu to true
                break
            if self.draw_button("Start Game", self.screen_height - 70, self.GREY, self.DARK_GREEN): # if the start game button is clicked
                # enregistrer le backlog dans un fichier json
                if backlog_description: # if there is at least one backlog
                    self.jeu.enregistrer_backlog("Backlogs/backlog.json") # save the backlogs in a json file
                    self.createBacklog_menu = False # set the create backlog menu to false
                    self.start_menu = True # set the start menu to true
                    break

            # Input box for new backlog
            txt_surface = font.render(text, True, color) # Render the current text.
            width = max(200, txt_surface.get_width() + 10) # Resize the box if the text is too long.
            input_box.w = width # Set the width of the input box to the width of the text
            self.screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5)) # Blit the text.
            pygame.draw.rect(self.screen, color, input_box, 2) # Blit the rect.
            pygame.display.flip() # Update the screen
            
    def vote_menu(self):
        """Loop for the vote menu"""
        clicked_vote = False # Boolean to keep the loop running
        while not clicked_vote: # while the loop is running
            self.screen.fill(self.DARK_GREEN) # Fill screen with dark green (background)

            backlog_box = pygame.Rect(0, 0, self.screen_width, 100) # Position and size of the rectangle
            pygame.draw.rect(self.screen, self.WHITE, backlog_box) # Draw the rectangle

            # Display the first backlog without a difficulty value
            small_text = pygame.font.Font("freesansbold.ttf", 20) # Define font
            description = None # default description

            for backlog in self.jeu.get_backlogs(): # for each backlog
                if not backlog.get('difficulty'): # If the backlog doesn't have a difficulty value
                    description = backlog.get('description') # set the description to the description of the backlog
                    break

            if description: # if there is a description
                text_surf, text_rect = self.text_objects(description, small_text) # render text
                text_rect.center = ((self.screen_width // 2), (50)) # position of the text 
                self.screen.blit(text_surf, text_rect) # draw text


            # Display the cards
            card_values = ["0", "1", "2", "3", "5", "8", "13", "20", "40", "100", "?", "cafe"]
            card_start_y = self.screen_height // 2 - 50
            card_gap = 75
            card_width = 50
            card_start_x = 65

            for i in range(int(len(card_values) / 2)): # for each card
                if self.draw_button_anywhere(card_values[i], card_start_x + i * (card_width + card_gap), card_start_y, card_width, self.WHITE, self.WHITE):
                    print(card_values[i] + " clicked") # print the value of the card clicked
                    clicked_vote = True # set clicked_vote to true
                    self.jeu.joueurs[self.jeu.get_joueur_actif()-1].set_carte(card_values[i]) # set the card of the player to the value of the card clicked
                    

            for i in range(0, int(len(card_values) / 2)): # for each card
                if self.draw_button_anywhere(card_values[i+6], card_start_x + i * (card_width + card_gap), card_start_y + 150, card_width, self.WHITE, self.WHITE):
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
                

        
        
        
        
    def start_menu_loop(self):
        """ Loop for the start menu """
        self.screen.fill(self.DARK_GREEN) # Fill screen with dark green (background)
        backlog_box = pygame.Rect(0, 0, self.screen_width, 100)  # Position and size of the rectangle
        pygame.draw.rect(self.screen, self.WHITE, backlog_box)  # Draw the rectangle

        # Display the first backlog without a difficulty value
        small_text = pygame.font.Font("freesansbold.ttf", 20) # Define font
        description = None # default description
        for backlog in self.jeu.get_backlogs(): # for each backlog
            if not backlog.get('difficulty'):  # If the backlog doesn't have a difficulty value
                description = backlog.get('description') # set the description to the description of the backlog
                break

        if description: # if there is a description
            text_surf, text_rect = self.text_objects(description, small_text) # render text
            text_rect.center = ((self.screen_width // 2), (50)) # position of the text
            self.screen.blit(text_surf, text_rect) # draw text
        else:
            # Handle the case where all backlogs have difficulty values or there are no backlogs
            text_surf, text_rect = self.text_objects("No backlogs available", small_text) # render text
            text_rect.center = ((self.screen_width // 2), (50)) # position of the text
            self.screen.blit(text_surf, text_rect) # draw text
            #enregistrer le backlog dans un fichier json
            for backlog in self.jeu.get_backlogs(): # for each backlog
                if backlog.get('difficulty') == 'Skipped': # if the backlog has a difficulty value of skipped
                    backlog['difficulty'] = None # set the difficulty value to None (default value)
            self.jeu.enregistrer_backlog("Backlogs/backlog.json") # save the backlogs in a json file
                    
            #######
            
            pygame.time.wait(1000)  # Wait 1 second before going back to the main menu
            self.start_menu = False # Change state back to main menu
            self.main_menu = True # Change state back to main menu

        if self.jeu.get_joueur_actif() <= len(self.jeu.get_joueurs()): # if there are still players to vote
            player_name = self.jeu.get_joueurs()[self.jeu.get_joueur_actif()-1] # get the name of the active player
            player_box = pygame.Rect(250, 150, 300, 50) # Position and size of the rectangle
            pygame.draw.rect(self.screen, self.WHITE, player_box)   # Draw the rectangle
            player_text_surf, player_text_rect = self.text_objects(f"Active Player: {player_name}", small_text) # render text
            player_text_rect.center = (player_box.centerx, player_box.centery) # position of the text
            self.screen.blit(player_text_surf, player_text_rect) # draw text
        else:
            self.show_result_screen() # if all players have voted, go to the result screen

        go_button_y = self.screen_height // 2 + 50 # Position it near the bottom of the screen
        go_button_text = "Go" # Text on the button
        if self.draw_button(go_button_text, go_button_y, self.GREY, self.GREEN): # if the go button is clicked
            self.vote_menu() # go to the vote menu
            
        back_button_y = self.screen_height - self.button_height - 10  # Position it near the bottom of the screen
        back_button_text = "Back to Main Menu"  # Text on the button

        if self.draw_button(back_button_text, back_button_y, self.GREY, self.GREEN): # if the back button is clicked
            #enregistrer le backlog dans un fichier json
            self.jeu.enregistrer_backlog("Backlogs/backlog.json") # save the backlogs in a json file
            self.start_menu = False # Change state back to main menu
            self.main_menu = True  # Change state back to main menu
         


    def show_result_screen(self):
        """ trigger for the Loop of the result screen """
        # Transition to the result screen
        self.show_result= True # Boolean to keep the loop running
        self.start_menu = False # Change state back to main menu
        

    def show_result_loop(self):
        """ Loop for the result screen """
        running = True # Boolean to keep the loop running
        while running: # while the loop is running
            self.screen.fill(self.DARK_GREEN) # Fill screen with dark green (background)
            
            backlog_box = pygame.Rect(0, 0, self.screen_width, 100)  # Position and size of the rectangle
            pygame.draw.rect(self.screen, self.WHITE, backlog_box)  # Draw the rectangle

            # Display the first backlog without a difficulty value
            small_text = pygame.font.Font("freesansbold.ttf", 20) # Define font
            description = None # default description

            for backlog in self.jeu.get_backlogs(): # for each backlog
                if not backlog.get('difficulty'):  # If the backlog doesn't have a difficulty value
                    description = backlog.get('description') # set the description to the description of the backlog
                    break

            if description: # if there is a description
                text_surf, text_rect = self.text_objects(description, small_text) # render text
                text_rect.center = ((self.screen_width // 2), (50)) # position of the text
                self.screen.blit(text_surf, text_rect) # draw text
            else:
                # Handle the case where all backlogs have difficulty values or there are no backlogs
                text_surf, text_rect = self.text_objects("No backlogs available", small_text) # render text
                text_rect.center = ((self.screen_width // 2), (50)) # position of the text
                self.screen.blit(text_surf, text_rect) # draw text
                pygame.time.wait(1000)  # Wait 1 second before going back to the main menu
                self.start_menu = False # Change state back to main menu
                self.main_menu = True # Change state back to main menu

            # Define offset between boxes
            box_offset = 10  # Space between boxes

            # Prepare to detect extreme values
            votes = [joueur.get_carte() for joueur in self.jeu.joueurs] # Get all votes
            numeric_votes = [int(vote) for vote in votes if vote.isdigit()] # Get only numeric votes
            max_vote = max(numeric_votes, default=None) # Get the maximum vote
            min_vote = min(numeric_votes, default=None) # Get the minimum vote 

            # Calculate the width and position for the vote boxes
            num_players = len(self.jeu.joueurs) # Number of players
            total_offset = box_offset * (num_players - 1) # Total offset between boxes
            vote_box_width = (self.screen_width - 200 - total_offset) // num_players # Width of each box
            vote_box_height = 40 # Height of each box
            vote_box_start_x = (self.screen_width - ((vote_box_width + box_offset) * num_players - box_offset)) // 2 # X position of the first box
            vote_box_y = self.screen_height // 2 - vote_box_height // 2 # Y position of the boxes

            # Display the votes in a row with offsets
            for i, joueur in enumerate(self.jeu.joueurs): # for each player
                vote = joueur.get_carte() # get the vote of the player
                vote_box_x = vote_box_start_x + i * (vote_box_width + box_offset) # X position of the box
               

                # Determine color based on vote value
                if vote.isdigit() and (int(vote) == max_vote or int(vote) == min_vote) and max_vote != min_vote: # If the vote is a number and it is the maximum or minimum vote
                    box_color = self.RED  # Red for extreme values
                elif vote in ["?", "cafe"]: # If the vote is a question mark or coffee
                    box_color = self.BLUE   #pygame.Color('blue')  # Blue for "?" or "coffee"
                else:
                    box_color = self.WHITE  # Default color

                
                self.draw_box(vote_box_x, vote_box_y, vote_box_width, vote_box_height, box_color, f"{joueur.get_nom()}: {vote}") # Draw the box with the vote and player name

            # Handling game rules and navigation buttons 
            if self.draw_button("Back to main menu", self.screen_height - 120, self.GREY, self.GREEN): # if the back to main menu button is clicked
                self.show_result = False # set the show result to false
                self.main_menu = True # set the main menu to true
                break
            
        
            all_votes = [joueur.get_carte() for joueur in self.jeu.joueurs] # Get all votes

            # the coffee as priority over everything
            if 'cafe' in all_votes: # If the coffee card is in the votes
                for backlog in self.jeu.get_backlogs(): # for each backlog
                    if backlog.get('difficulty') == 'Skipped': # if the backlog has a difficulty value of skipped
                        backlog['difficulty'] = None # set the difficulty value to None (default value)
                self.jeu.enregistrer_backlog("Backlogs/backlog.json") # save the backlogs in a json file
                # wait 1 second 
                pygame.time.wait(1000) # Wait 1 second before going back to the main menu
                self.show_result = False # set the show result to false
                self.main_menu = True # set the main menu to true
                break
            
            # the ? as priority over everything except the coffee
            elif '?' in all_votes: # If the question mark card is in the votes
                if self.draw_button("Skip this backlog", self.screen_height - 200, self.GREY, self.GREEN): # if the skip this backlog button is clicked
                    self.jeu.set_difficulty_backlog('Skipped')  # Mark current backlog as skipped
                    self.jeu.set_joueur_actif(1)  # Reset active player for next backlog
                    self.start_menu = True  # Proceed to next backlog
                    self.show_result = False # Stop showing the result
                    break
                break
            
            elif self.medianne_clicked or self.moyenne_clicked : # If the medianne or moyenne button is clicked
                numeric_votes = [int(vote) for vote in all_votes if vote.isdigit()] # Get only numeric votes
                if self.medianne_clicked: # If the medianne button is clicked
                    if self.draw_button("Validate votes", self.screen_height - 200, self.GREY, self.GREEN): # if the validate votes button is clicked                       
                        medianne = self.jeu.medianne(numeric_votes) # Calculate the medianne
                        self.jeu.set_difficulty_backlog(medianne)  # Set the difficulty of the backlog to the medianne
                        self.jeu.set_joueur_actif(1) # Reset active player for next backlog go back to the first player
                        self.start_menu = True  # Proceed to next backlog
                        self.show_result = False # Stop showing the result
                        break
                    break
                
                elif self.moyenne_clicked: # If the moyenne button is clicked
                    if self.draw_button("Validate votes", self.screen_height - 200, self.GREY, self.GREEN): # if the validate votes button is clicked                
                        moyenne = int(sum(numeric_votes) / len(numeric_votes)) # Calculate the moyenne   
                        self.jeu.set_difficulty_backlog(moyenne) # Set the difficulty of the backlog to the moyenne
                        self.jeu.set_joueur_actif(1) # Reset active player for next backlog go back to the first player
                        self.start_menu = True # Proceed to next backlog
                        self.show_result = False # Stop showing the result
                        break
                    break
                    
            
            elif self.strictes_clicked: # If the strictes button is clicked
                if len(set(numeric_votes)) == 1: # If all votes are the same
                    if self.draw_button("Validate votes", self.screen_height - 200, self.GREY, self.GREEN): # if the validate votes button is clicked
                        self.jeu.set_difficulty_backlog(all_votes[0]) # Set the difficulty of the backlog to the first vote
                        self.jeu.set_joueur_actif(1) # Reset active player for next backlog go back to the first player
                        self.start_menu = True # Proceed to next backlog
                        self.show_result = False # Stop showing the result
                        break
                    break
                else:
                    if self.draw_button("Restart vote", self.screen_height - 200, self.GREY, self.GREEN): # if the restart vote button is clicked
                        self.jeu.set_joueur_actif(1) # Reset active player for next backlog go back to the first player
                        self.start_menu = True # Proceed to next backlog
                        self.show_result = False # Stop showing the result
                        break
                    break
                
            else:
                self.show_result = False # Stop showing the result
                self.start_menu = True # Proceed to next vote
                break
                    
            # Update the display
            pygame.display.update()
            for event in pygame.event.get(): # Check for events
                if event.type == pygame.QUIT: # If the user clicks the X in the top right corner, quit the game
                    pygame.quit() # quit pygame
                    sys.exit() # quit python

    
    
    def run(self):
        """ Method for running the game """
        pygame.init() # Initialize pygame
        
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height)) # Set screen size
        pygame.display.set_caption('Planning Poker Game') # Set window title
        
        running = True # Boolean to keep the loop running
        while running: # while the loop is running
            for event in pygame.event.get(): # Check for events
                if event.type == pygame.QUIT:   # If the user clicks the X in the top right corner, quit the game
                    running = False # Stop the loop
                    pygame.quit() # quit pygame
                    sys.exit() # quit python
                    
            self.screen.fill(self.WHITE) # Fill screen with white (background)
            
            # handle the different menus
            if self.main_menu: 
                self.main_menu_loop()  
                    
            elif self.rules_menu:
                self.rules_menu_loop()
                
            elif self.load_menu:
                self.load_menu_loop()
                
            elif self.start_menu:
                self.start_menu_loop()
                
            elif self.show_result:
                self.show_result_loop()    
                
            elif self.createBacklog_menu:
                self.createBacklog_menu_loop()
                
            pygame.display.update()
        
        pygame.quit()
        sys.exit()
        
        