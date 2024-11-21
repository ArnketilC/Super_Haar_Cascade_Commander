import pygame
import sys
from os import path

GRID_WIDTH = 1

QUARDINAL={
    0:"up",
    1:"down",
    2:"left",
    3:"right"
}


class Entity():    
    def __init__(self, grid,  name, init_position, image):
        "Init an actor character"
        self.name = name
        self.position = init_position
        
        grid.filled[init_position[1]][init_position[0]].inside = self
        self.image = pygame.image.load(path.join(sys.path[0], f"resources/{image}"))
        self.image = pygame.transform.scale(self.image, (grid.size , grid.size ))
        self.rect = self.image.get_rect()
        
    def draw_self(self, screen, grid, x, y):
        screen.blit(self.image, pygame.Rect(x*grid.size+grid.x_start+GRID_WIDTH, 
                    y*grid.size+grid.y_start+3, 
                    grid.size, 
                    grid.size))   
        
class Obstacle(Entity):
    def __init__(self, grid, name, init_position, image):
        "Init an actor character"
        super().__init__(grid, name, init_position, image)
        self.object_type = "Obstacle"
class Bush(Obstacle):
    def __init__(self, grid, name, init_position):
        "Init an actor character"
        super().__init__(grid, name, init_position, "bushes.png")

class Rock(Obstacle):
    def __init__(self, grid, name, init_position):
        "Init an actor character"
        super().__init__(grid, name, init_position, "rocks.png")         
      
class Actor(Entity):
    def __init__(self, grid, name, init_position, image):
        "Init an actor character"
        super().__init__(grid, name, init_position, image)
        self.action_queue = []
        
    def move(self, key, grid):
        """Handle movements"""
        max_x = grid.grid_nb[1]-1
        max_y = grid.grid_nb[0]-1
        
        # GODDAMMM PYTHON 3.9        
        # match key:
        #     case "up":
        #         if 0 < self.position[1] and grid.filled[self.position[1] -1][self.position[0]].inside == "": 
        #             grid.filled[self.position[1]][self.position[0]].inside = ""
        #             self.position[1] -= 1
        #             print(f"{self.name} moved up")
        #     case "down":
        #         if max_x> self.position[1] and grid.filled[self.position[1] +1][self.position[0]].inside == "": 
        #             grid.filled[self.position[1]][self.position[0]].inside = ""
        #             self.position[1] += 1
        #             print(f"{self.name} moved down")
        #     case "left":
        #         if 0 < self.position[0] and grid.filled[self.position[1]][self.position[0]-1].inside == "": 
        #             grid.filled[self.position[1]][self.position[0]].inside = ""
        #             self.position[0] -= 1
        #             print(f"{self.name} moved left")
        #     case "right":
        #         if max_y > self.position[0] and grid.filled[self.position[1]][self.position[0]+1].inside == "": 
        #             grid.filled[self.position[1]][self.position[0]].inside = ""
        #             self.position[0] += 1
        #             print(f"{self.name} moved right")
        #     case "attack":
        #         score = self.attack(grid, self.target)
        #         try:
        #             self.score_update(score)
        #         except:
        #             pass
        #     case _:
        #         pass

       # match key:
        if key == "up":
                if 0 < self.position[1] and grid.filled[self.position[1] -1][self.position[0]].inside == "": 
                    grid.filled[self.position[1]][self.position[0]].inside = ""
                    self.position[1] -= 1
                    print(f"{self.name} moved up")
        elif key == "down":
                if max_x> self.position[1] and grid.filled[self.position[1] +1][self.position[0]].inside == "": 
                    grid.filled[self.position[1]][self.position[0]].inside = ""
                    self.position[1] += 1
                    print(f"{self.name} moved down")
        elif key == "left":
                if 0 < self.position[0] and grid.filled[self.position[1]][self.position[0]-1].inside == "": 
                    grid.filled[self.position[1]][self.position[0]].inside = ""
                    self.position[0] -= 1
                    print(f"{self.name} moved left")
        elif key =="right":
                if max_y > self.position[0] and grid.filled[self.position[1]][self.position[0]+1].inside == "": 
                    grid.filled[self.position[1]][self.position[0]].inside = ""
                    self.position[0] += 1
                    print(f"{self.name} moved right")
        elif key =="attack":
                score = self.attack(grid, self.target)
                try:
                    self.score_update(score)
                except:
                    pass

        

    def attack(self, grid, target_name):
        """Attack method to deal with enemy"""
        score = 0
        for i in range(-1,2,2):
            try:
                target = grid.filled[self.position[1]+i][self.position[0]]
                if not target.is_empty():
                    if target.inside.object_type  == target_name:
                        print(f"{self.name} is attacking:{target_name}")
                        score += target.inside.hit(grid)
            except:
                pass
            try:
                target = grid.filled[self.position[1]][self.position[0]+i]
                if not target.is_empty():
                    if target.inside.object_type  == target_name:
                        print(f"{self.name} is attacking: {target_name}")
                        score += target.inside.hit(grid)
            except:
                pass  
        return score 
            
            
    def queue_action(self, action):
        """Queue action for the player"""
        if len(self.action_queue)<4:
            self.action_queue.append(action)
            print(f"Action queue : {action}")


    def action(self, grid):
        """Do the queues actions"""
        if len(self.action_queue)<=0: return 1
        self.move(self.action_queue.pop(0), grid)   
        return 0

