class Actor():
    def __init__(self, name, init_position):
        "Init an actor character"
        self.name = name
        self.position = init_position
        
    def move(self, key, max):
        """Handle movements"""
        match key:
            case "up":
                if 0 < self.position[1]: 
                    self.position[1] -= 1
                    print(f"{self.name} moved up")
            case "down":
                if max > self.position[1]: 
                    self.position[1] += 1
                    print(f"{self.name} moved down")
            case "left":
                if 0 < self.position[0]: 
                    self.position[0] -= 1
                    print(f"{self.name} moved left")
            case "right":
                if max > self.position[0]: 
                    self.position[0] += 1
                    print(f"{self.name} moved rigth")
            case _:
                pass
        

class Player(Actor):
    def __init__(self, name="Player"):
        """Init the player character"""
        super().__init__(name, init_position=[0, 0])
        
class Monster(Actor):
    def __init__(self, name, init_position):
        """Init the player character"""
        super().__init__(name, init_position)