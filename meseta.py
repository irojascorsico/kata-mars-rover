class Meseta:

    def __init__(self, width , height):
        self.width=width 
        self.height=height

    def __str__(self):
        return f"Meseta {self.width }x{self.height}"
    
    def within_the_limits(self, x, y ):
        return 0 <= x < self.width  and 0 <= y < self.height