class Player(Actor):
    def __init__(self, grid, stats, sb, name="player"):
        """Init the player character"""
        init_position = [0,0]
        super().__init__(grid, name, init_position, "player.png")
        self.object_type = "player"
        self.stats = stats
        self.sb = sb
        self.target = "monster"
        self.invincibility = False
        

    def move(self, key, grid):
        """Move the player"""
        super().move(key, grid)
        grid.filled[self.position[1]][self.position[0]].inside = self
        
    def hit(self, grid):
        """Player is hit"""
        if self.invincibility == False:
            self.stats.lives -= 1
            self.sb.prop_player_life()
            print("player got hit")
        else :
            print("player dodge the second attack")
        if self.stats.lives <= 0:
            self.stats.game_run = False
            pygame.mouse.set_visible(True)

        
    def guard(self, monster):
        """Guard one attack comming from a monster"""
        pass

    def score_update(self, score_to_add):
        """Update the score board"""
        self.stats.score += score_to_add
        self.sb.prop_score()
        self.check_player_high_score()
        
    def check_player_high_score(self):
        """Update the high score"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.sb.prop_high_score()
        

from random import randrange

class Monster(Actor):
    def __init__(self, grid, name, init_position, image):
        """Init the player character"""
        super().__init__(grid, name, init_position, image)
        self.object_type = "monster"
        self.id
        self.point_value = 0
        self.target = "player"
        
    def move(self, key, grid):
        """Move the monster"""
        super().move(key, grid)
        grid.filled[self.position[1]][self.position[0]].inside = self
        
    def hit(self, grid):
        """Handling of ennemies getting killed + score"""
        grid.filled[self.position[1]][self.position[0]].inside = ""
        grid.monsters.pop(self.id)
        
        return self.point_value
    
    def monster_queue(self):
        """Action of monster"""
        self.action_queue.append(QUARDINAL[randrange(4)])
        self.action_queue.append("attack")
        
        
class Warrior(Monster):
    def __init__(self, grid, id, init_position):
        """Init the warrior ennemy type"""
        self.id = id        
        name = f"Warrior: id{self.id}"
        super().__init__(grid, name, init_position, "warrior.png")
        self.point_value = 100

class Archer(Monster):
    def __init__(self, grid, id, init_position):
        """Init the warrior ennemy type"""
        self.id = id
        name = f"Archer: id{self.id}"
        super().__init__(grid, name, init_position, "archer.png")
        self.point_value = 200
        
from pygame.sprite import Sprite
class Heart(Sprite):
    def __init__(self):
        super(Heart, self).__init__()
        self.image = pygame.image.load(path.join(sys.path[0], f"resources/heart.png"))
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        
if __name__ == "__name__":
    pass