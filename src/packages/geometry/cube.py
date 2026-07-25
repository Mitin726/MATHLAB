from figure3D import Figure3D
import math

class Cube(Figure3D):
    def __init__(self, side: float):
        if side <= 0:
            raise ValueError("The side must be greater than zero...")
        
        self.side = side
        
    def calculate_volume(self):
        return self.side**3
    
    def calculate_surface_area(self):
        return (self.side**2) * 6
    
    def __str__(self):
        return f"Cube\nside: {self.side}"
    
    def info(self):
        return f"""
                {self}
                Volume: {self.calculate_volume():.2f}
                Surface Area: {self.calculate_surface_area():.2f}
                """