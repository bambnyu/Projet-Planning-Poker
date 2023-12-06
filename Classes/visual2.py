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
        self.show_result = False #!!!
        
        #state variables for rules menu buttons
        self.strictes_clicked = True
        self.moyenne_clicked = False
        self.medianne_clicked = False
        
        # Define colors
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.GREY = (200, 200, 200)
        self.GREEN = (0, 200, 0)
        self.DARK_GREEN = (0, 100, 0)
        self.RED = (200, 0, 0)
        
        #set up screen
        self.screen_width, self.screen_height = 800, 600
        
        # Define button properties
        self.button_width, self.button_height = 200, 50
        self.button_start_x = self.screen_width // 2 - self.button_width // 2
        self.button_start_y = 150
        self.button_gap = 70

        # description test
        self.description_posX =  3.5 * self.screen_width // 5




    def draw_button(self, text, y, active_color, inactive_color, clicked=False):
        """ Draws a button on the screen  """
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if clicked:
            pygame.draw.rect(self.screen, active_color, [self.button_start_x, y, self.button_width, self.button_height])
        elif self.button_start_x < mouse[0] < self.button_start_x + self.button_width and y < mouse[1] < y + self.button_height:
            pygame.draw.rect(self.screen, active_color, [self.button_start_x, y, self.button_width, self.button_height])
            if click[0] == 1:
                return True
        else:
            pygame.draw.rect(self.screen, inactive_color, [self.button_start_x, y, self.button_width, self.button_height])

        small_text = pygame.font.Font("freesansbold.ttf", 20)
        text_surf, text_rect = self.text_objects(text, small_text)
        text_rect.center = ((self.button_start_x + (self.button_width // 2)), (y + (self.button_height // 2)))
        self.screen.blit(text_surf, text_rect)
        
        
        
    def draw_button_anywhere(self, text, x, y, width, active_color, inactive_color, clicked=False):
        """ Draws a button on the screen  """
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if clicked:
            pygame.draw.rect(self.screen, active_color, [x, y, width, self.button_height])
        elif x < mouse[0] < x +width and y < mouse[1] < y + self.button_height:
            pygame.draw.rect(self.screen, active_color, [x, y, width, self.button_height])
            if click[0] == 1:
                return True
        else:
            pygame.draw.rect(self.screen, inactive_color, [x, y, width, self.button_height])

        small_text = pygame.font.Font("freesansbold.ttf", 20)
        text_surf, text_rect = self.text_objects(text, small_text)
        text_rect.center = ((x + (width // 2)), (y + (self.button_height // 2)))
        self.screen.blit(text_surf, text_rect)
        
        
    def text_objects(self, text, font):
        """ Creates a text object """
        text_surface = font.render(text, True, self.BLACK)
        return text_surface, text_surface.get_rect()
    
    
    def wrap_text(self, text, max_chars):
        """Wraps text into multiple lines based on the maximum characters per line."""
        words = text.split()
        wrapped_lines = []
        current_line = ""
        for word in words:
            if len(current_line + word) <= max_chars:
                current_line += word + " "
            else:
                wrapped_lines.append(current_line)
                current_line = word + " "
        if current_line:
            wrapped_lines.append(current_line)
        return wrapped_lines
    
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
                
        small_text = pygame.font.Font("freesansbold.ttf", 20)
        wrapped_text = self.wrap_text(description, 20) # 20 characters per line
        y_offset = -20
        for line in wrapped_text:
            text_surf, text_rect = self.text_objects(line, small_text)
            text_rect.topleft = (self.description_posX, 200 + y_offset)
            self.screen.blit(text_surf, text_rect)
            y_offset += 30
        
    def open_file_dialog(self):
        """Opens a file dialog and returns the selected file path."""
        import tkinter as tk
        from tkinter import filedialog

        # Hide the main Tkinter window
        root = tk.Tk()
        root.withdraw()

        # Open the file dialog
        file_path = filedialog.askopenfilename()
        return file_path
        
    def rules_menu_loop(self):
        """Loop for the rules menu"""
        
        if self.strictes_clicked:
            self.display_rule_description("strictes")
        elif self.moyenne_clicked:
            self.display_rule_description("moyenne")
        elif self.medianne_clicked:
            self.display_rule_description("mediane")
                
                
        if self.draw_button("Strictes", self.button_start_y, self.GREY, self.GREEN, self.strictes_clicked):
            self.strictes_clicked = True
            self.moyenne_clicked = False
            self.medianne_clicked = False
        if self.draw_button("Moyenne", self.button_start_y + self.button_gap, self.GREY, self.GREEN, self.moyenne_clicked):
            self.strictes_clicked = False
            self.moyenne_clicked = True
            self.medianne_clicked = False
        if self.draw_button("Medianne", self.button_start_y + 2 * self.button_gap, self.GREY, self.GREEN, self.medianne_clicked):
            self.strictes_clicked = False
            self.moyenne_clicked = False
            self.medianne_clicked = True
        if self.draw_button("Back to main menu", self.button_start_y + 3 * self.button_gap, self.GREY, self.GREEN):
            self.rules_menu = False
            self.main_menu = True
        
    
    def main_menu_loop(self):
        """Loop for the main menu"""
        if self.draw_button("Start", self.button_start_y, self.GREY, self.GREEN):
            self.main_menu = False
            self.load_menu = True
        if self.draw_button("Rules", self.button_start_y + self.button_gap, self.GREY, self.GREEN):
            self.main_menu = False
            self.rules_menu = True
        if self.draw_button("Quit", self.button_start_y + 2 * self.button_gap, self.GREY, self.RED):
            pygame.quit()
            sys.exit()
            
    def load_menu_loop(self):
        """Loop for the load menu"""
        # Text input box properties
        #wait 1 second
        pygame.time.wait(100) # so it doesn't register the click on the load game button as a click on the start button
        
        input_box = pygame.Rect(400, 225, 140, 40)  # x, y, width, height
        color_inactive = pygame.Color('lightskyblue3')
        color_active = pygame.Color('dodgerblue2')
        color = color_inactive
        active = False
        text = ''
        font = pygame.font.Font(None, 32)

        players = []  # List to store player names
        loop_keyboard = True
        
        file_path = None

        while loop_keyboard:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

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
                            print("Added player:", text)  # For demonstration
                            text = ''  # Clear the text box after adding
                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        else:
                            text += event.unicode

            # Render the current text.
            txt_surface = font.render(text, True, color)
            # Resize the box if the text is too long.
            width = max(200, txt_surface.get_width() + 10)
            input_box.w = width

            # Drawing the screen and buttons
            self.screen.fill(self.WHITE)

            if file_path == None:
                if self.draw_button("Load Game (none)", self.button_start_y, self.GREY, self.GREEN):
                    print("Load Game clicked")
                    ## open file from your computer and load it in a variable
                    file_path = self.open_file_dialog()
                    if file_path:
                        print("Selected file:", file_path)
                        # Here, you can call your method to load and process the game data from the selected file
                        self.jeu.charger_backlog(file_path)
                    else:
                        print("No file selected")
                        file_path = None
            else:
                if self.draw_button("Load Game (done)", self.button_start_y, self.GREY, self.DARK_GREEN):
                    print("Load Game clicked")
                    ## open file from your computer and load it in a variable
                    file_path = self.open_file_dialog()
                    if file_path:
                        print("Selected file:", file_path)
                        # Here, you can call your method to load and process the game data from the selected file
                        self.jeu.charger_backlog(file_path)
                    else:
                        print("No file selected")
                        file_path = None

                                              
            if self.draw_button("Start", self.button_start_y + 2 * self.button_gap, self.GREY, self.DARK_GREEN):    
                print("Start clicked")
                if len(self.jeu.joueurs) > 0 and file_path != None:
                    self.load_menu = False
                    self.start_menu = True
                    loop_keyboard = False
                if len(self.jeu.joueurs) > 0:
                    self.load_menu = False
                    self.createBacklog_menu = True
                    loop_keyboard = False
            if self.draw_button("Back to main menu", self.button_start_y + 3 * self.button_gap, self.GREY, self.GREEN):
                self.load_menu = False
                self.main_menu = True
                loop_keyboard = False
                
            # Add player text
            self.screen.blit(font.render("Add Player :", True, self.BLACK), (self.button_start_x-50, self.button_start_y + self.button_gap+15))    
            # at the bottom of the screen, display the list of players
            self.screen.blit(font.render("Players :", True, self.BLACK), (self.button_start_x-50, self.button_start_y + 4*self.button_gap+15))
            # delete empty players
            players = [joueur.get_nom() for joueur in self.jeu.joueurs]       
            wrapped_text = self.wrap_text(str(players), 78) # 20 characters per line
            y_offset = -20
            for line in wrapped_text:
                text_surf, text_rect = self.text_objects(line, font)
                text_rect.topleft = (50, self.button_start_y + 5*self.button_gap+15 + y_offset)
                self.screen.blit(text_surf, text_rect)
                y_offset += 30

            # Blit the text box
            self.screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
            pygame.draw.rect(self.screen, color, input_box, 2)

            pygame.display.update()


    def createBacklog_menu_loop(self):
        """Loop for the create backlog menu"""
        #### HERE WE NEED AN INPUT BOX TO ENTER THE DESCRIPTION OF BACKLOGS
        ### and show the already created backlogs on the bottom of the screen
        ### a button to go back to the main menu
        ### a button to go to the start menu
            # Input box setup
        input_box = pygame.Rect(300, 200, 200, 60)  # x, y, width, height
        color_inactive = pygame.Color('lightskyblue3')
        color_active = pygame.Color('dodgerblue2')
        color = color_inactive
        active = False
        text = ''
        font = pygame.font.Font(None, 32)

        backlog_description = ''

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Event handling for the input box
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_box.collidepoint(event.pos):
                        active = not active
                    else:
                        active = False
                    color = color_active if active else color_inactive

                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                            backlog_description = text
                            self.jeu.ajouter_backlog((backlog_description))  # Add the backlog to your game object
                            text = ''
                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        else:
                            text += event.unicode

            self.screen.fill(self.WHITE)

            # Display existing backlogs
            # This can be a loop displaying each backlog item. Here's a simple example:
            y_offset = 150
            for backlog in self.jeu.get_backlogs():
                self.screen.blit(font.render(backlog['description'], True, self.BLACK), (50, y_offset))
                y_offset += 40

            # Navigation buttons
            if self.draw_button("Back to main menu", self.screen_height - 120, self.GREY, self.GREEN):
                self.createBacklog_menu = False
                self.main_menu = True
                break
            if self.draw_button("Start Game", self.screen_height - 70, self.GREY, self.DARK_GREEN):
                # enregistrer le backlog dans un fichier json
                if backlog_description:
                    self.jeu.enregistrer_backlog("Backlogs/backlog.json")
                    
                    self.createBacklog_menu = False
                    self.start_menu = True
                    break

            # Input box for new backlog
            txt_surface = font.render(text, True, color)
            width = max(200, txt_surface.get_width() + 10)
            input_box.w = width
            self.screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
            pygame.draw.rect(self.screen, color, input_box, 2)

            pygame.display.flip()
            
    def vote_menu(self):

        clicked_vote = False
        while not clicked_vote:
            self.screen.fill(self.DARK_GREEN)

            backlog_box = pygame.Rect(0, 0, self.screen_width, 100)
            pygame.draw.rect(self.screen, self.WHITE, backlog_box)

            # Display the first backlog without a difficulty value
            small_text = pygame.font.Font("freesansbold.ttf", 20)
            description = None

            for backlog in self.jeu.get_backlogs():
                if not backlog.get('difficulty'):
                    description = backlog.get('description')
                    break

            if description:
                text_surf, text_rect = self.text_objects(description, small_text)
                text_rect.center = ((self.screen_width // 2), (50))
                self.screen.blit(text_surf, text_rect)



            card_values = ["0", "1", "2", "3", "5", "8", "13", "20", "40", "100", "?", "cafe"]
            card_start_y = self.screen_height // 2 - 50
            card_gap = 75
            card_width = 50
            card_start_x = 65

            for i in range(int(len(card_values) / 2)):
                if self.draw_button_anywhere(card_values[i], card_start_x + i * (card_width + card_gap), card_start_y, card_width, self.WHITE, self.WHITE):
                    print(card_values[i] + " clicked")
                    clicked_vote = True
                    self.jeu.joueurs[self.jeu.get_joueur_actif()-1].set_carte(card_values[i])
                    # Handle the vote here, e.g., update backlog difficulty

            for i in range(0, int(len(card_values) / 2)):
                if self.draw_button_anywhere(card_values[i+6], card_start_x + i * (card_width + card_gap), card_start_y + 150, card_width, self.WHITE, self.WHITE):
                    print(card_values[i+6] + " clicked")
                    clicked_vote = True
                    self.jeu.joueurs[self.jeu.get_joueur_actif()-1].set_carte(card_values[i+6])
                    # Handle the vote here 

            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

        # After voting, you might want to go back to the start menu or handle the next action
        self.jeu.set_joueur_actif(self.jeu.get_joueur_actif() + 1)
        print("joueur actif : ", self.jeu.get_joueur_actif()) #!
        self.start_menu = True  # Example: Going back to the start menu
                

        
        
        
        
    def start_menu_loop(self):
        self.screen.fill(self.DARK_GREEN)

        
        backlog_box = pygame.Rect(0, 0, self.screen_width, 100)  # Position and size of the rectangle
        pygame.draw.rect(self.screen, self.WHITE, backlog_box)  # Draw the rectangle

        # Display the first backlog without a difficulty value
        small_text = pygame.font.Font("freesansbold.ttf", 20)
        description = None

        for backlog in self.jeu.get_backlogs():
            if not backlog.get('difficulty'):  # If the backlog doesn't have a difficulty value
                description = backlog.get('description')
                break

        if description:
            text_surf, text_rect = self.text_objects(description, small_text)
            text_rect.center = ((self.screen_width // 2), (50))
            self.screen.blit(text_surf, text_rect)
        else:
            # Handle the case where all backlogs have difficulty values or there are no backlogs
            text_surf, text_rect = self.text_objects("No backlogs available", small_text)
            text_rect.center = ((self.screen_width // 2), (50))
            self.screen.blit(text_surf, text_rect)
            pygame.time.wait(1000)  # Wait 1 second before going back to the main menu
            self.start_menu = False
            self.main_menu = True

        if self.jeu.get_joueur_actif() <= len(self.jeu.get_joueurs()):
            player_name = self.jeu.get_joueurs()[self.jeu.get_joueur_actif()-1]
            player_box = pygame.Rect(250, 150, 300, 50)
            pygame.draw.rect(self.screen, self.WHITE, player_box)
            player_text_surf, player_text_rect = self.text_objects(f"Active Player: {player_name}", small_text)
            player_text_rect.center = (player_box.centerx, player_box.centery)
            self.screen.blit(player_text_surf, player_text_rect)
        else:
            print("We finished all the players")
            #### we need to check all votes considering the rule choosen
            #### and display the result screen
            self.show_result_screen()

        # Go button
        go_button_y = self.screen_height // 2 + 50
        go_button_text = "Go"

        if self.draw_button(go_button_text, go_button_y, self.GREY, self.GREEN):
            print("Go clicked")
            self.vote_menu()
            
            
        back_button_y = self.screen_height - self.button_height - 10  # Position it near the bottom of the screen
        back_button_text = "Back to Main Menu"

        if self.draw_button(back_button_text, back_button_y, self.GREY, self.GREEN):
            #enregistrer le backlog dans un fichier json
            
            self.jeu.enregistrer_backlog("Backlogs/backlog.json")
            self.start_menu = False
            self.main_menu = True  # Change state back to main menu
         


    def show_result_screen(self):
        # Transition to the result screen
        self.show_result= True
        self.start_menu = False
        

    def show_result_loop(self):
        running = True
        while running:
            self.screen.fill(self.DARK_GREEN)
            
            backlog_box = pygame.Rect(0, 0, self.screen_width, 100)  # Position and size of the rectangle
            pygame.draw.rect(self.screen, self.WHITE, backlog_box)  # Draw the rectangle

            # Display the first backlog without a difficulty value
            small_text = pygame.font.Font("freesansbold.ttf", 20)
            description = None

            for backlog in self.jeu.get_backlogs():
                if not backlog.get('difficulty'):  # If the backlog doesn't have a difficulty value
                    description = backlog.get('description')
                    break

            if description:
                text_surf, text_rect = self.text_objects(description, small_text)
                text_rect.center = ((self.screen_width // 2), (50))
                self.screen.blit(text_surf, text_rect)
            else:
                # Handle the case where all backlogs have difficulty values or there are no backlogs
                text_surf, text_rect = self.text_objects("No backlogs available", small_text)
                text_rect.center = ((self.screen_width // 2), (50))
                self.screen.blit(text_surf, text_rect)
                pygame.time.wait(1000)  # Wait 1 second before going back to the main menu
                self.start_menu = False
                self.main_menu = True

            # Define offset between boxes
            box_offset = 10  # Space between boxes

            # Prepare to detect extreme values
            votes = [joueur.get_carte() for joueur in self.jeu.joueurs]
            numeric_votes = [int(vote) for vote in votes if vote.isdigit()]
            max_vote = max(numeric_votes, default=None)
            min_vote = min(numeric_votes, default=None)

            # Calculate the width and position for the vote boxes
            num_players = len(self.jeu.joueurs)
            total_offset = box_offset * (num_players - 1)
            vote_box_width = (self.screen_width - 200 - total_offset) // num_players
            vote_box_height = 40
            vote_box_start_x = (self.screen_width - ((vote_box_width + box_offset) * num_players - box_offset)) // 2
            vote_box_y = self.screen_height // 2 - vote_box_height // 2

            # Display the votes in a row with offsets
            for i, joueur in enumerate(self.jeu.joueurs):
                vote = joueur.get_carte()
                vote_box_x = vote_box_start_x + i * (vote_box_width + box_offset)
                vote_box = pygame.Rect(vote_box_x, vote_box_y, vote_box_width, vote_box_height)

                # Determine color based on vote value
                if vote.isdigit() and (int(vote) == max_vote or int(vote) == min_vote):
                    box_color = self.RED  # Red for extreme values
                elif vote in ["?", "cafe"]:
                    box_color = pygame.Color('blue')  # Blue for "?" or "coffee"
                else:
                    box_color = self.WHITE  # Default color

                pygame.draw.rect(self.screen, box_color, vote_box)
                vote_text = f"{joueur.get_nom()}: {vote}"
                vote_text_surf, vote_text_rect = self.text_objects(vote_text, pygame.font.Font("freesansbold.ttf", 20))
                vote_text_rect.center = (vote_box.centerx, vote_box.centery)
                self.screen.blit(vote_text_surf, vote_text_rect)

            # Handling game rules and navigation buttons as before...
            # ...

            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            

    
    
    def run(self):
        # Method for running the game
        pygame.init()
        
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption('Planning Poker Game')
        
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()
                    
            self.screen.fill(self.WHITE)
            
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
        
        
if __name__ == "__main__":
    visual = Visual()
    visual.run()
    