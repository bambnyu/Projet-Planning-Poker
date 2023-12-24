from Visual import *

class Board :
    ##### Constructor #####
    def __init__(self):
        self.visual = Visual()
    
    ##### Methods #####
    
    def run(self):
        """ Method for running the game """
        pygame.init() # Initialize pygame
        
        self.visual.screen = pygame.display.set_mode((self.visual.screen_width, self.visual.screen_height)) # Set screen size
        pygame.display.set_caption('Planning Poker Game') # Set window title
        
        running = True # Boolean to keep the loop running
        while running: # while the loop is running
            for event in pygame.event.get(): # Check for events
                self.visual.check_for_quit(event) # Check if the user wants to quit
                    
            self.visual.screen.fill(self.visual.WHITE) # Fill screen with white (background)
            # handle the different menus
            if self.visual.main_menu: 
                self.main_menu_loop()           
            elif self.visual.rules_menu:
                self.rules_menu_loop()
            elif self.visual.load_menu:
                self.load_menu_loop()
            elif self.visual.start_menu:
                self.start_menu_loop()
            elif self.visual.show_result:
                self.show_result_loop()    
            elif self.visual.createBacklog_menu:
                self.createBacklog_menu_loop()
            
            pygame.display.update()
        self.visual.quit_game() # quit pygame
    
    
    def main_menu_loop(self):
        """Loop for the main menu"""
        if self.visual.draw_button_general("Start", self.visual.button_start_x, self.visual.button_start_y, self.visual.button_width, self.visual.button_height, self.visual.GREY, self.visual.GREEN): # if the start button is clicked
            self.visual.change_state("load_menu") # change the state to load menu
        if self.visual.draw_button_general("Rules", self.visual.button_start_x, self.visual.button_start_y + self.visual.button_gap, self.visual.button_width, self.visual.button_height, self.visual.GREY, self.visual.GREEN): # if the rules button is clicked
            self.visual.change_state("rules_menu") # change the state to rules menu
        if self.visual.draw_button_general("Quit", self.visual.button_start_x, self.visual.button_start_y + 2 * self.visual.button_gap, self.visual.button_width, self.visual.button_height, self.visual.GREY, self.visual.RED):
            self.visual.quit_game() # quit pygame
        
        
    def rules_menu_loop(self):
        """Loop for the rules menu"""
        if self.visual.strictes_clicked: # if the strictes button is clicked
            self.visual.display_rule_description("strictes")
        elif self.visual.moyenne_clicked: # if the moyenne button is clicked
            self.visual.display_rule_description("moyenne")
        elif self.visual.medianne_clicked: # if the medianne button is clicked
            self.visual.display_rule_description("medianne")
        elif self.visual.majorite_abs_clicked: # if the majorite absolue button is clicked
            self.visual.display_rule_description("majorite_abs")
        elif self.visual.majorite_rel_clicked: # if the majorite relative button is clicked
            self.visual.display_rule_description("majorite_rel")
                
        if self.visual.draw_button_general("Strict", self.visual.button_start_x, self.visual.button_start_y, self.visual.button_width, self.visual.button_height, self.visual.GREY, self.visual.GREEN, self.visual.strictes_clicked): # if the strictes button is clicked
            self.visual.change_difficulty("strictes") # change the difficulty to strictes
        if self.visual.draw_button_general("Average", self.visual.button_start_x, self.visual.button_start_y + self.visual.button_gap, self.visual.button_width, self.visual.button_height, self.visual.GREY, self.visual.GREEN, self.visual.moyenne_clicked): # if the moyenne button is clicked   
            self.visual.change_difficulty("moyenne") # change the difficulty to moyenne
        if self.visual.draw_button_general("Median", self.visual.button_start_x, self.visual.button_start_y + 2 * self.visual.button_gap, self.visual.button_width, self.visual.button_height, self.visual.GREY, self.visual.GREEN,self.visual.medianne_clicked): # if the medianne button is clicked
            self.visual.change_difficulty("medianne") # change the difficulty to medianne
        if self.visual.draw_button_general("Absolute majority", self.visual.button_start_x, self.visual.button_start_y + 3 * self.visual.button_gap, self.visual.button_width, self.visual.button_height, self.visual.GREY, self.visual.GREEN, self.visual.majorite_abs_clicked): # if the majorite absolue button is clicked
            self.visual.change_difficulty("majorite_abs") # change the difficulty to majorite absolue
        if self.visual.draw_button_general("Relative majority", self.visual.button_start_x, self.visual.button_start_y + 4 * self.visual.button_gap, self.visual.button_width, self.visual.button_height, self.visual.GREY, self.visual.GREEN, self.visual.majorite_rel_clicked): # if the majorite relative button is clicked
            self.visual.change_difficulty("majorite_rel") # change the difficulty to majorite relative
        if self.visual.draw_button_general("Back to main menu", self.visual.button_start_x, self.visual.button_start_y + 5 * self.visual.button_gap, self.visual.button_width, self.visual.button_height, self.visual.GREY, self.visual.GREEN): # if the back to main menu button is clicked
            self.visual.change_state("main_menu") # change the state to main menu
            
            
    def createBacklog_menu_loop(self):
        """Loop for the create backlog menu"""
        input_box = pygame.Rect(300, 200, 200, 60)  # x, y, width, height
        color_inactive = self.visual.BLUE # color of the input box when it is not clicked
        color_active = self.visual.GREY # color of the input box when it is clicked
        color = color_inactive # default color of the input box
        active = False # default state of the input box
        text = '' # default text of the input box
        font = pygame.font.Font(None, 32) # font of the input box
        backlog_description = '' # default backlog description

        # Loop for the create backlog menu
        while True: # while the loop is running                     
            for event in pygame.event.get(): # Check for events
                self.visual.check_for_quit(event) # Check if the user wants to quit
                # Event handling for the input box
                active, color = self.visual.input_box_toggle(event, input_box, active, color, color_active, color_inactive) # toggle the input box
                text = self.visual.handle_input_box_events(event, active, text, backlog_description) # handle the input box events
                
            self.visual.screen.fill(self.visual.WHITE) # Fill screen with white (background)
            instruction_text = "Enter the description of your backlogs in the box below" # Instruction text
            self.visual.screen.blit(font.render(instruction_text, True, self.visual.BLACK), (110, 50)) # Display instruction text
            # Display existing backlogs
            y_offset = 150  # offset for the y position of the text
            for backlog in self.visual.jeu.get_backlogs(): # for each backlog
                self.visual.screen.blit(font.render(backlog['description'], True, self.visual.BLACK), (50, y_offset)) # Display the description of the backlog
                y_offset += 40 # increase the offset for the next line

            # Navigation buttons
            if self.visual.draw_button_general("Back to main menu", self.visual.button_start_x , self.visual.screen_height - 140, self.visual.button_width, self.visual.button_height, self.visual.GREY, self.visual.GREEN): # if the start button is clicked
                self.visual.change_state("main_menu") # change the state to main menu
                break
            if self.visual.draw_button_general("Start Game", self.visual.button_start_x , self.visual.screen_height - 70, self.visual.button_width, self.visual.button_height, self.visual.GREY, self.visual.DARK_GREEN): # if the start button is clicked
                # enregistrer le backlog dans un fichier json
                if len(self.visual.jeu.backlogs)!=0: # if there is at least one backlog
                    self.visual.jeu.enregistrer_backlog("Code/Backlogs/backlog.json") # save the backlogs in a json file
                    self.visual.change_state("start_menu") # change the state to start menu
                    break
                else:
                    self.visual.draw_box(225, 100, 350, 60, self.visual.RED, "Please enter at least one backlog") # Display error message
                
            self.visual.draw_box_dynamic(input_box.x, input_box.y, 200, 60, color, text, font_size=32, max_width=300)
            pygame.display.flip() # Update the screen
            
            
    def start_menu_loop(self):
        """ Loop for the start menu """
        small_text = pygame.font.Font("freesansbold.ttf", 20) # Define font
        self.visual.screen.fill(self.visual.DARK_GREEN)  # Fill screen with dark green (background)
        # Get the first backlog description without a difficulty value
        description =  self.visual.check_if_all_backlogs_have_difficulty() # check if all backlogs have difficulty values
        # Handle the case where all backlogs have difficulty values or there are no backlogs
        if description == "No backlogs available":
            self.visual.jeu.enregistrer_backlog_skipped("Code/Backlogs/backlog.json") # save the backlogs in a json file
            pygame.time.wait(1000)  # Wait 1 second before going back to the main menu
            self.visual.change_state("main_menu")  # Change state back to main menu
        if self.visual.jeu.get_joueur_actif() <= len(self.visual.jeu.get_joueurs()): # if there are still players to vote
            player_name = self.visual.jeu.get_joueurs()[self.visual.jeu.get_joueur_actif()-1]
            player_text = f"Active Player: {player_name}"
            # Use draw_box to display the active player's name
            self.visual.draw_box(250, 150, 300, 50, self.visual.WHITE, player_text, font_size=20)
        else:
            self.visual.change_state("show_result") # change the state to show result
        if self.visual.draw_button_general("Go", self.visual.button_start_x, self.visual.screen_height // 2 + 50, self.visual.button_width, self.visual.button_height, self.visual.GREY, self.visual.GREEN): # if the go button is clicked
            self.vote_menu() # go to the vote menu
        if self.visual.draw_button_general("Back to main menu", self.visual.button_start_x, self.visual.screen_height - self.visual.button_height - 10, self.visual.button_width, self.visual.button_height, self.visual.GREY, self.visual.GREEN):
            #enregistrer le backlog dans un fichier json
            self.visual.jeu.enregistrer_backlog("Code/Backlogs/backlog.json") # save the backlogs in a json file
            self.visual.start_menu = False # Change state back to main menu
            self.visual.main_menu = True  # Change state back to main menu
            
            
    def show_result_loop(self):
        """ Loop for the result screen """
        running = True # Boolean to keep the loop running
        while running: # while the loop is running
            self.visual.screen.fill(self.visual.DARK_GREEN) # Fill screen with dark green (background)
            
            # Check if all backlogs have a difficulty value and display the appropriate message
            description = self.visual.check_if_all_backlogs_have_difficulty()
            if description == "No backlogs available":
                pygame.time.wait(1000)  # Wait 1 second before going back to the main menu
                self.visual.change_state("main_menu")  # Change state back to main menu
                continue
            # Define offset between boxes
            box_offset = 10  # Space between boxes
            numeric_votes = self.visual.jeu.get_numerical_votes() # Get only numeric votes
            max_vote, min_vote = self.visual.jeu.max_min_votes() # Get the maximum and minimum votes

            # Calculate the width and position for the vote boxes
            num_players = len(self.visual.jeu.joueurs) # Number of players
            total_offset = box_offset * (num_players - 1) # Total offset between boxes
            vote_box_width = (self.visual.screen_width - 200 - total_offset) // num_players # Width of each box
            vote_box_height = 40 # Height of each box
            vote_box_start_x = (self.visual.screen_width - ((vote_box_width + box_offset) * num_players - box_offset)) // 2 # X position of the first box
            vote_box_y = self.visual.screen_height // 2 - vote_box_height // 2 # Y position of the boxes

            # Display the votes in a row with offsets
            for i, joueur in enumerate(self.visual.jeu.joueurs): # for each player
                vote = joueur.get_carte() # get the vote of the player
                vote_box_x = vote_box_start_x + i * (vote_box_width + box_offset) # X position of the box
                # Determine color based on vote value
                box_color = self.visual.vote_color(vote, max_vote, min_vote) # Determine color based on vote value
                self.visual.draw_box(vote_box_x, vote_box_y, vote_box_width, vote_box_height, box_color, vote) # Draw the box with the vote value
                
            # Handling game rules and navigation buttons 
            if self.visual.draw_button_general("Back to main menu", self.visual.button_start_x, self.visual.screen_height - 120, self.visual.button_width, self.visual.button_height, self.visual.GREY, self.visual.GREEN): # if the back to main menu button is clicked
                self.visual.change_state("main_menu") # change the state to main menu
                break
            all_votes = self.visual.jeu.get_all_votes() # Get all votes
            # the coffee as priority over everything
            if 'cafe' in all_votes: # If the coffee card is in the votes
                self.visual.cafe_vote() # do the cafe instructions
                # wait 1 second 
                pygame.time.wait(1000) # Wait 1 second before going back to the main menu
                self.visual.change_state("main_menu") # change the state to main menu
                break
            # the ? as priority over everything except the coffee
            elif '?' in all_votes: # If the question mark card is in the votes
                self.visual.question_mark_vote() # do the question mark instructions
                break
            elif self.visual.medianne_clicked or self.visual.moyenne_clicked : # If the medianne or moyenne button is clicked
                if self.visual.medianne_clicked: # If the medianne button is clicked
                    self.visual.medianne_vote() # do the moyenne instructions
                    break
                elif self.visual.moyenne_clicked: # If the moyenne button is clicked         
                    self.visual.moyenne_vote() # do the medianne instructions
                    break        
            elif self.visual.strictes_clicked: # If the strictes button is clicked
                if len(set(numeric_votes)) == 1: # If all votes are the same
                    self.visual.strictes_vote_egaux(all_votes) # do the strictes instructions
                    break
                else:
                    self.visual.strictes_vote_diff()
                    break 
            elif self.visual.majorite_abs_clicked: # If the majorite absolue button is clicked
                # If there is a majority
                val_max = -1 # default value for the majority
                for i in numeric_votes: # for each vote
                    if numeric_votes.count(i) > len(numeric_votes) / 2:
                        val_max = i # there is a majority
                        break
                if val_max==-1:
                    self.visual.majorite_abs_vote_not_exist() # do the majorite absolue instructions
                    break
                else:
                    self.visual.majorite_abs_vote_exist(val_max) # do the majorite absolue instructions
                    break
            elif self.visual.majorite_rel_clicked: # If the majorite relative button is clicked
                self.visual.majorite_rel_vote(numeric_votes)
                break
            else:
                self.visual.change_state("start_menu") # change the state to main menu
                break      
            # Update the display
            pygame.display.update()       
            for event in pygame.event.get(): # Check for events
                self.visual.check_for_quit(event) # Check if the user wants to quit
                
      
    def load_menu_loop(self):
        """Loop for the load menu"""
        # Text input box properties
        #wait 1 second
        pygame.time.wait(100) # so it doesn't register the click on the load game button as a click on the start button
        input_box = pygame.Rect(400, 225, 140, 40)  # x, y, width, height
        color_inactive = self.visual.BLUE # color of the input box when it is not clicked
        color_active = self.visual.GREY # color of the input box when it is clicked
        color = color_inactive # default color of the input box
        active = False # default state of the input box
        text = '' # default text of the input box
        font = pygame.font.Font(None, 32) # font of the input box

        players = []  # List to store player names
        loop_keyboard = True # Boolean to keep the loop running
        file_path = None # default file path
        
        while loop_keyboard: # while the loop is running
            for event in pygame.event.get(): # Check for events
                self.visual.check_for_quit(event) # Check if the user wants to quit
                active,color = self.visual.input_box_toggle(event, input_box, active, color, color_active, color_inactive) # toggle the input box
                
                #couldn't put it in the visual class because of the text variable #!!!!!!
                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                            self.visual.jeu.ajouter_joueur(Joueur(text))
                            text = ''  # Clear the text box after adding
                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1] # Remove the last character from the text box
                        else:
                            text += event.unicode # Add the entered character to the text box
                # end couldn't put it in the visual class because of the text variable #!!!!!!
                
            # Render the current text.
            txt_surface = font.render(text, True, color)
            # Resize the box if the text is too long.
            width = max(200, txt_surface.get_width() + 10)
            input_box.w = width
            # Drawing the screen and buttons
            self.visual.screen.fill(self.visual.WHITE) # Fill screen with white (background)
            if file_path == None: # if no file is selected
                if self.visual.draw_button_general("Load Game (none)", self.visual.button_start_x, self.visual.button_start_y,self.visual.button_width, self.visual.button_height, self.visual.GREY,self.visual.GREEN): # if the load game button is clicked
                    ## open file and load it in a variable
                    file_path = self.visual.open_file_dialog()
                    if file_path:
                        # load and process the game data from the selected file
                        self.visual.jeu.charger_backlog(file_path) 
                    else:
                        file_path = None # If no file is selected, set file_path to None
            else:
                if self.visual.draw_button_general("Load Game (done)", self.visual.button_start_x, self.visual.button_start_y, self.visual.button_width, self.visual.button_height, self.visual.GREY, self.visual.DARK_GREEN): # if the load game button is clicked
                    ## open file from your computer and load it in a variable
                    file_path = self.visual.open_file_dialog()
                    if file_path:
                        # Here, you can call your method to load and process the game data from the selected file
                        self.visual.jeu.charger_backlog(file_path) 
                    else:
                        file_path = None  # If no file is selected, set file_path to None
 
            if self.visual.draw_button_general("Start", self.visual.button_start_x, self.visual.button_start_y + 2 * self.visual.button_gap, self.visual.button_width, self.visual.button_height, self.visual.GREY, self.visual.DARK_GREEN): # if the start button is clicked
                if len(self.visual.jeu.joueurs) > 0 and file_path != None: # if there is at least one player and a file is selected
                    self.visual.change_state("start_menu") # change the state to start menu
                    loop_keyboard = False # stop the loop
                    break
                if len(self.visual.jeu.joueurs) > 0: # if there is at least one player but no file is selected
                    self.visual.change_state("createBacklog_menu") # change the state to create backlog menu
                    loop_keyboard = False # stop the loop
                    break
            if self.visual.draw_button_general("Back to main menu", self.visual.button_start_x, self.visual.button_start_y + 3 * self.visual.button_gap, self.visual.button_width, self.visual.button_height, self.visual.GREY, self.visual.GREEN): # if the back to main menu button is clicked    
                self.visual.change_state("main_menu") # change the state to main menu
                loop_keyboard = False # stop the loop
                break
                
            # Add player text
            self.visual.screen.blit(font.render("Add Player :", True, self.visual.BLACK), (self.visual.button_start_x-50, self.visual.button_start_y + self.visual.button_gap+15))    
            # at the bottom of the screen, display the list of players
            self.visual.screen.blit(font.render("Players :", True, self.visual.BLACK), (self.visual.button_start_x-50, self.visual.button_start_y + 4*self.visual.button_gap+15))
            # Display the list of players
            self.visual.display_players_list()         
            # Blit the text box
            self.visual.screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5)) # Blit the text.
            pygame.draw.rect(self.visual.screen, color, input_box, 2) # Blit the rect.
            pygame.display.update() # Update the screen


    def vote_menu(self):
        """Loop for the vote menu"""
        clicked_vote = False  # Boolean to keep the loop running
        while not clicked_vote:  # while the loop is running
            self.visual.screen.fill(self.visual.DARK_GREEN)  # Fill screen with dark green (background)
            # Get the first backlog description without a difficulty value
            description = self.visual.check_if_all_backlogs_have_difficulty()
            # Use draw_box to display the backlog description
            self.visual.draw_box(0, 0, self.visual.screen_width, 100, self.visual.WHITE, description, font_size=20)
            # Display the cards
            clicked_vote = self.visual.display_cards_to_vote_screens(clicked_vote) # Display the cards and check if a card is clicked

            pygame.display.update() # Update the screen
            for event in pygame.event.get(): # Check for events
                self.visual.check_for_quit(event)

        # After voting, you might want to go back to the start menu or handle the next action
        self.visual.jeu.set_joueur_actif(self.visual.jeu.get_joueur_actif() + 1) # set the active player to the next player
        self.visual.change_state("start_menu")
        
        
        
        
        
# Code by Adjame Tellier-Rozen (ROZEN)