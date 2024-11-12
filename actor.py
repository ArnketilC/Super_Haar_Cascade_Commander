class Actor():
    def __init__(self, name, init_position):
        "Init an actor character"
        self.name = name
        self.position = init_position
        print(type(init_position))
        
    def move(self, key, grid):
        """Handle movements"""
        max_x = grid.grid_nb[1]-1
        max_y = grid.grid_nb[0]-1
        
        grid.filled[self.position[1]][self.position[0]] = ""
        
        match key:
            case "up":
                if 0 < self.position[1]: 
                    self.position[1] -= 1
                    print(f"{self.name} moved up")
            case "down":
                if max_x> self.position[1]: 
                    self.position[1] += 1
                    print(f"{self.name} moved down")
            case "left":
                if 0 < self.position[0]: 
                    self.position[0] -= 1
                    print(f"{self.name} moved left")
            case "right":
                if max_y > self.position[0]: 
                    self.position[0] += 1
                    print(f"{self.name} moved right")
            case _:
                pass



class Player(Actor):
    def __init__(self, grid, name="Player"):
        """Init the player character"""
        super().__init__(name, init_position=[0, 0])
        grid.filled[0][0] = "p"
        
    def move(self, key, grid):
        """Move the player"""
        super().move(key, grid)
        grid.filled[self.position[1]][self.position[0]] = "p"
        

QUARDINAL={
    0:"up",
    1:"down",
    2:"left",
    3:"right"
}
class Monster(Actor):
    def __init__(self, grid, name, init_position):
        """Init the player character"""
        super().__init__(name, init_position)
        grid.filled[init_position[1]][init_position[0]] = "m"
        
    def move(self, int_direct, grid):
        """Move the monster"""
        key = QUARDINAL[int_direct]
        super().move(key, grid)
        grid.filled[self.position[1]][self.position[0]] = "m"
        
if __name__ == "__name__":
    pass