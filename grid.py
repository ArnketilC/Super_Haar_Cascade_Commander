
WHITE = (200, 200, 200)

class Grid():
    """Game grid object with all filler"""
    def __init__(self, settings):
        self.grid_nb = settings["grid_nb"]
        self.size = self.findGridSize(settings)
        print(self.size)
             
    def findGridSize(self, settings):
        "Calculate grid size for the game"
        # x = settings['resolution'][0]
        # y = settings['resolution'][1]
        size = []
        for i in range(2):
            resolution_w_border = settings['resolution'][i]-self.grid_nb [i]*1+1  -20
            size.append(int( resolution_w_border / self.grid_nb [i]))

        if size[0]>size[1]: return size[1]
        else: return size[0]
        
    def drawGrid(self, screen, pygame):
        """Draw the grid in pygame"""
        for x in range(10, self.grid_nb[0]*self.size, self.size):
            for y in range(10, self.grid_nb[1]*self.size, self.size):
                rect = pygame.Rect(x, y, self.size, self.size)
                pygame.draw.rect(screen, WHITE, rect, 1)
                
    def drawPlayer(self, screen, pygame, player):
        """Draw the player"""
        pygame.draw.circle(screen, 
                           "red",
                           (player.position[0] * self.size, 
                            player.position[1] * self.size), 
                           self.size/2)
