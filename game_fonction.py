import pygame
import pygame.font
import sys
from pygame.constants import QUIT, MOUSEBUTTONDOWN, K_q, KEYDOWN
from actor import Heart


def update_screen(screen, grid, sb, countDown, stats, play_button):
    """Update screen."""
    # Show score board
    sb.show()    
    # Count down
    countDown.show()   
    # Draw the grid
    grid.drawGrid(screen)    

    # Draw the play button
    if stats.game_run is False:
        play_button.draw_button()
        
    # Update en fonction des des demandes
    pygame.display.update()
    
def check_high_score(stats, sb):
    """Check if the high score is beaten"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prop_high_score()


def check_key_strokes(key, player):
    """Check for specific keys strokes""" 
    if key == pygame.K_UP:
        player.queue_action("up")
    elif key == pygame.K_DOWN:
        player.queue_action("down")
    elif key == pygame.K_LEFT:
        player.queue_action("left")
    elif key == pygame.K_RIGHT:
        player.queue_action("right") 
    elif key == pygame.K_SPACE:
        player.queue_action("attack") 
  
def check_button_click(settings, stats, sb, play_button, mouse_x, mouse_y, clicked = False):
    """Check if the play button is pushed."""
    clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if clicked and not stats.game_run:
        pygame.mouse.set_visible(False)
        stats.game_run = True

        stats.reset(settings)


        sb.prop_high_score()
        sb.prop_score()
        sb.prop_level()
        sb.prop_player_life()
        
def check_event(settings, stats, sb, play_button, count_down, player, grid, TIMEREVENT):
    """Check for events."""
    # Check les event
    for event in pygame.event.get():
        # Check si on click sur la croix
        if event.type == QUIT:
            sys.exit()
        # Events on keydown
        elif event.type == KEYDOWN:
            if event.key == K_q:
                sys.exit()
            else:
                check_key_strokes(event.key, player)

        elif event.type == MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_button_click(settings, stats, sb, play_button, mouse_x, mouse_y)

        if stats.game_run is True:
            if event.type == TIMEREVENT and stats.turn_status == "timer":
                if count_down.up_date():
                    stats.turn_status = "player"
                    
        # GODAMMMM PYTHON 3.9
        # match stats.turn_status:
        #     case "player":
        #             stats.turn_status = player.action(grid)
        #             stats.turn_status = "monster"
        #     case "monster":
        #             for monster in grid.monsters.values():
        #                 monster.monster_queue()
        #                 monster.action(grid)
        #             player.invincibility = False # remove invincibility "frame"
        #             stats.turn_status = "timer"
        #     case _:
        #         pass
        
        # match stats.turn_status:
        if stats.turn_status =="player":
            if player.action(grid):
                stats.turn_status = "monster"
        if stats.turn_status =="monster":
            for monster in grid.monsters.values():
                if len(monster.action_queue) == 0:
                    monster.monster_queue()
                monster.action(grid)

            # if finished_monster == len(grid.monsters):
            player.invincibility = False # remove invincibility "frame"
            stats.turn_status = "timer"
            count_down.reset() # Reset the countdown
                    



class CountDown:
    """Countdown object for handling timer"""
    def __init__(self, settings, screen) -> None:
        "Init the item"
        self.settings = settings
        self.value_default = settings["default_count_down"]
        self.value = self.value_default
        
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.txt_color = pygame.Color('white')
    
        SIZE = 136
        self.font = pygame.font.SysFont(None, SIZE)
        
        self.prop_countdown()
         
    def up_date(self):
        "Update the value"
        if self.value > 0:
            self.value -= 1
        pygame.display.set_caption(f'Countdown: {self.value}')
        if self.value == 0:
            print('Time\'s up!')
            return 1
        return 0;
    
    def reset(self):
        """Reset the countdown when needed"""
        self.value = self.settings["default_count_down"]
                   
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

        self.txt_color = pygame.Color('red')
        self.font = pygame.font.SysFont(None, 36)
        self.prop_score()
        self.prop_high_score()
        self.prop_level()
        self.prop_player_life()
        
    def prop_score(self):
        """Prop scorboard text."""
        str_score = f"Score : {self.stats.score}"
        self.score_as_image = self.font.render(str_score, True, self.txt_color, self.settings["screen_color"])
        self.score_rect = self.score_as_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 10

    def prop_high_score(self):
        """Prop scorboard  high score text."""
        high_score = int(round(self.stats.high_score, -1))
        str_high_score = "High Score : {:,}".format(high_score)
        self.high_as_image = self.font.render(str_high_score, True, self.txt_color, self.settings["screen_color"])
        self.high_score_rect = self.high_as_image.get_rect()
        self.high_score_rect.right = self.score_rect.right
        self.high_score_rect.top = self.score_rect.bottom

    def prop_level(self):
        """Prop scorboard level text."""
        str_level = f"Level : {self.stats.level}"
        self.level_as_image = self.font.render(str_level, True, self.txt_color, self.settings["screen_color"])
        self.level_rect = self.level_as_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.high_score_rect.bottom

    def prop_player_life(self):
        """Prop ships left until death."""
        self.lives = pygame.sprite.Group()
        for live in range(self.stats.lives):
            heart = Heart()
            heart.rect.x = 10 + live * heart.rect.width
            heart.rect.y = 10
            self.lives.add(heart)
            

    def show(self):
        """Draw score screen."""
        self.screen.blit(self.score_as_image, self.score_rect)
        self.screen.blit(self.high_as_image, self.high_score_rect)
        self.screen.blit(self.level_as_image, self.level_rect)
        self.lives.draw(self.screen)

