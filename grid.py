
WHITE = (200, 200, 200)

class Grid():
    """Game grid object with all filler"""
    def __init__(self, settings):
        self.grid_nb = settings["grid_nb"] #     "grid_nb": [30, 20]
        self.x_start = 20
        self.y_start = 100
        self.size = self.findGridSize(settings)
        self.filled = [["" for i in range(self.grid_nb[0])] for j in range(self.grid_nb[1])]
  
    def findGridSize(self, settings):
        "Calculate grid size for the game"
        size = []
        for i in range(2):
            resolution_w_border = settings['resolution'][i]-self.grid_nb [i]*1+1  -self.x_start
            size.append(int( resolution_w_border / self.grid_nb [i]))

        if size[0]>size[1]: return size[1]
        else: return size[0]
   
                     
    def drawGrid(self, screen, pygame):
        """Draw the grid in pygame"""
        
        for y, ligne in enumerate(self.filled):
            for x, filling in enumerate(ligne):
                match filling:
                    case "":
                        rect = pygame.Rect(x*self.size+self.x_start, 
                                        y*self.size+self.y_start, 
                                        self.size, 
                                        self.size)
                        pygame.draw.rect(screen, WHITE, rect, 1)    
                    case "p":
                        pygame.draw.circle(screen, 
                                            "red",
                                            (x*self.size+self.size/2+self.x_start, 
                                            y*self.size+self.size/2+self.y_start), 
                                            self.size/3)                       
                    case "m":
                        pygame.draw.circle(screen, 
                                            "green",
                                            (x*self.size+self.size/2+self.x_start, 
                                            y*self.size+self.size/2+self.y_start), 
                                            self.size/3)     
                    case _:
                        pass

                    
    # def updatePosition(self, player):
if __name__ == "__name__":
    pass