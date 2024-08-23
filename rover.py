from meseta import Meseta

class Rover:
    def __init__(self, x, y, direction, meseta):
        self.x=x
        self.y=y
        self.direction=direction
        self.meseta=meseta

    def move(self,commands):
        ORIENTATIONS = {
        "N": {"x": 0, "y": 1, "left":"W", "right":"E"},
        "E": {"x": 1, "y":0, "left":"N", "right":"S"},
        "S": {"x": 0,"y": -1, "left":"E", "right":"W"},
        "W": {"x": -1,"y": 0, "left":"S", "right":"N"},
        }

        for command in commands:
            action= ORIENTATIONS[self.direction] 
            x= action['x']
            y= action['y']
            if command=="F":
                if self.meseta.within_the_limits(self.x+x,self.y+y):
                    self.x+=x
                    self.y+=y
            if command=="B":
                if self.meseta.within_the_limits(self.x+x,self.y+y):
                    self.x-=x
                    self.y-=y
            if command=="L":
                    self.direction=action['left']
            if command=="R":
                    self.direction=action['right']
            
    def get_current_position(self):
        return f"({self.x},{self.y},{self.direction})"
