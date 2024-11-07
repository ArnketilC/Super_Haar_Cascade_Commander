import pygame
import sys
import json
from os import path
from grid import Grid
from actor import Player



def setup():
    "Set the game up"
    global screen, settings, game_grid
    """Main loop."""
    # Initialise pygame
    pygame.init()

    # Load the settings from json file.
    settings = []
    with open(path.join(sys.path[0], 'settings.json'), 'r') as json_file:
        settings = json.load(json_file)
    
    # Set the screen to game resolution.
    screen = pygame.display.set_mode((tuple(settings["resolution"]))  )#, pygame.FULLSCREEN)
    
    # Set gride size
    game_grid = Grid(settings)


def run():
    """Main loop of the game"""
    running = True
    player = Player() # Init the player

    while running:
        screen.fill(settings['screen_color'])
        game_grid.drawGrid(screen, pygame)
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        game_grid.drawPlayer(screen, pygame, player)
 
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            player.move("up", game_grid.grid_nb[1])
        if keys[pygame.K_DOWN]:
            player.move("down", game_grid.grid_nb[1])
        if keys[pygame.K_LEFT]:
            player.move("left", game_grid.grid_nb[0])
        if keys[pygame.K_RIGHT]:
            player.move("right", game_grid.grid_nb[0])

        pygame.display.update()

        # Exit the game using q
        if keys[pygame.K_q]:
            pygame.quit()

    # pygame.quit()
 


    
if __name__ == "__main__":
    pass
