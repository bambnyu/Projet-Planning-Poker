import pygame
import sys

class Visual:
    def __init__(self):
        
        # Game state
        self.main_menu = True
        self.rules_menu = False
        self.load_menu = False
        
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
        if self.draw_button("Load Game", self.button_start_y, self.GREY, self.GREEN):
            print("Load Game clicked")
        if self.draw_button("Players", self.button_start_y + self.button_gap, self.GREY, self.GREEN):
            print("Players clicked")
        if self.draw_button("Start", self.button_start_y + 2 * self.button_gap, self.GREY, self.DARK_GREEN):    
            print("Start clicked")
        if self.draw_button("Back to main menu", self.button_start_y + 3 * self.button_gap, self.GREY, self.GREEN):
            self.load_menu = False
            self.main_menu = True
    
    
    
    
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
                
            pygame.display.update()
        pygame.quit()
        sys.exit()
        
        
if __name__ == "__main__":
    visual = Visual()
    visual.run()
    