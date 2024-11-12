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

TURN_ORDER=["player", "monster", "next"]
    

class Entity():    
    def __init__(self, grid,  name, init_position, image):
        "Init an actor character"
        self.name = name
        self.position = init_position
        
        grid.filled[init_position[1]][init_position[0]].inside = self
        self.image = pygame.image.load(path.join(sys.path[0], f"resources/{image}"))
        self.image = pygame.transform.scale(self.image, (50, 50))
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
        
    def move(self, key, grid):
        """Handle movements"""
        max_x = grid.grid_nb[1]-1
        max_y = grid.grid_nb[0]-1
        
        match key:
            case "up":
                if 0 < self.position[1] and grid.filled[self.position[1] -1][self.position[0]].inside == "": 
                    grid.filled[self.position[1]][self.position[0]].inside = ""
                    self.position[1] -= 1
                    print(f"{self.name} moved up")
            case "down":
                if max_x> self.position[1] and grid.filled[self.position[1] +1][self.position[0]].inside == "": 
                    grid.filled[self.position[1]][self.position[0]].inside = ""
                    self.position[1] += 1
                    print(f"{self.name} moved down")
            case "left":
                if 0 < self.position[0] and grid.filled[self.position[1]][self.position[0]-1].inside == "": 
                    grid.filled[self.position[1]][self.position[0]].inside = ""
                    self.position[0] -= 1
                    print(f"{self.name} moved left")
            case "right":
                if max_y > self.position[0] and grid.filled[self.position[1]][self.position[0]+1].inside == "": 
                    grid.filled[self.position[1]][self.position[0]].inside = ""
                    self.position[0] += 1
                    print(f"{self.name} moved right")
            case "attack":
                self.attack(grid)
            case _:
                pass

    def action(self, grid):
        """Do the queues actions"""
        if len(self.action_queue) == 0:
            return TURN_ORDER[self.order+1]
        
        self.move(self.action_queue.pop(0), grid)
        
        return TURN_ORDER[self.order]
    


class Player(Actor):
    def __init__(self, grid, name="Player"):
        """Init the player character"""
        init_position = [0,0]
        super().__init__(grid, name, init_position, "player.png")
        self.action_queue = []
        self.object_type = "player"
        self.order = 0
        
    def queue_action(self, action):
        """Queue action for the player"""
        if len(self.action_queue)<4:
            self.action_queue.append(action)
            print(f"Action queue : {action}")
        
    def move(self, key, grid):
        """Move the player"""
        super().move(key, grid)
        grid.filled[self.position[1]][self.position[0]].inside = self
        
    def attack(self, grid):
        """Attack method to deal with enemy"""

        for i in range(-1,2,2):
            target = grid.filled[self.position[1]+i][self.position[0]]
            if not target.is_empty():
                if target.inside.object_type  == "monster":
                    print("MonsterFound !")
                    target.inside.killed(grid)
                    break
            target = grid.filled[self.position[1]][self.position[0]+i]
            if not target.is_empty():
                if target.inside.object_type  == "monster":
                    print("MonsterFound !")
                    target.inside.killed(grid)
                    break
        
    def guard(self, monster):
        """Guard one attack comming from a monster"""
        pass
    

 

class Monster(Actor):
    def __init__(self, grid, name, init_position, image):
        """Init the player character"""
        super().__init__(grid, name, init_position, image)
        self.object_type = "monster"
        self.order = 1
        self.id
        
    def move(self, int_direct, grid):
        """Move the monster"""
        key = QUARDINAL[int_direct]
        super().move(key, grid)
        grid.filled[self.position[1]][self.position[0]].inside = self
        
    def killed(self, grid):
        grid.filled[self.position[1]][self.position[0]].inside = ""
        grid.monsters.pop(self.id)
        
class Warrior(Monster):
    def __init__(self, grid, id, init_position):
        """Init the warrior ennemy type"""
        self.id = id        
        name = f"Warrior: id{self.id}"
        super().__init__(grid, name, init_position, "warrior.png")


class Archer(Monster):
    def __init__(self, grid, id, init_position):
        """Init the warrior ennemy type"""
        self.id = id
        name = f"Archer: id{self.id}"
        super().__init__(grid, name, init_position, "archer.png")

from pygame.sprite import Sprite
class Heart(Sprite):
    def __init__(self):
        super(Heart, self).__init__()
        self.image = pygame.image.load(path.join(sys.path[0], f"resources/heart.png"))
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        
if __name__ == "__name__":
    pass