import pygame
import sys
import json
from os import path
from grid import Grid
from actor import Player, Warrior, Archer, Rock, Bush
from stats import GameStats
from game_fonction import update_screen, check_key_strokes, CountDown, Scoreboard, check_event
from random import randrange
from button import Button

ENNEMY_NUMBER = 10

def setup():
    "Set the game up"
    global screen, settings, game_grid, player, sb, count_down, stats
    # Initialise pygame
    pygame.init()
    # Load the settings from json file.
    settings = []
    with open(path.join(sys.path[0], 'settings.json'), 'r') as json_file:
        settings = json.load(json_file)
    
    # Set the screen to game resolution.
    screen = pygame.display.set_mode((tuple(settings["resolution"])))#, pygame.FULLSCREEN)
    # screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN ) # For that piece of shit raspberry
  
    # pygame.display.toggle_fullscreen()
    
    # Change title
    pygame.display.set_caption("Super Haar Cascade Commander !")

    # Create sructure for current game stats
    stats = GameStats(settings)
    
    # Set gride size
    game_grid = Grid(settings)

    # Create a scoreboard
    sb = Scoreboard(settings, stats, screen)
    
    # Create the player and position    
    player = Player(game_grid, stats, sb) # Init the player

    count_down = CountDown(settings, screen)


def run():
    """Main function to launch the game"""
    running = True   

    play_button = Button(settings, screen, "PRESS BUTTON TO START GAME")
    
    
    for i in range(randrange(ENNEMY_NUMBER)+1):
        game_grid.monsters[f"a{i+1}"] = (Archer(game_grid, f"a{i+1}", 
                                    [randrange(settings["grid_nb"][0]),
                                    randrange(settings["grid_nb"][1])]
        ))

    for i in range(randrange(ENNEMY_NUMBER)+1):
        game_grid.monsters[f"w{i+1}"] = (Warrior(game_grid, f"w{i+1}", 
                                    [randrange(settings["grid_nb"][0]),
                                    randrange(settings["grid_nb"][1])]
        ))
        
    for i in range(randrange(10)+1):
        game_grid.obstacles.append(Bush(game_grid, i+1, 
                          [randrange(settings["grid_nb"][0]),
                           randrange(settings["grid_nb"][1])]
        ))
        
    for i in range(randrange(10)+1):
        game_grid.obstacles.append(Rock(game_grid, i+1, 
                          [randrange(settings["grid_nb"][0]),
                           randrange(settings["grid_nb"][1])]
        ))

    TIMEREVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(TIMEREVENT, 1000) 
    
    while running:
        """Main loop of the game"""
        
        if stats.turn_status == "timer":
            pygame.time.delay(100) # Small delay 
        else:
            pygame.time.delay(10)
    
        screen.fill(settings['screen_color'])

        check_event(settings, 
                    stats, 
                    sb, 
                    play_button, 
                    count_down, 
                    player, 
                    game_grid, 
                    TIMEREVENT)

        update_screen(screen, game_grid, sb, count_down, stats, play_button)


if __name__ == "__main__":
    pass
