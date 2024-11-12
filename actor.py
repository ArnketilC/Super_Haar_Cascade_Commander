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
        
        grid.filled[init_position[1]][init_position[0]] = self
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

class Bush(Entity):
    def __init__(self, grid, name, init_position):
        "Init an actor character"
        super().__init__(grid, name, init_position, "bushes.png")

class Rock(Entity):
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
                if 0 < self.position[1] and grid.filled[self.position[1] -1][self.position[0]] == "": 
                    grid.filled[self.position[1]][self.position[0]] = ""
                    self.position[1] -= 1
                    print(f"{self.name} moved up")
            case "down":
                if max_x> self.position[1] and grid.filled[self.position[1] +1][self.position[0]] == "": 
                    grid.filled[self.position[1]][self.position[0]] = ""
                    self.position[1] += 1
                    print(f"{self.name} moved down")
            case "left":
                if 0 < self.position[0] and grid.filled[self.position[1]][self.position[0]-1] == "": 
                    grid.filled[self.position[1]][self.position[0]] = ""
                    self.position[0] -= 1
                    print(f"{self.name} moved left")
            case "right":
                if max_y > self.position[0] and grid.filled[self.position[1]][self.position[0]+1] == "": 
                    grid.filled[self.position[1]][self.position[0]] = ""
                    self.position[0] += 1
                    print(f"{self.name} moved right")
            case _:
                pass

    def attack(self):
        """Attacking method for all actors"""
        pass
    
    def action(self, grid):
        """Do the queues actions"""
        try : 
            self.move(self.action_queue.pop(0), grid)
        except:
            pass
        if len(self.action_queue) == 0:
            return TURN_ORDER[self.order+1]
        return TURN_ORDER[self.order]
    


class Player(Actor):
    def __init__(self, grid, name="Player"):
        """Init the player character"""
        init_position = [0,0]
        super().__init__(grid, name, init_position, "player.png")
        self.action_queue = []
        self.type = "player"
        self.order = 0
        
    def queue_action(self, action):
        """Queue action for the player"""
        if len(self.action_queue)<4:
            self.action_queue.append(action)
            print(f"Action queue : {action}")
        
    def move(self, key, grid):
        """Move the player"""
        super().move(key, grid)
        grid.filled[self.position[1]][self.position[0]] = self
        
    def attack(self, monster):
        """Attack method to deal with enemy"""
        pass
    
    def guard(self, monster):
        """Guard one attack comming from a monster"""
        pass
    

 

class Monster(Actor):
    def __init__(self, grid, name, init_position, image):
        """Init the player character"""
        super().__init__(grid, name, init_position, image)
        self.type = "monster"
        self.order = 1
        
    def move(self, int_direct, grid):
        """Move the monster"""
        key = QUARDINAL[int_direct]
        super().move(key, grid)
        grid.filled[self.position[1]][self.position[0]] = self
        
        
class Warrior(Monster):
    def __init__(self, grid, id, init_position):
        """Init the warrior ennemy type"""
        name = f"Warrior: id{id}"
        super().__init__(grid, name, init_position, "warrior.png")

class Archer(Monster):
    def __init__(self, grid, id, init_position):
        """Init the warrior ennemy type"""
        name = f"Archer: id{id}"
        super().__init__(grid, name, init_position, "archer.png")
  
        
if __name__ == "__name__":
    pass