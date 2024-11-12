import pygame
import sys
import json
from os import path
from grid import Grid
from actor import Player, Monster
from stats import GameStats
from game_fonction import update_screen, check_key_strokes, CountDown, Scoreboard


def setup():
    "Set the game up"
    global screen, settings, game_grid, player, sb, count_down
    """Main loop."""
    # Initialise pygame
    pygame.init()

    # Load the settings from json file.
    settings = []
    with open(path.join(sys.path[0], 'settings.json'), 'r') as json_file:
        settings = json.load(json_file)
    
    # Set the screen to game resolution.
    screen = pygame.display.set_mode((tuple(settings["resolution"]))  )#, pygame.FULLSCREEN)
    
    # Change title
    pygame.display.set_caption("Super Haar Cascade Commander !")
    
    # Set gride size
    game_grid = Grid(settings)
    
    # Create the player and position    
    player = Player(game_grid) # Init the player


    # Create sructure for current game stats
    stats = GameStats(settings)
    # Create a scoreboard
    sb = Scoreboard(settings, stats, screen)
    
    count_down = CountDown(settings, screen)

def run():
    """Main loop of the game"""
    running = True   


    monster = Monster(game_grid, "id1", (20,10))
    
    TIMEREVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(TIMEREVENT, 1000) 

    
    while running:
        
        pygame.time.delay(100) # Small delay 
        
        
        screen.fill(settings['screen_color'])

        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # Else we update the timer
            elif event.type == TIMEREVENT:
                count_down.up_date()

 
        keys = pygame.key.get_pressed()
        check_key_strokes(keys, player, game_grid)

        update_screen(screen, game_grid, sb, count_down)

        # Exit the game using q
        if keys[pygame.K_q]:
            pygame.quit()


    # pygame.quit()
 

if __name__ == "__main__":
    pass
