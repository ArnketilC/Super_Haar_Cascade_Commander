import pygame 

GREEN = (10, 90, 10)
BLACK = (0, 0, 0)
GRID_WIDTH = 3


class Grid():
    """Game grid object with all filler"""
    def __init__(self, settings):
        self.grid_nb = settings["grid_nb"] #     "grid_nb": [30, 20]
        self.x_start = 20
        self.y_start = 100
        self.size = self.findGridSize(settings)
        self.filled = [["" for i in range(self.grid_nb[0])] for j in range(self.grid_nb[1])]
        self.rect = pygame.Rect(self.x_start, self.y_start, self.size*self.grid_nb[0], self.size*self.grid_nb[1])
  
    def findGridSize(self, settings):
        "Calculate grid size for the game"
        size = []
        for i in range(2):
            resolution_w_border = settings['resolution'][i]-self.grid_nb [i]*1+1  -self.x_start
            size.append(int( resolution_w_border / self.grid_nb [i]))

        if size[0]>size[1]: return size[1]
        else: return size[0]
   

                     
    def drawGrid(self, screen, player, monster):
        """Draw the grid in pygame"""
        pygame.draw.rect(screen, GREEN, self.rect)
        for y, ligne in enumerate(self.filled):
            for x, filling in enumerate(ligne):
                match filling:
                    case "":
                        pass
                    case "p":
                        screen.blit(player.image, pygame.Rect(x*self.size+self.x_start+GRID_WIDTH, 
                                        y*self.size+self.y_start+GRID_WIDTH, 
                                        self.size, 
                                        self.size))
                    case "m":
                        screen.blit(monster.image, pygame.Rect(x*self.size+self.x_start+GRID_WIDTH, 
                                        y*self.size+self.y_start+3, 
                                        self.size, 
                                        self.size)) 
                    case _:
                        pass
                rect = pygame.Rect(x*self.size+self.x_start, 
                                    y*self.size+self.y_start, 
                                    self.size, 
                                    self.size)
                pygame.draw.rect(screen, BLACK, rect, GRID_WIDTH)  

        def isAllowed(self, target):
            """Check if the move target is allowed"""
            max_x = self.grid_nb[1]-1
            max_y = self.grid_nb[0]-1
            
                    
    # def updatePosition(self, player):
if __name__ == "__name__":
    pass