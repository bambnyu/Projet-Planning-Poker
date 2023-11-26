import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the window
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Planning Poker Game')

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (200, 200, 200)
GREEN = (0, 200, 0)

# Define button properties
button_width, button_height = 200, 50
button_start_x = screen_width // 2 - button_width // 2
button_start_y = 150
button_gap = 70

# Game states
main_menu = True
rules_menu = False

# Function definitions

def draw_button(text, y, active_color, inactive_color):
    """Draws a button with text on it. If the mouse is hovering over the button, the button color changes."""
    mouse = pygame.mouse.get_pos() # Get mouse position
    click = pygame.mouse.get_pressed() # Get mouse click
    # If mouse is hovering over button, change color
    if button_start_x < mouse[0] < button_start_x + button_width and y < mouse[1] < y + button_height:
        pygame.draw.rect(screen, active_color, [button_start_x, y, button_width, button_height]) # Draw button
        # If button is clicked, return True
        if click[0] == 1:
            return True
    else:
        # If mouse is not hovering over button, draw button with inactive color
        pygame.draw.rect(screen, inactive_color, [button_start_x, y, button_width, button_height])

    # Draw text on button
    small_text = pygame.font.Font("freesansbold.ttf", 20) # Define font
    text_surf, text_rect = text_objects(text, small_text) # Render text
    text_rect.center = ((button_start_x + (button_width // 2)), (y + (button_height // 2))) # Center text on button
    screen.blit(text_surf, text_rect) # Draw text
    # If button is not clicked, return False
    return False

def text_objects(text, font):
    """Renders text and returns the text surface and the rectangle around the text."""
    text_surface = font.render(text, True, BLACK) # Render text
    return text_surface, text_surface.get_rect() # Return text surface and rectangle around text

# Main game loop
running = True # Boolean to keep game running
while running:
    for event in pygame.event.get(): # Check for events
        if event.type == pygame.QUIT: # If the user clicks the X in the top right corner, quit the game
            running = False 

    screen.fill(WHITE) # Fill screen with white (background)

    if main_menu: # If in main menu
        if draw_button("Start New Game", button_start_y, GREY, GREEN):
            print("Start New Game clicked")
        if draw_button("Load Game", button_start_y + button_gap, GREY, GREEN):
            print("Load Game clicked")
        if draw_button("Rules", button_start_y + 2 * button_gap, GREY, GREEN):
            # Go to rules menu
            main_menu = False
            rules_menu = True
        if draw_button("Quit", button_start_y + 3 * button_gap, GREY, GREEN):
            # Quit game
            running = False
    
    if rules_menu: # If in rules menu
        if draw_button("Classique", button_start_y, GREY, GREEN):
            print("Classique rules selected")
        if draw_button("Strictes", button_start_y + button_gap, GREY, GREEN):
            print("Strictes rules selected")
        if draw_button("Moyenne", button_start_y + 2 * button_gap, GREY, GREEN):
            print("Moyenne rules selected")
        if draw_button("Médiane", button_start_y + 3 * button_gap, GREY, GREEN):
            print("Médiane rules selected")
        if draw_button("Back to Main Menu", button_start_y + 4 * button_gap, GREY, GREEN):
            # Go back to main menu
            rules_menu = False 
            main_menu = True
    # Update screen
    pygame.display.flip()
# Quit game
pygame.quit()
sys.exit()
