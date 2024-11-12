import pygame
import pygame.font

def check_key_strokes(keys, player, grid):
    """Check for specific keys strokes""" 
    if keys[pygame.K_UP]:
        player.queue_action("up")
    if keys[pygame.K_DOWN]:
        player.queue_action("down")
    if keys[pygame.K_LEFT]:
        player.queue_action("left")
    if keys[pygame.K_RIGHT]:
        player.queue_action("right") 

def update_screen(screen, grid, sb, countDown, player, monster):
    """Update screen."""
    # Show score board
    sb.show()    
    # Count down
    countDown.show()   
    # Draw the grid
    grid.drawGrid(screen)    
    # Update en fonction des des demandes
    pygame.display.update()


class CountDown:
    """Countdown object for handling timer"""
    def __init__(self, settings, screen) -> None:
        "Init the item"
        self.settings = settings
        self.value = settings["default_count_down"]
        
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.txt_color = (255, 255, 255)
    
        SIZE = 136
        self.font = pygame.font.SysFont(None, SIZE)
        
        self.prop_countdown()
         
    def up_date(self):
        "Update the value"
        self.value -= 1
        pygame.display.set_caption(f'Countdown: {self.value}')
        if self.value == 0:
            print('Time\'s up!')
            self.value = self.settings["default_count_down"]
            return 1
        return 0;
            
    def prop_countdown(self):
        """Prop scorboard text."""
        str_count_down = str(self.value)
        self.count_down_as_image = self.font.render(str_count_down, True, self.txt_color, self.settings["screen_color"])
        self.count_down_rect = self.count_down_as_image.get_rect()
        self.count_down_rect.right = self.screen_rect.centerx
        self.count_down_rect.top = self.count_down_rect.top

    def show(self):
        "Show the timer"
        self.prop_countdown()
        self.screen.blit(self.count_down_as_image, self.count_down_rect)
        
"""Create a scoreboard."""

import pygame.font
import pygame.sprite


class Scoreboard():
    """Create a scoreboard class."""
    
    def __init__(self, settings, stats, screen):
        """Construct scoboard screen."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings
        self.stats = stats

        self.txt_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 36)
        self.prop_score()
        self.prop_high_score()
        self.prop_level()
        
    def prop_score(self):
        """Prop scorboard text."""
        str_score = f"Score : {self.stats.score}"
        self.score_as_image = self.font.render(str_score, True, self.txt_color, self.settings["screen_color"])
        self.score_rect = self.score_as_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prop_high_score(self):
        """Prop scorboard  high score text."""
        high_score = int(round(self.stats.high_score, -1))
        str_high_score = "High Score : {:,}".format(high_score)
        self.high_as_image = self.font.render(str_high_score, True, self.txt_color, self.settings["screen_color"])
        self.high_score_rect = self.high_as_image.get_rect()
        self.high_score_rect.left = self.screen_rect.left
        self.high_score_rect.top = self.score_rect.top

    def prop_level(self):
        """Prop scorboard level text."""
        str_level = f"Level : {self.stats.level}"
        self.level_as_image = self.font.render(str_level, True, self.txt_color, self.settings["screen_color"])
        self.level_rect = self.level_as_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom

    def show(self):
        """Draw score screen."""
        self.screen.blit(self.score_as_image, self.score_rect)
        self.screen.blit(self.high_as_image, self.high_score_rect)
        self.screen.blit(self.level_as_image, self.level_rect)

